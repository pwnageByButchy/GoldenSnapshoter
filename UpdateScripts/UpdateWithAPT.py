import os
import time
import subprocess


# Put your code between here

# and here


get_guest_os = 'cat /etc/*release | grep ^"NAME=" | cut -d "=" -f2 | tr \'"\' \' \'| cut -d " " -f2'
result = subprocess.check_output(get_guest_os, shell=True)
result = result.decode("utf-8")
result = result.strip()


def switch(value):
    if value in apt:
        apt_update()
    elif value in yum:
        yum_update()
    elif value in pacman:
        pacman_update()
    else:
        print("This value is not accounted for " + value)
        print("Unable to update system")
 


def apt_update():
    os.system('apt-get update -y && apt-get upgrade -y')
    os.system('apt-get autoclean -y && apt-get clean -y')
    os.system('apt-get autoremove -y')
    time.sleep(10)
    os.system('poweroff')


def yum_update():
    os.system('yum check-update && yum -y update')
    os.system('yum -y autoremove')
    time.sleep(10)
    os.system('poweroff')


def pacman_update():
    # Make sure the network interface is up
    os.system('systemctl restart NetworkManager')
    os.system('pacman -Syu --noconfirm')
    time.sleep(10)
    os.system('poweroff')

apt = ["Kali", "Ubuntu", "Parrot", "Debian"]
yum = ["RHEL", "CentOS", "Fedora"]
pacman = ["blackarch", "arch"]


switch(result)

