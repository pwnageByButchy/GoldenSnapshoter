from utilities import Utilities
from vmware import Vmware
from settings import Settings
print("Starting...")


def main():
    print("\n")
    print("Attempting to load settings...")

    my_settings = Settings()

    print("...Settings Loaded")
    print("\n")
    print("Searching for VMs...")
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
        new_vm.snapshotProcess(new_vm)
        print("...Snapshot Completed...")
        print("\n")


if __name__ == "__main__":
    main()
