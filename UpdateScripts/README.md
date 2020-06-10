
The application will create separate UpdateScripts for each virtual machine based on the 2 master scripts

If you use the Git script you will need to copy and paste it into the individual UpdateScripts and next run of the Snapshoter will migrate those changes into your VM.

Inside the UpdateLinux.py we have catered for a few different distributions if yours in not list let us know and we can add support for it. If you already know the package manager and it is one of the 4 supplied. There are some arrays at the end of the script add your distro to the appropriate array.

```
apt = ["Kali", "Ubuntu", "Debian"]
yum = ["RHEL", "CentOS", "Fedora"]
pacman = ["blackarch", "arch"]
parrot = ["Parrot"]
```
