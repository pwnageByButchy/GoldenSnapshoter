class Vmware:
    def __init__(self, filepath):
        self.self.vm = filepath
        self.guest_os = determineGuestOS()
        self.vmware_type = ""
        self.base_image = ""
        self.guest_user = ""
        self.guest_password = ""
        self.update_script = ""

    # Snapshot the VMs, ensure update files exist if not copy them to VM
    def snapshotProcess():
        vmrun - T self.vmware_type revertToSnapshot self.vm self.base_image
        vmrun - T self.vmware_type start self.vm
        if self.guest_os == "Linux":
            fileExists = vmrun - T self.vmware_type - gu self.guest_user - gp self.guest_password fileExistsInGuest self.vm / self.update_script
            if fileExists == false:
                vmrun - T self.vmware_type - gu self.guest_user - gp self.guest_password copyFileFromHostToGuest self.vm ./UpdateScripts/self.update_script / self.update_script
            vmrun - T self.vmware_type - gu self.guest_user - gp self.guest_password runScriptInGuest self.vm - interactive "" "/bin/bash /" + self.update_script
        elif self.guest_os == "Windows":
            fileExists = vmrun - T self.vmware_type - gu self.guest_user - gp self.guest_password fileExistsInGuest self.vm / self.update_script
            if fileExists == false:
                vmrun - T self.vmware_type - gu self.guest_user - gp self.guest_password copyFileFromHostToGuest self.vm ./UpdateScripts/self.update_script "C:\\" + self.update_script
            vmrun - T self.vmware_type - gu self.guest_user - gp self.guest_password runScriptInGuest self.vm - interactive "" "cmd.exe C:\\" + self.update_script
        else:
            print("Unknown Guest OS, please set Guest OS Identifier")
        vmrun - T self.vmware_type snapshot self.vm self.base_image

    # determine the OS of the Virtual Guest, needed for Update file
    # ie. bash file for *nix and powershell for windows
    def determineGuestOS():
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
