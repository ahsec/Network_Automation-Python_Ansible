#!/usr/bin/env python
'''
Use Netmiko to enter into configuration mode on pynet-rtr2.
Also use Netmiko to verify your state (i.e. that you are currently in
configuration mode).
'''
from netmiko import ConnectHandler
from getpass import getpass

DEVICES = ['184.105.247.71']
COMMANDS = []
DEV_TYPE = 'cisco_ios'

def main():
    print 'Username:',
    usern = raw_input()
    passwd = getpass()

    for dev in DEVICES:
        net_dev = {
            'device_type':DEV_TYPE,
            'ip':dev,
            'username':usern,
            'password':passwd
            }
        # Initiating netmiko connection
        net_connect = ConnectHandler(**net_dev)
        resp = net_connect.find_prompt()
        print resp
        # Entering config mode
        net_connect.config_mode()
        # Verifying we're in config mode
        resp = net_connect.check_config_mode()
        print 'Entered Config mode? {}'.format(resp)
        # Exiting config mode
        net_connect.exit_config_mode()

if __name__ == '__main__':
    main()
