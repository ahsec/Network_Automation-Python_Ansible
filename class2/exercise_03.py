#!/usr/bin/env python 
"""
(optional - challenge question)
Convert the code that Kirk B, wrote to a class-based solution (i.e. convert over from 
functions to a class with methods).
"""

import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

class NetDevice():
    def __init__(self, ip_address, username, password):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.connect()    
    
    def connect(self):
        # exception handling for telnet connections
        try:
            self.conn = telnetlib.Telnet(self.ip_address, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")

    def login(self):
        # read until will stop when it finds the specified pattern on the output or when the 
        # connection timesout TELNET_TIMEOUT
        self.output = self.conn.read_until("sername:", TELNET_TIMEOUT)
        # conn.write will send a command through the connection
        self.conn.write(self.username + '\n')
        self.output += self.conn.read_until("ssword:", TELNET_TIMEOUT)
        self.conn.write(self.password + '\n')
        time.sleep(1)
        self.output = self.conn.read_very_eager()
        return self.output
    def close(self):
        self.conn.close()

    def send_command(self, cmd):
        self.cmd = cmd
        # rstrip will strip trailing whitespaces
        self.cmd = self.cmd.rstrip()
        self.conn.write(cmd + '\n')
        time.sleep(1)
        # red_very_eager() will read as much output as possible 
        print self.conn.read_very_eager()

def main():
    ip_addr = "184.105.247.70"
    username = "pyclass"
    password = "88newclass"

    net_dev1 = NetDevice(ip_addr, username, password)

    time.sleep(1)
    output = net_dev1.login()
    print output
    time.sleep(1)

    net_dev1.send_command("sh ip int brief")

    net_dev1.close()

if __name__ == '__main__':
    main()


