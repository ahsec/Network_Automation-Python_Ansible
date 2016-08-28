#!/usr/bin/env python
"""
Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
"""
import pexpect
import sys
from getpass import getpass

DEVICES = ['184.105.247.71']
PORT = 22
COMMANDS = ['sh ip int brief']
PROMPT = '#'

class PexpectDev(object):
    def __init__(self, ip_addr, usern, passwd, port=22):
        try:
            self.ip_addr = ip_addr
            self.usern = usern
            self.passwd = passwd
            self.port = port
    
            self.ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(self.usern, self.ip_addr, self.port))
            self.ssh_conn.timeout = 3
            self.ssh_conn.expect('ssword:')
            self.ssh_conn.sendline(self.passwd)

            self.ssh_conn.expect(PROMPT)
            print self.ssh_conn.before
            print self.ssh_conn.after

            self.ssh_conn.sendline('terminal length 0')
            self.ssh_conn.expect(PROMPT)
            print self.ssh_conn.before
        except Exception as e:
            print e
            exit(0)

    def exec_comm(self, command):
        try:
            self.ssh_conn.sendline(command)
            self.ssh_conn.expect(PROMPT)
            return self.ssh_conn.before
        except Exception as e:
            print e

def main():
    print 'Username:',
    usern = raw_input()
    passwd = getpass()
    for dev in DEVICES:
        print '>>>>>>>>>>>>>>>>> DEVICE: {} <<<<<<<<<<<<<<<<<<<'.format(dev)
        pex_dev = PexpectDev(dev, usern, passwd)
        for command in COMMANDS:
            print '-----------------------------------------------------------'
            resp = pex_dev.exec_comm(command)
            print PROMPT + resp

if __name__ == '__main__':
    main()


