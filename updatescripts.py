import sys
import os
import subprocess
from settings import Settings


class Updatescripts:
    def __init__(self, filepath):
        self.my_settings = Settings()
        self.my_git_directory = self.my_settings.my_git_directory
        self.my_git_repos = self.my_settings.my_git_repos
        self.external_git_directory = self.my_settings.external_git_directory
        self.external_git_repos = self.my_settings.external_git_repos
        self.fullpath = filepath

    # still to write this
    def generate_update_script(self):
        pathname = os.path.dirname(sys.argv[0])
        app_path = os.path.abspath(pathname)
        fullpath = str(bytes(self.fullpath, 'utf-8'))
        fullpath = fullpath.replace("'", "")
        parts = fullpath.split(r'\\')
        count = len(parts)
        file = parts[count-1]
        file = file[:-4] + ".py"
        source_file = app_path + '\\UpdateScripts\\' + "UpdateLinux.py"
        destination_file = app_path + '\\UpdateScripts\\' + file
        subprocess.check_output('copy ' + source_file + ' ' + destination_file, shell=True, universal_newlines=True)
        return app_path + '\\UpdateScripts\\' + file

    def set_update_script(self):
        pathname = os.path.dirname(sys.argv[0])
        app_path = os.path.abspath(pathname)
        fullpath = str(bytes(self.fullpath, 'utf-8'))
        fullpath = fullpath.replace("'", "")
        parts = fullpath.split(r'\\')
        count = len(parts)
        file = parts[count-1]
        file = file[:-4] + ".py"
        return app_path + '\\UpdateScripts\\' + file
