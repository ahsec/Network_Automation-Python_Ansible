#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

'''
This script will parse a Cisco configuration file, find all the lines that
begin with "crypto map CRYPTO", for each crypto map will print out its
children.
'''

CISCO_FILENAME = "cisco_ipsec.txt"

def print_objects_and_children(crypto_objs):
    for obj in crypto_objs:
        print "[-]"
        print obj.text
        for child in obj.all_children:
            print child.text

def main():
    cisco_cfg = CiscoConfParse(CISCO_FILENAME)
    crypto_objs = cisco_cfg.find_objects(r"crypto map CRYPTO")
    print 'All crypto objects and their respective children:'
    print_objects_and_children(crypto_objs)

if __name__ == '__main__':
    main()
