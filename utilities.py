import sys
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
        for root, dirs, files in os.walk(self.vmDirectory):
            for file in files:
                if file.endswith(self.extension):
                    vm_files.append(os.path.join(root, file))

        return vm_files

    @staticmethod
    def find_if_file_exists(file):
        pathname = os.path.dirname(sys.argv[0])
        app_path = os.path.abspath(pathname)
        fullpath = str(bytes(file, 'utf-8'))
        fullpath = fullpath.replace("'", "")
        parts = fullpath.split(r'\\')
        count = len(parts)
        file = parts[count-1]
        file = file[:-4] + ".sh"
        file = app_path + '\\UpdateScripts\\' + file
        return os.path.isfile(file)
