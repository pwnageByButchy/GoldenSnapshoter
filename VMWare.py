# File to cover off all the VMWare Components
# make this a class you wally!!!!


# Snapshot the VMs, ensure update files exist if not copy them to VM
def snapshotProcess(vm, guestUser, guestPassword, guestOS, vmWareType):
    vmrun - T vmWareType revertToSnapshot vm baseImageName
    vmrun - T vmWareType start vm
   if guestOS == "Linux":
        fileExists = vmrun - T vmWareType - gu guestUser - gp guestpasswd fileExistsInGuest vm / update.sh
        if fileExists == false:
            vmrun - T vmWareType - gu guestUser - gp guestpasswd copyFileFromHostToGuest vm ./UpdateScripts/UpdateWithAPT.sh / update.sh
        vmrun - T vmWareType - gu guestUser - gp guestpasswd runScriptInGuest vm - interactive "" "/bin/bash /update.sh"
    elif guestOS == "Windows":
        fileExists = vmrun - T vmWareType -gu guestUser -gp guestpasswd fileExistsInGuest vm /update.ps1
        if fileExists == false:
            vmrun - T vmWareType -gu guestUser -gp guestpasswd copyFileFromHostToGuest vm ./UpdateScripts/UpdateWithPS.ps1 C:\update.ps1
        vmrun - T vmWareType -gu guestUser -gp guestpasswd runScriptInGuest vm -interactive "" "cmd.exe C:\update.ps1"
    else:
        print("Unknown Guest OS, please set Guest OS Identifier")
    vmrun - T vmWareType snapshot vm baseImageName


# determine the OS of the Virtual Guest, needed for Update file ie. bash file for *nix and powershell for windows
def determineGuestOS(vm):
    result = ""
    with open(vm) as search:
        for line in search:
            line = line.rstrip()  # remove '\n' at end of line
            if "guestOS" == line:
                line.replace(' ', '')
                line.split('=')
                if "win" in line[1]:
                    result = "Windows"
                    return result
                else:
                    result = "Linux"
                    return result
