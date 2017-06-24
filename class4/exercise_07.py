#!/usr/bin/env python
'''
Use Netmiko to change the logging buffer size (logging buffered <size>) on
pynet-rtr2
'''
from netmiko import ConnectHandler
from getpass import getpass

DEVICES = ['184.105.247.71']
CONF_COMMANDS = ['logging buffered 64001']
DEV_TYPE = ['cisco_ios']

def main():
    print 'Username:',
    usern = raw_input()
    passwd = getpass()

    for i in range(len(DEVICES)):
        try:
            net_dev = {
                        'device_type':DEV_TYPE[i],
                        'ip':DEVICES[i],
                        'username':usern,
                        'password':passwd
                    }

            print '>>>>>>>>>>>>> DEVICE: {} <<<<<<<<<<<<<<'.format(DEVICES[i])
            # Initiating netmiko connection
            net_connect = ConnectHandler(**net_dev)
            resp = net_connect.find_prompt()
            print resp

            # Entering config mode, deploying commands and exiting config mode
            resp = net_connect.send_config_set(CONF_COMMANDS)
            print resp

        except Exception as e:
            print e
            exit(0)

if __name__ == '__main__':
    main()
