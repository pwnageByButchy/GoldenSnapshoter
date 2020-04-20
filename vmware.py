import os
import time


class Vmware:
    def __init__(self, filepath):
        self.vm = filepath
        self.guest_os = self.determineGuestOS(self)
        self.vmware_type = ""
        self.base_image = ""
        self.guest_user = ""
        self.guest_password = ""
        self.update_script = ""
        # comment

    # Snapshot the VMs, ensure update files exist if not copy them to VM
    @staticmethod
    def snapshotProcess(self):
        # snapshot machine
        print("...Reverting to Base Image")
        revert_machine = 'vmrun -T {0} revertToSnapshot {1} {2}'.format(self.vmware_type, self.vm, self.base_image)
        os.system(revert_machine)
        # start machine up
        print("...Starting reverted VM")
        start_machine = 'vmrun -T {0} start {1}'.format(self.vmware_type, self.vm)
        os.system(start_machine)
        # give it enough time to boot
        time.sleep(20)
        # run script in guest... can you run a local script in the vm... if so this is simpler
        # put runScript command here
        # shutdown the newly updated VM
        print("...Shutting down VM")
        stop_machine = 'vmrun -T {0} stop {1}'.format(self.vmware_type, self.vm)
        os.system(stop_machine)
        time.sleep(20)
        # after process snapshot to make a new base_image
        print("...Deleting old snapshot")
        snapshot_delete = 'vmrun -T {0} deleteSnapshot {1} {2}'.format(self.vmware_type, self.vm, self.base_image)
        os.system(snapshot_delete)

        print("...Creating new Base Image")
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
