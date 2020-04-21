from utilities import Utilities
from vmware import Vmware
from settings import Settings
from updatescripts import Updatescripts
print("Starting...")


def main():
    print("\n")
    print("Attempting to load settings...")

    my_settings = Settings()
    # VMWare settings
    vmware_product = my_settings.vmware_product
    vm_directory = my_settings.vm_directory
    extension = my_settings.extension
    base_image = my_settings.base_image
    guest_user = my_settings.user
    guest_password = my_settings.guestpass

    # Git Repo settings
    my_git_directory = my_settings.my_git_directory
    external_git_directory = my_settings.external_git_directory
    my_git_repos = my_settings.my_git_repos
    external_git_repos = my_settings.external_git_repos

    print("...Settings Loaded")
    print("\n")
    print("Searching for VMs...")
    # Initialise Utilities class
    utility = Utilities(vm_directory, extension)
    utility.found_files
    print("...VMs found {0}", len(utility.found_files))
    print("\n")

    print("Beginning Snapshot Process")
    # looping through virtual machines and initiate snapshotProcess()
    for vm in utility.found_files:
        print("...Loading VM: ", vm)
        print("\n")
        new_vm = Vmware(vm)
        new_vm.vmware_type = vmware_product
        new_vm.base_image = base_image
        new_vm.guest_user = guest_user
        new_vm.guest_password = guest_password
        # Insert into here the creation of the update scripts
        print("...Creating Update Script...")
        # create_update_script = Updatescripts(my_git_directory, external_git_directory, my_git_repos, external_git_repos)
        # new_vm.updatescript = create_update_script
        # put it in between the above line and this line
        print("\n")
        print("...Snapshotting VM...")
        new_vm.snapshotProcess(new_vm)
        print("...Snapshot Completed...")
        print("\n")


if __name__ == "__main__":
    main()
