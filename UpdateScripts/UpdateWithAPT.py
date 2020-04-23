
import os
import subprocess


# Put your code between here

# and here


get_guest_os = 'cat /etc/*release | grep ^"NAME=" | cut -d "=" -f2 | tr \'"\' \' \'| cut -d " " -f2'
result = subprocess.check_output(get_guest_os, shell=True)
result = result.replace("b'", "")
result = result.replace("\\n'", "")


def switch(value):
    return {
        "Kali": 1,
        "Ubuntu": 1,
        "Parrot": 1,
        "RHEL": 2,
        "CentOS": 2,
        "Fedora": 2,
        "Arch": 3,
        "blackarch": 3,
    }.get(value, 42)


def apt_update():
    os.system('apt-get update -y && apt-get upgrade -y')
    os.system('apt-get autoclean -y && apt-get clean -y')
    os.system('apt-get autoremove -y')
    os.system('poweroff')


def yum_update():
    os.system('yum check-update && yum -y update')
    os.system('yum -y autoremove')
    os.system('poweroff')


def pacman_update():
    # Make sure the network interface is up
    os.system('systemctl restart NetworkManager')
    os.system('pacman -Syu --noconfirm')
    os.system('poweroff')


if switch(result) == 1:
    apt_update()
elif switch(result) == 2:
    yum_update()
elif switch(result) == 3:
    pacman_update()
else:
    print("Unable to update system")
