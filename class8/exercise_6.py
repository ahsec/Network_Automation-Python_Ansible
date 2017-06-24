#!/usr/bin/env python
'''
Use threads and Netmiko to execute 'show version' on each device in the database.
Calculate the amount of time required to do this. What is the difference in time
between executing 'show version' sequentially versus using threads?

There's a 30 secs difference between threading and serialized execution
'''
from datetime import datetime
import threading
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
        print
        print '#' * 80
        print connection.send_command(cmd)
        print '#' * 80
        print
    except netmiko.ssh_exception.NetMikoAuthenticationException as e:
        print 'Authentication error: {}'.format(e)

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
        my_thread = threading.Thread(target=execute_command, args=(COMMAND,
                                                                   dev,))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            some_thread.join()

    total_time = datetime.now() - start_time
    print 'Total time is {}'.format(total_time)

if __name__ == '__main__':
    main()
