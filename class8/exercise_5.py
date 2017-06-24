#!/usr/bin/env python
'''
Use Netmiko to connect to each of the devices in the database. Execute
'show version' on each device.
Calculate the amount of time required to do this.

* Your results will be more reliable if you use Netmiko's send_command_expect()
method.
There is an issue with the Arista vEOS switches and Netmiko's send_command()
method.
'''
from datetime import datetime
import django
from net_system.models import NetworkDevice
import netmiko

COMMAND = 'show version'

def execute_command(cmd, dev):
    '''
    Will execute a command using Netmiko's send_command_expect() method.
    Receives: command to execute and device to execute it on.
    Returns the output
    '''
    try:
        creds = dev.credentials
        connection = netmiko.ConnectHandler(device_type=dev.device_type,
                                            ip=dev.ip_address,
                                            username=creds.username,
                                            password=creds.password,
                                            port=dev.port, secret='')

        out = connection.send_command_expect(cmd)
    except netmiko.ssh_exception.NetMikoAuthenticationException as e:
        print 'Authentication error: {}'.format(e)
        out = ''
    return out

def main():
    '''
    Use Netmiko to connect to each of the devices in the database. Execute
    'show version' on each device.
    Calculate the amount of time required to do this.
    '''
    django.setup()
    start_time = datetime.now()

    devs = NetworkDevice.objects.all()
    for dev in devs:
        out = execute_command(COMMAND, dev)
        print "{} {} \n {} \n {} {}".format(">"*17, "<"*17, out, ">"*17, "<"*17)

    total_time = datetime.now() - start_time
    print 'Total time is {}'.format(total_time)

if __name__ == '__main__':
    main()
