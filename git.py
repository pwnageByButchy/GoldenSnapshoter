import os
import sys
from settings import Settings


class Git:
    def __init__(self):
        self.my_settings = Settings()

    def generate_git_script(self):
        app_path = os.path.abspath(os.path.dirname(sys.argv[0]))
        git_file = app_path + '\\UpdateScripts\\git_script.txt'
        file = open(git_file, "w")
        file.write("import shutil\n\n")
        file.write("#### Copy from below here and paste it into whichever Update Script you want to add it too ####\n")
        # Create MyGit Repo folder
        file.write("if not os.path.exists('{0}'):\n".format(self.my_settings.my_git_directory))
        file.write("    os.makedirs('{0}')\n".format(self.my_settings.my_git_directory))
        # for loop looping through My Git Repos dictionary
        for repo_name in self.my_settings.my_git_repos:
            file.write("if not os.path.exists('{0}/{1}'):\n".format(self.my_settings.my_git_directory, repo_name))
            file.write("    os.system('git clone {0} {1}/{2}')\n".format(
                self.my_settings.my_git_repos[repo_name], self.my_settings.my_git_directory, repo_name))
        # if exists delete repo then git cloned
            file.write("else:\n")
            file.write("    shutil.rmtree('{0}/{1}')\n".format(self.my_settings.my_git_directory, repo_name))
            file.write("    os.system('git clone {0} {1}/{2}')\n\n".format(
                self.my_settings.my_git_repos[repo_name], self.my_settings.my_git_directory, repo_name))

        # Create 3rd Party Repo Directory
        file.write("if not os.path.exists('{0}'):\n".format(self.my_settings.external_git_directory))
        file.write("    os.makedirs('{0}')\n".format(self.my_settings.external_git_directory))

        # for loop looping through External Git Repos dictionary
        for repo_name in self.my_settings.external_git_repos:
            file.write("if not os.path.exists('{0}/{1}'):\n".format(self.my_settings.external_git_directory, repo_name))
            file.write("    os.system('git clone {0} {1}/{2}')\n".format(
                self.my_settings.external_git_repos[repo_name], self.my_settings.external_git_directory, repo_name))
        # if exists delete repo then git cloned
            file.write("else:\n")
            file.write("    shutil.rmtree('{0}/{1}')\n".format(self.my_settings.external_git_directory, repo_name))
            file.write("    os.system('git clone {0} {1}/{2}')\n\n".format(
                self.my_settings.external_git_repos[repo_name], self.my_settings.external_git_directory, repo_name))
        file.write("os.system('chown -R {0}:{0} {1}')\n".format(self.my_settings.linux_standard_user,
                                                                self.my_settings.my_git_directory))
        file.write("os.system('chown -R {0}:{0} {1}')\n".format(self.my_settings.linux_standard_user,
                                                                self.my_settings.external_git_directory))
        file.write("#### End Copying here ####\n\n")
        file.close()
