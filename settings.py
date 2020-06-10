class Settings:
    def __init__(self):
        # are you using vmware or virtualbox?
        self.virtualisation_platform = r'vmware'

        # What VMWare Product are you using ws = Workstation, fusion = VMWare Fusion, esx = ESX/ESXi hosts
        self.vmware_product = r'ws'

        # Directory of the VMs you wish to snapshot
        self.vm_directory = r'I:\Virtual Machines\Clients'

        # Extension VMware (.vmx) or VirtualBox (.vbox)
        self.extension = r'.vmx'

        # Name of your base image
        self.base_image = r'baseImage'

        # Linux GuestOS root username
        self.linux_guestuser = r'root'
        # Linux GuestOS root password
        self.linux_guestpass = r'password'
        # standard user username
        self.linux_standard_user = r'butchy'
        # Linux path to where scripts go
        self.linux_scripts_path_in_guest = r'/root'

        # Windows GuestOS username
        self.windows_guestuser = r'adminsitrator'
        # Windows GuestOS password
        self.windows_guestpass = r'password'
        # Windows path to where scripts go
        self.windows_scripts_path_in_guest = r'C:\Windows\temp'

        # I want to preserve my machine for forensic evidence as Reverting the VM will destroy any logs or files created
        # Set to True if you want to presverse this in your snapshot...meaning it will be snapshotted before being reverted
        # Default is False (NOT to preserve this data)
        #
        # This is handy for Forensic Investigators, Incident Management and Evidence requirements
        self.preserve_for_forensic_evidence = False
        # Clone VM Directory for when above question is True
        self.preserve_forensic_clone_directory = r'I:\Virtual Machines\Clones'

        # Your Stuff
        # Your Git repo local folder location inside the guest
        self.my_git_directory = r'/home/butchy/InternalGit'
        # List of your Git Repos to be cloned into my_git_directory
        # for private repos you will need to include a username and password in the URL
        # example: https://username:password@github.com/username/repository.git
        self.my_git_repos = {r'GoldenSnapshoter': r'https://github.com/pwnageByButchy/GoldenSnapshoter.git'}

        # Third party Git Repo local folder location inside the guest
        self.external_git_directory = r'/home/butchy/ExternalGit'
        # List of Third Party Git Repos to be cloned into external_git_directory
        self.external_git_repos = {r'USB-Rubber-Ducky': r'https://github.com/hak5darren/USB-Rubber-Ducky.git',
                                   r'Bash-Bunny-Payloads': r'https://github.com/hak5darren/bashbunny-payloads.git',
                                   r'Packet-Squirrel-Payloads': r'https://github.com/hak5darren/packetsquirrel-payloads.git',
                                   r'StegCracker': r'https://github.com/Paradoxis/StegCracker.git'}
