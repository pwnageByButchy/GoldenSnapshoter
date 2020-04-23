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
        self.guest_os = self.determineGuestOS(self)
        self.vmware_type = self.my_settings.vmware_product
        self.base_image = self.my_settings.base_image
        self.guest_user = self.my_settings.user
        self.guest_password = self.my_settings.guestpass
        self.update_script = ""
        # comment

    # Snapshot the VMs, ensure update files exist if not copy them to VM
    @staticmethod
    def snapshotProcess(self):
        if self.baseImageExists(self):
            if self.my_settings.preserve_for_forensic_evidence:
                client_name = input("......Enter Client's name for Forensic Preservation:")
                snapshot_machine = 'vmrun -T {0} snapshot {1} {2}-{3}'.format(
                    self.vmware_type, self.vm, client_name, datetime.datetime.now())
                os.system(snapshot_machine)

            # snapshot machine
            print("......Reverting to Base Image")
            revert_machine = 'vmrun -T {0} revertToSnapshot {1} {2}'.format(self.vmware_type, self.vm, self.base_image)
            os.system(revert_machine)
            print("......Renaming current base image")
            date_stamp = datetime.datetime.now()
            snapshot_machine = 'vmrun -T {0} snapshot {1} {2}-pre-{3}'.format(
                self.vmware_type, self.vm, self.base_image, date_stamp.strftime("%d-%b-%Y-%H%M"))
            os.system(snapshot_machine)
        else:
            # creating initial baseImage as it currently doesnt exist
            print("......A Base Image with the provided name " + self.base_image + " does not exist...So I am creating it!")
            snapshot_machine = 'vmrun -T {0} snapshot {1} {2}'.format(self.vmware_type, self.vm, self.base_image)
            os.system(snapshot_machine)

        # start machine up
        print("......Starting VM")
        start_machine = 'vmrun -T {0} start {1}'.format(self.vmware_type, self.vm)
        os.system(start_machine)
        # give it enough time to boot
        time.sleep(20)
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
        copy_script_to_vm = 'vmrun -gu {0} -gp {1} -T {2} CopyFileFromHostToGuest {3} {4} /root/UpdateScript.py'.format(
            self.guest_user, self.guest_password, self.vmware_type, self.vm, self.update_script)
        os.system(copy_script_to_vm)
        print("......Copying Completed")
        print("......Running Script in VM")
        convert_dos2unix = 'vmrun -gu {0} -gp {1} -T {2} runProgramInGuest {3} "/usr/bin/dos2unix" /root/UpdateScript.py'.format(
            self.guest_user, self.guest_password, self.vmware_type, self.vm)
        os.system(convert_dos2unix)
        run_script = 'vmrun -gu {0} -gp {1} -T {2} runProgramInGuest {3} "/usr/bin/python3" /root/UpdateScript.py'.format(
            self.guest_user, self.guest_password, self.vmware_type, self.vm)
        os.system(run_script)
        print("......Script Completed")
        print("......Stoping VM")
        while self.is_machine_running():
            time.sleep(3)
        # after process snapshot to make a new base_image
        print("......Deleting old " + self.base_image)
        snapshot_delete = 'vmrun -T {0} deleteSnapshot {1} {2}'.format(self.vmware_type, self.vm, self.base_image)
        os.system(snapshot_delete)

        print("......Creating new " + self.base_image)
        snapshot_machine = 'vmrun -T {0} snapshot {1} {2}'.format(self.vmware_type, self.vm, self.base_image)
        os.system(snapshot_machine)

    # determine the OS of the Virtual Guest, needed for Update file
    # ie. bash file for *nix and powershell for windows
    @staticmethod
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

    @staticmethod
    def baseImageExists(self):
        baseImage = bytes(self.base_image, 'utf-8')
        find_snapshot = r'vmrun -T {0} listSnapshots {1}'.format(self.vmware_type, self.vm)
        result = subprocess.check_output(find_snapshot, shell=True)
        if result.find(baseImage) != -1:
            return True

    @staticmethod
    def is_machine_running():
        is_machine_running = r'vmrun list'
        result = subprocess.check_output(is_machine_running, shell=True)
        if result.find(bytes('Total running VMs: 1', 'utf-8')) != -1:
            return True
        else:
            return False
