#!/usr/bin/env python
"""
Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2.
This will require that you enter into configuration mode.
"""
import exercise_01
from getpass import getpass

NET_DEVS = ['184.105.247.71']
COMMANDS_TO_RUN = ['conf t', 'logging buffered 80000', 'exit',
                   'sh runn | inc logging']

def main():
    print 'Username:',
    usern = raw_input()
    passwd = getpass()

    for dev in NET_DEVS:
        p_dev = exercise_01.ParamikoDev(dev, usern, passwd)
        print '\n ########### Device: {} ###########\n'.format(dev)
        for command in COMMANDS_TO_RUN:
            resp = p_dev.exec_command(command)
            print resp

if __name__ == '__main__':
    main()
