class Updatescripts:
    def __init__(self, my_git_directory, external_git_directory, my_git_repos, external_git_repos):
        self.my_git_directory = my_git_directory
        self.my_git_repos = my_git_repos
        self.external_git_directory = external_git_directory
        self.external_git_repos = external_git_repos

    def generate_update_script(guest_os):
