#!usr/bin/env python3

import subprocess
import time
from pathlib import Path

BLOCK_DEVICES = [Path("/dev/sda1"),
                 Path("/dev/sdb1"),
                 Path("/dev/sdc1"),
                 Path("/dev/sdd1"),
                 Path("/dev/sde1") ]
MOUNT_POINT = Path("/media/usb")
detect_flag = 0

#check for mount point
if(MOUNT_POINT.is_dir()):
        pass
else:
        os.mkdir('/media/usb')

#check if the pendrive is plugged in
for  BLOCK_DEVICE in BLOCK_DEVICES:
        if(BLOCK_DEVICE.exists()):
                DEVICE = BLOCK_DEVICE

#to mount and print the status
if(DEVICE.exists() and not MOUNT_POINT.is_mount()):
        MOUNT_COMMAND = ["sudo","mount",DEVICE,MOUNT_POINT]
        subprocess.check_call(MOUNT_COMMAND)
        detect_flag = 1
        print("Detected")
elif (DEVICE.exists() and MOUNT_POINT.is_mount()):
        print("Detected")
        detect_flag = 1
else:
        print("Not detected")

#copying the contents of pendrive

#unmount the pendrive
print("Press 1 to remove the pendrive or press any key not to proceed")
var = input()
UNMOUNT_COMMAND = ["sudo","umount",MOUNT_POINT]
if(var == '1'):
        subprocess.check_call(UNMOUNT_COMMAND)

