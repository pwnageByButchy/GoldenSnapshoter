# GoldenSnapshoter
A Python3 script to create and maintain a “Golden Image” of VMs in VMWare Workstation (for the moment) on either a Windows or Linux host...

This saves deleting the VM, downloading the VM and then updating it, download all the Git repos, download your git repos everytime time you mess up a VM or in the case of Pentesters when you start work on a new job start fresh but updated!

With GoldenSnapshoter your VMs, is reset to your current golden image, the guest OS is updated, your's and third party Git repos are updated/downloaded and then that is saved as your new "Golden Image".

WARNING!!! This removes any unwanted (or possiblely wanted) data from the VM, be sure to move any wanted data off the VM prior to running the Script WARNING!!!

### The Initial Setup ###
#### Physical Host Configuration ####
1. Install Python3
2. Install VMWare Workstation
3. Add path to vmrun to your host's path
4. Implement VirtualMachines Folder Structure
5. Modify settings in settings.py to suit your environment

a folder structure example: \VirtualMachines\Clients\Windows10 or C:\VirtualMachines\Clients\Windows10
![VirtualMachines Folder Structure](assets/images/VirtualMachines.png "VirtualMachines Folders")

If you dont want all of your VMs snapshotted put them in a good folder structure. I usually only want to snapshot my "Clients" but not my CTFs.<br />

#### Create Your VM(s) ####
(Remember there are ways to script an initial build of a VM... go have a look)
1. Create your VM - Download and Create your Guest VM with the OS of your choice
2. Install any additional items you want included in your Image - Favourite Browser, Additional Tools, Password Manager, Git Repos
3. Configure your VM
4. Shutdown your VM and Create a snapshot called "BaseImage" (or what you will be calling your base image...be consistent with the name for all the VMs you want to snapshot)

### Usage ###
1. Configure all the variables in settings.py to match your environment
2. Open powershell and run python ./GoldenSnapshoter.py
