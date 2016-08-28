#!/usr/bin/env python
'''
Use Netmiko to change the logging buffer size (logging buffered <size>) and to disable console 
logging (no logging console) from a file on both pynet-rtr1 and pynet-rtr2 
(see 'Errata and Other Info, item #4).

*Netmiko supports a method (send_config_from_file) that allows you to execute configuration 
commands directly from a file. For example, if you had a set of commands in a file called 
'config_file.txt', then you could execute those commands via the SSH channel as follows:
 
         net_connect.send_config_from_file(config_file='config_file.txt')
'''
from netmiko import ConnectHandler
from getpass import getpass

DEVICES = ['184.105.247.70', '184.105.247.71']
CONF_COMMANDS_FILE = 'exercise_08_conf_commands'
DEV_TYPE = ['cisco_ios', 'cisco_ios']

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

            print '>>>>>>>>>>>>>>>>> DEVICE: {} <<<<<<<<<<<<<<<<<<'.format(DEVICES[i])
            # Initiating netmiko connection    
            net_connect = ConnectHandler(**net_dev)
            resp = net_connect.find_prompt()
            print resp
        
            # Deploying config commands from file
            resp = net_connect.send_config_from_file(config_file=CONF_COMMANDS_FILE)
            print resp

        except Exception as e:
            print e
            exit(0)

if __name__ == '__main__':
    main()

