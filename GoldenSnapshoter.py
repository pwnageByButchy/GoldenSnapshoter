#!/usr/bin/env python3

try:
    from configparser import ConfigParser
    from utilities import Utilities
    from vmware import Vmware
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0


def main():
    # instantiate
    config = ConfigParser()
    # parse existing file
    config.read('settings.ini')
    # VMWare settings
    vmware_product = config['virtualisation']['vmware_product']
    vm_directory = config['virtualisation']['vm_directory']
    extension = config['virtualisation']['extension']
    base_image = config['virtualisation']['base_image']
    guest_user = config['virtualisation']['user']
    guest_password = config['virtualisation']['pass']
    # Git Repo settings
    my_git_directory = config['git']['my_git_directory']
    external_git_directory = config['git']['external_git_directory']
    my_git_repos = config['git']['my_git_directories']
    external_git_repos = config['git']['external_git_directories']
    # Initialise Utilities class
    utility = Utilities(vm_directory, extension)
    vms = utility
    for vm in vms:
        new_vm = Vmware(vm)
        new_vm.vmware_type = vmware_product
        new_vm.base_image = base_image
        new_vm.guest_user = guest_user
        new_vm.guest_password = guest_password
        new_vm.determineGuestOS()
        new_vm.snapshotProcess()