#!/usr/bin/env python
'''
Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2. 
Verify this change by examining the output of 'show run'.
'''
import exercise_03
import pexpect
import sys
from getpass import getpass

DEVICES = ['184.105.247.71']
PORT = 22
COMMANDS = ['conf t', 'logging buffered 80000', 'exit', 'sh runn | inc logging']
PROMPT = '#'

def main():
    print 'Username:',
    usern = raw_input()
    passwd = getpass()

    for dev in DEVICES:
        print '>>>>>>>>>>>>>>>>> DEVICE: {} <<<<<<<<<<<<<<<<<<<'.format(dev)
        pex_dev = exercise_03.PexpectDev(dev, usern, passwd)
        for command in COMMANDS:
            print '-----------------------------------------------------------'
            resp = pex_dev.exec_comm(command)
            print PROMPT + resp

if __name__ == '__main__':
    main()

