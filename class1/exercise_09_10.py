#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse
'''
This script will parse a Cisco Configuration file and print all the
crypto map entries that are using PFS group 2
'''

CISCO_FILENAME = 'cisco_ipsec.txt'

def main():
    cisco_cfg = CiscoConfParse(CISCO_FILENAME)

    print 'All crypto maps that use "pfs group2"'
    cisco_objs = cisco_cfg.find_objects_w_child(parentspec=r"crypto map CRYPTO", childspec=r"set pfs group2")
    for obj in cisco_objs:
        print "[-]"
        print obj.text
        for child in obj.all_children:
            print child.text

    print '\n\nAll crypto maps that are not using AES'
    cisco_objs = cisco_cfg.find_objects_wo_child(parentspec=r"crypto map CRYPTO", childspec=r"set transform-set AES-")
    for obj in cisco_objs:
        print "[-]"
        print obj.text
        for child in obj.all_children:
            print child.text


if __name__ == '__main__':
    main()
