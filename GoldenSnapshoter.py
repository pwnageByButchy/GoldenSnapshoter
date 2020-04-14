#!/usr/bin/env python3

from VMWare import *
from setup import *


def main():
    virtualMachines = []
    vmWareType = ""
    guestUser = input()
    guestpasswd = input()
    determineEnvironment()
    findVMs(vmDirectory, extension)
    for vm in virtualMachines:
        guestOS = determineGuestOS(vm)
        VMWare.snapshotProcess(vm, guestUser, guestPassword, guestOS)
