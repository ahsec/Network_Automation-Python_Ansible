#!/usr/bin/env python
"""
script that connects using telnet to the pynet-rtr1 router. Execute the 
'show ip int brief' command on the router and return the output
"""

import time
import exercise_03

def main():
    username = 'USERNAME'
    password = 'PASSWD'
    ip_address = 'x.x.x.x'

    dev = exercise_03.NetDevice(ip_address, username, password)

    time.sleep(1)
    output = dev.login()
    print output

    time.sleep(1)
    dev.send_command("sh ip int brief")

    dev.close()

if __name__ == '__main__':
    main()

