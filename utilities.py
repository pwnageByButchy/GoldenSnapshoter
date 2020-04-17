import os


class Utilities:
    def __init__(self, directory, ext):
        self.vmDirectory = directory
        self.extension = ext
        self.found_files = []

    # Simply loop through directory looking for VMs
    def find_files_by_extension():
        for root, dirs, files in os.walk(self.vmDirectory):
            for file in files:
                if file.endswith(self.extension):
                    self.found_files.append(os.path.join(root, file))
