from utilities import Utilities
from vmware import Vmware
from settings import Settings
from git import Git
print("Starting...")


def main():
    print("\n")
    print("Attempting to load settings...")
    my_settings = Settings()
    print("...Settings Loaded")
    print("...Generating Git Script")
    new_git = Git()
    new_git.generate_git_script()
    print("\n")
    print("Searching for VMs...")
    if my_settings.virtualisation_platform == "vmware":
        # Initialise Utilities class
        utility = Utilities(my_settings.vm_directory, my_settings.extension)
        utility.found_files
        print("...VMs found " + str(len(utility.found_files)))
        print("\n")
        print("Beginning Snapshot Process")
        # looping through virtual machines and initiate snapshotProcess()
        for vm in utility.found_files:
            print("...Loading VM: ", vm)
            new_vm = Vmware(vm)
            print("\n")
            print("...Snapshotting VM...")
            new_vm.snapshotProcess()
            print("...Snapshot Completed...")
            print("\n")
    elif my_settings.virtualisation_platform == "virtualbox":
        print("\n")
        print("Aaaah havent written it yet!")
    else:
        print("\n")
        print("Unsupported Virtualisation Platform!")


if __name__ == "__main__":
    main()
