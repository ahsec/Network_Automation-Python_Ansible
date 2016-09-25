#!/usr/bin/env python
'''
Repeat exercise #6 except use processes.

Optional bonus question--use a queue to get the output data back from the child
processes in question #7. Print this output data to the screen in the main process.
'''
from datetime import datetime
from multiprocessing import Process, Queue
import django
from net_system.models import NetworkDevice
import netmiko

COMMAND = 'show version'

def execute_command(cmd, dev, q):
    '''
    Will execute a command using Netmiko's send_command_expect() method.
    Receives: command to execute and device to execute it on.
    Writes the output to a Queue (FIFO structure)
    '''
    try:
        output_dict = {}
        creds = dev.credentials
        connection = netmiko.ConnectHandler(device_type=dev.device_type,
                                            ip=dev.ip_address,
                                            username=creds.username,
                                            password=creds.password,
                                            port=dev.port, secret='')
        # Create and write output to the Queue
        out = connection.send_command_expect(cmd)
        output = "{} \n {} \n {}".format("#" * 80, out, "#" * 80)
        output_dict[dev.device_name] = output
        q.put(output_dict)

    except netmiko.ssh_exception.NetMikoAuthenticationException as e:
        print 'Authentication error: {}'.format(e)

def main():
    '''
    Use Netmiko to connect to each of the devices in the database. Execute 'show version' on each
    device.
    Calculate the amount of time required to do this.
    '''
    django.setup()
    start_time = datetime.now()
    q = Queue(maxsize=20)

    devs = NetworkDevice.objects.all()
    procs = []
    for dev in devs:
        my_proc = Process(target=execute_command, args=(COMMAND, dev, q))
        my_proc.start()
        procs.append(my_proc)

    for proc in procs:
        proc.join()

    # Will read the content of the Queue and print out the output to the screen
    # We're not printing out the output until the enD ! This makes the exit more ordered and pretty.
    while not q.empty():
        my_dict = q.get()
        for k, v in my_dict.iteritems():
            print k     # Dictionary key
            print v     # Dictionary Value

    total_time = datetime.now() - start_time
    print 'Total time is {}'.format(total_time)

if __name__ == '__main__':
    main()
