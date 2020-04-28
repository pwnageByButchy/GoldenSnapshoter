import os
import time
import datetime
import subprocess
from utilities import Utilities
from settings import Settings
from updatescripts import Updatescripts


class Vmware:
    def __init__(self, filepath):
        self.my_settings = Settings()
        self.vm = filepath
        self.guest_os = self.determineGuestOS()
        self.vmware_type = self.my_settings.vmware_product
        self.base_image = self.my_settings.base_image
        # GuestOS If/Else statement around...
        if self.guest_os == "Windows":
            self.guest_user = self.my_settings.windows_guestuser
            self.guest_password = self.my_settings.windows_guestpass
            self.guest_script_path = self.my_settings.windows_scripts_path_in_guest
        else:
            self.guest_user = self.my_settings.linux_guestuser
            self.guest_password = self.my_settings.linux_guestpass
            self.guest_script_path = self.my_settings.linux_scripts_path_in_guest

        # IF/Else statement this!!!
        self.update_script = ""
        # comment

    # Snapshot the VMs, ensure update files exist if not copy them to VM
    def snapshotProcess(self):
        if self.baseImageExists():
            if self.my_settings.preserve_for_forensic_evidence:
                client_name = input("......Enter Client's name for Forensic Preservation:")
                client_name = client_name + "-" + datetime.datetime.now().strftime("%d-%m-%Y")
                self.vm_snapshot(client_name)
                do_i_clone = input("......Do I Clone this Snapshot? [N/y]:")
                if do_i_clone == 'y':
                    self.vm_create_clone(client_name)
            self.vm_revert()
            previous_snapshot = self.base_image + "-pre-" + datetime.datetime.now().strftime("%d-%m-%Y")
            self.vm_snapshot(previous_snapshot)
        else:
            # creating initial baseImage as it currently doesnt exist
            print("......A Base Image with the provided name " + self.base_image + " does not exist...So I am creating it!")
            self.vm_snapshot(self.base_image)

        # start machine up
        self.vm_start()
        # copying and running scripts on guest
        self.vm_run_scripts()
        print("......Stoping VM")
        while self.is_machine_running():
            time.sleep(40)
        # after process snapshot to make a new baseImage need to remove the old one first to prevent errors
        self.vm_delete_snapshot()
        self.vm_snapshot(self.base_image)

    def vm_revert(self):
        print("......Reverting to Base Image")
        revert_machine = 'vmrun -T {0} revertToSnapshot {1} {2}'.format(self.vmware_type, self.vm, self.base_image)
        os.system(revert_machine)
        print("......Renaming current base image")

    def vm_start(self):
        print("......Starting VM")
        start_machine = 'vmrun -T {0} start {1}'.format(self.vmware_type, self.vm)
        os.system(start_machine)
        # give it enough time to boot
        time.sleep(20)

    def vm_snapshot(self, imageName):
        print("......Creating new " + imageName)
        snapshot_machine = 'vmrun -T {0} snapshot {1} {2}'.format(self.vmware_type, self.vm, imageName)
        os.system(snapshot_machine)

    def vm_delete_snapshot(self):
        print("......Deleting old " + self.base_image)
        snapshot_delete = 'vmrun -T {0} deleteSnapshot {1} {2}'.format(self.vmware_type, self.vm, self.base_image)
        os.system(snapshot_delete)

    def vm_run_scripts(self):
        print("......Running script in VM")
        utilities = Utilities(self.my_settings.vm_directory, self.my_settings.extension)
        update_script = Updatescripts(self.vm)
        if utilities.find_if_file_exists(self.vm):
            print("......Script Present")
            self.update_script = update_script.set_update_script()
        else:
            print("......Creating Script")
            self.update_script = update_script.generate_update_script()
            print("......Script Created")
        print("......Copying Script to VM")
        # if/else statement here for is GuestOS Linux based of Windows
        copy_script_to_vm = 'vmrun -gu {0} -gp {1} -T {2} CopyFileFromHostToGuest {3} {4} {5}/UpdateScript.py'.format(
            self.guest_user, self.guest_password, self.vmware_type, self.vm, self.update_script, self.guest_script_path)
        os.system(copy_script_to_vm)
        print("......Copying Completed")
        print("......Running Script in VM")
        # file seems to be copied over with windows end of line chars
        convert_dos2unix = 'vmrun -gu {0} -gp {1} -T {2} runProgramInGuest {3} "/usr/bin/dos2unix" {4}/UpdateScript.py'.format(
            self.guest_user, self.guest_password, self.vmware_type, self.vm, self.guest_script_path)
        os.system(convert_dos2unix)
        run_script = 'vmrun -gu {0} -gp {1} -T {2} runProgramInGuest {3} "/usr/bin/python3" {4}/UpdateScript.py'.format(
            self.guest_user, self.guest_password, self.vmware_type, self.vm, self.guest_script_path)
        os.system(run_script)
        # end if/else statement here
        print("......Script Completed")

    def vm_create_clone(self, imageName):
        print("......Creating Clone of " + imageName)
        clone_machine = r'vmrun -T {0} clone {1} {2}\{3}\{3}.vmx full -snapshot={3} -cloneName={3}'.format(
            self.vmware_type, self.vm, self.my_settings.preserve_forensic_clone_directory, imageName)
        os.system(clone_machine)

    # determine the OS of the Virtual Guest, needed for Update file
    # ie. bash file for *nix and powershell for windows
    def determineGuestOS(self):
        with open(self.vm) as search:
            for line in search:
                line = line.rstrip()  # remove '\n' at end of line
                if "guestOS" == line:
                    line.replace(' ', '')
                    line.split('=')
                    if "win" in line[1]:
                        self.guest_os = "Windows"
                    else:
                        self.guest_os = "Linux"

    def baseImageExists(self):
        baseImage = bytes(self.base_image, 'utf-8')
        find_snapshot = r'vmrun -T {0} listSnapshots {1}'.format(self.vmware_type, self.vm)
        result = subprocess.check_output(find_snapshot, shell=True)
        if result.find(baseImage) != -1:
            return True

    def is_machine_running(self):
        is_machine_running = r'vmrun list'
        result = subprocess.check_output(is_machine_running, shell=True)
        if result.find(bytes('Total running VMs: 1', 'utf-8')) != -1:
            return True
        else:
            return False
