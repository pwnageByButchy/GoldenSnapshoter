import os


class Utilities:
    def __init__(self, directory, ext):
        self.vmDirectory = directory
        self.extension = ext
        self.found_files = self.find_files_by_extension(self)

    # Simply loop through directory looking for VMs
    @staticmethod
    def find_files_by_extension(self):
        # create a list of file and sub directories
        # names in the given directory
        vm_files = []
        print(self.extension)
        print(self.vmDirectory)

        for root, dirs, files in os.walk(self.vmDirectory):
            for file in files:
                if file.endswith(self.extension):
                    vm_files.append(os.path.join(root, file))

        return vm_files
