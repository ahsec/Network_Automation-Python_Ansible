#!/usr/bin/env python
"""
1. Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2. 
"""

import paramiko
from getpass import getpass
import time

NET_DEVS = ['184.105.247.71'] 
COMMANDS_TO_RUN = ['show version']

class ParamikoDev(object):
    def __init__(self, ip_address, usern, passwd, portn = 22):
        self.ip_address = ip_address
        self.usern = usern
        self.passwd = passwd
        self.portn = portn
        
        try: 
            ssh_pre = paramiko.SSHClient()
            ssh_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_pre.connect(self.ip_address, username=self.usern, password=self.passwd, port=self.portn)
            self.ssh = ssh_pre.invoke_shell()
            self.ssh.keep_this = ssh_pre
            resp = self.ssh.recv(9999)
            self.ssh.send('terminal length 0' + '\n')
            time.sleep(1)
        except Exception as e:
            print e
            exit(0)

    def exec_command(self, command):
        try:
            self.ssh.send(command + '\n')
            time.sleep(1)
            resp = self.ssh.recv(999999)
            return resp
        except Exception as e:
            print e
            exit(0)

def main():
    print 'Username:',
    usern = raw_input()
    passwd = getpass()

    for dev in NET_DEVS:
        p_dev = ParamikoDev(dev, usern, passwd)
        print '\n ########### Device: {} ###########\n'.format(dev)
        for command in COMMANDS_TO_RUN:
            resp = p_dev.exec_command(command)
            print resp
            
if __name__ == '__main__':
    main()


