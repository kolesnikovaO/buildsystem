#!/usr/bin/env python
import datetime
import os
import re


#
VMAJOR = ''
VMINOR = ''
VHFNUMBER = ''
VERSION_FILE = "../VersionStorage/vercontrol.h"
X_VER_STRING = ''
VSUBMINOR = ''

lines = ''
with open(VERSION_FILE,  encoding="utf8") as FILE:
    lines = FILE.readlines()
    print(lines)
    for line in lines:
        if "VMAJOR" in line:
            VMAJOR = line.split(' ')[-1].strip('\n')
        if "VMINOR" in line:
            VMINOR = line.split(' ')[-1].strip('\n')
        if "VHFNUMBER" in line:
            VHFNUMBER = line.split(' ')[-1].strip('\n')
        if "VSUBMINOR" in line:
            oldline = line
            newline = re.sub(r'[0-9]+$',
            lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}",
            line)
            print(newline)
            lines = [line.replace(oldline, newline) for line in lines]
            VSUBMINOR = newline.split(' ')[-1].strip('\n')
        if "X_VER_STRING" in line:
            oldline = line
            X_VER_STRING = VMAJOR + '.' + VMINOR + '.' + VSUBMINOR  + '.' +  VHFNUMBER + '\n'
            newline = line.replace(line.split(' ')[-1], X_VER_STRING )
            lines = [line.replace(oldline, newline) for line in lines]

    print(lines)

with open (VERSION_FILE, 'w') as FILE:
    FILE.writelines(lines)
