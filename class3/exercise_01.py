#!/usr/bin/env python
"""
Using SNMPv3 create a script that detects router configuration changes.

If the running configuration has changed, then send an email notification to
yourself identifying the router that changed and the time that it changed.

Note, the running configuration of pynet-rtr2 is changing every 15 minutes
(roughly at 0, 15, 30, and 45 minutes after the hour).  This will allow you to
test your script in the lab environment

# HERE are some interesting OIDs from Cisco Devices

# Uptime when running config last changed
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'   

# Uptime when running config last saved (note any 'write' constitutes a save)
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'

# Uptime when startup config last saved
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'

To do this, we'll compare old values retrieved by OIDs against new values

"""

import yaml
import json
import snmp_helper
import time
import email_helper

SCAN_TIME = 60 #secs
DEVS_TO_MONITOR = ['x.x.x.x']
USER_NAME = 'USERNAME'
AUTH_KEY = 'AUTHKEY1'
ENCRY_KEY = 'AUTHKEY2'
SNMP_PORT = 161
CONTROL_FILE = 'snmp_readings.yml'

def write_yaml(f_name, content):
    with open(f_name, "w") as f:
        f.write(yaml.dump(content, default_flow_style=False))

def read_yaml(f_name):
    with open(f_name, "r") as f:
        yaml_content = yaml.load(f)
    return yaml_content

def compare(old_values, new_values):
    # Sample values to compare
    # [('ccmHistoryRunningLastChanged', '356898449'),
    # ('ccmHistoryRunningLastSaved', '356412236'),
    #  ('ccmHistoryStartupLastChanged', '354047837')]

    # ccmHistoryRunningLastChanged values
    RLC_old = old_values[0][1]
    RLC_new = new_values[0][1]
    # ccmHistoryRunningLastSaved values
    RLS_old = old_values[1][1]
    RLS_new = new_values[1][1]
    # ccmHistoryStartupLastChanged values
    SLC_old = old_values[2][1]
    SLC_new = new_values[2][1]

    uptime = int(new_values[3][1])/100

    if((RLC_new > RLC_old) and (RLS_new == RLS_old) and (SLC_new == SLC_old)):
        ret = 'Reboot or runn config was modified at {} secs'.format(uptime)
    elif((RLC_new == RLC_old) and (RLS_new > RLS_old) and (SLC_new > SLC_old)
          and (RLS_new == SLC_new)):
        ret = 'write memory has been issued at {} secs'.format(uptime)
    elif((RLC_new == RLC_old) and (RLS_new > RLS_old) and (SLC_new == SLC_old)):
        ret = 'sh runn was issued causing write terminal at {} secs'.format(uptime)
    else:
        # No change in configuration
        ret = False
    return ret

def send_email_change(has_changed):
    recipient = 'rcv_example@example.com'
    subject = 'Device Configuration Change'
    message = has_changed + "\n Regards, \nAngel"
    sender = 'sndr_example@example.com'
    email_helper.send_mail(recipient, subject, message, sender)

class SNMP_v3_DEVICE(object):
    def __init__(self, ip_address, username, auth_k, encry_k, snmp_port):
        self.ip_address = ip_address
        self.username = username
        self.auth_k = auth_k
        self.encry_k = encry_k
        self.snmp_port = snmp_port
        self.snmp_oids = (
                          # format here is, Description of OID, OID, Boolean for is this value
                          # a counter?
            ('ccmHistoryRunningLastChanged', '1.3.6.1.4.1.9.9.43.1.1.1.0', True),
            ('ccmHistoryRunningLastSaved', '1.3.6.1.4.1.9.9.43.1.1.2.0', True),
            ('ccmHistoryStartupLastChanged', '1.3.6.1.4.1.9.9.43.1.1.3.0', True),
            ('sysUptime', '1.3.6.1.2.1.1.3.0', True))

    def read_all_oids(self):
        self.oid_values = []
        self.snmp_user = (self.username, self.auth_k, self.encry_k)
        self.dev_tuple = (self.ip_address, self.snmp_port)
        for desc, an_oid, is_count in self.snmp_oids:
            self.snmp_data = snmp_helper.snmp_get_oid_v3(self.dev_tuple,
                                                    self.snmp_user, oid=an_oid)
            self.output = snmp_helper.snmp_extract(self.snmp_data)
            self.oid_values.append((desc, self.output))
        return self.oid_values

def main():
    for dev in DEVS_TO_MONITOR:
        snmpv3_dev = SNMP_v3_DEVICE(dev, USER_NAME, AUTH_KEY, ENCRY_KEY, SNMP_PORT)
        out = snmpv3_dev.read_all_oids()
        # Writing output to YAML file
        f_name = dev + '_' + CONTROL_FILE
        write_yaml(f_name, out)
        print 'YAML file: {} has been created' .format(f_name)

        while True:
            # We'll sleep for SCAN_TIME secs before reading again
            # and comparing values
            time.sleep(SCAN_TIME)
            # Time to wake up, read new values and make comparisons
            old_values = read_yaml(f_name)

            # Read again ( new values)
            new_values = snmpv3_dev.read_all_oids()
            #print old_values
            #print new_values
            # Writing output to YAML file
            f_name = dev + '_' + CONTROL_FILE
            write_yaml(f_name, new_values)
            print 'YAML file: {} has been created'.format(f_name)

            has_changed = compare(old_values, new_values)
            if has_changed != False:
                send_email_change(has_changed)

if __name__ == '__main__':
    main()
