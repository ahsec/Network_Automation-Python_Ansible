#!/usr/bin/env python
'''
 Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx
'''
from netmiko import ConnectHandler
from getpass import getpass

DEVICES = ['184.105.247.70', '184.105.247.71', '184.105.247.76']
COMMANDS = ['show arp']
DEV_TYPE = ['cisco_ios', 'cisco_ios', 'juniper']


def main():
    print 'Username:',
    usern = raw_input()
    passwd = getpass()
    
    for i in range(len(DEVICES)):
        net_dev = {
            'device_type':DEV_TYPE[i],
            'ip':DEVICES[i],
            'username':usern,
            'password':passwd
            }
        print '\n>>>>>>>>>>>>>>>>>> DEVICE: {} <<<<<<<<<<<<<<<<<<<'.format(DEVICES[i])
        # Initiating netmiko connection    
        net_connect = ConnectHandler(**net_dev)
        resp = net_connect.find_prompt()
        print resp,
        for command in COMMANDS:
            # Sending command(s)
            print command
            resp = net_connect.send_command("show ip int brief")
            print resp

if __name__ == '__main__':
    main()

