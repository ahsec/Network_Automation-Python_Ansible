#!/usr/bin/env python
"""
script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out
both the MIB2 sysName and sysDescr.
"""

from snmp_helper import snmp_get_oid, snmp_extract

OID_TO_POLL = ['1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.1.0']
DEVS_TO_POLL = ['x.x.x.x', 'y.y.y.y']
COMMUNITY_STRING = 'not-public'
SNMP_PORT = 161

class SNMP_DEV():
    def __init__(self, ip_address, community, snmp_port):
        self.ip_address = ip_address
        self.community = community
        self.snmp_port = snmp_port

    def poll_print_oid(self, oid):
        # Combines both snmp_get_oid and snmp_extract into one class method
        self.oid = oid
        self.a_device = (self.ip_address, self.community, self.snmp_port)
        self.snmp_data = snmp_get_oid(self.a_device, self.oid)
        self.output = snmp_extract(self.snmp_data)
        return self.output

def main():
    for dev in DEVS_TO_POLL:
        print '\n\n[+] Polling device: {}' .format(dev)
        dev = SNMP_DEV(dev, COMMUNITY_STRING, SNMP_PORT)
        for oid in OID_TO_POLL:
            oid_value = dev.poll_print_oid(oid)
            print '   [-] OID: {}    Value: {} ' .format(oid, oid_value)

if __name__ == '__main__':
    main()
