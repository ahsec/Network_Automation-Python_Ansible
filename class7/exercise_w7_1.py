#!/usr/bin/env python
'''
 Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the
 'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields for
each of the interfaces on the switch.  Accomplish this using Arista's pyeapi.
'''
import pyeapi

def get_out(dev_conn, command):
    '''
    Runs a command in enable mode using the earista eAPI and returns the data
    relavant to the switch output.
    Requires a pyeapi connection already established
    '''
    conn = dev_conn.enable(command)
    # Relvant output is on index 0 of the output list
    out = conn[0]['result']
    return out

def main():
    '''
    Establishes connection and unpacks output to retrieve relevant in and out
    Octects data
    '''
    # Establish connection to device defined in the .eapi.conf file
    pynet_sw2 = pyeapi.connect_to("pynet-sw2")

    # Run commands in enable mode (Returns a list) and return relevant content
    out = get_out(pynet_sw2, 'sh interfaces')
    out = out['interfaces']
    # Will start unpacking the relevant values per each interface found in the
    # out interfaces
    for interface, values in out.items():
        in_oct = values.get('interfaceCounters', {}).get('inOctets')
        out_oct = values.get('interfaceCounters', {}).get('outOctets')
        print "Interface: {} - In Octects: {} - Out Octects: {} ".format(interface,
                                                                         in_oct,
                                                                         out_oct)
if __name__ == '__main__':
    main()
