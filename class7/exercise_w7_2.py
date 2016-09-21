#!/usr/bin/env python
'''
Using Arista's pyeapi, create a script that allows you to add a VLAN (both the VLAN ID
and the VLAN name).
Your script should first check that the VLAN ID is available and only add the VLAN if
it doesn't already exist.  Use VLAN IDs between 100 and 999.  You should be able to
call the script from the command line as follows:

   python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.

   python eapi_vlan.py --remove 100          # remove VLAN100
'''
import argparse
import pyeapi

ARISTA_DEV = 'pynet-sw2'

def connect_arista(dev_name):
    ''' Performs a connection through the pyeapi API.
    Returns necessary object to execute commands'''
    dev = pyeapi.connect_to(dev_name)
    return dev

def verify_vlan(dev, identifier, to_search):
    ''' Verifies that a vlan exists on an Arista switch
    Uses the vlan name and command sh vlan name <name>  to achieve verification
    Receives dev object (necessary to execute commands) identifier (vlan name or vlan id),
    and the vlan name or id number to serach for'''

    if identifier == 'name':
        try:
            # Setting return vlaue to True. This will change if command is unsucessful
            ret = True
            command = 'sh vlan name ' + to_search
            dev.enable(command)
        except pyeapi.eapilib.CommandError as e:
            ret = False

    elif identifier == 'id':
        try:
            # Setting return vlaue to True. This will change if command is unsucessful
            ret = True
            command = 'sh vlan id ' + str(to_search)
            dev.enable(command)
        except pyeapi.eapilib.CommandError as e:
            ret = False
    return ret

def main():
    parser = argparse.ArgumentParser(description='Adds or removes vlans on an Arista switch.'+\
                                    'pyeapi required')
    group = parser.add_mutually_exclusive_group()
    # Option to add a new vlan
    group.add_argument("--name", "-n", help='Vlan name and id to add. i.e. --name "blue 100".'+\
                        '\nNote the double quotes around the argument')
    # Option to remove a VLAN
    group.add_argument("--remove", "-r", type=int, help='Vlan id to remove. i.e. --remove 100')
    args = parser.parse_args()

    # Processing the received arguments
    if args.name:
        dev = connect_arista(ARISTA_DEV)
        # Verify that vlan id and name doesn't currently exist on switch then add vlan
        vlan_name, vlan_id = args.name.split()
        # Verify VLAN exists by ID and NAME
        ret_name = verify_vlan(dev, 'name', vlan_name)
        ret_id = verify_vlan(dev, 'id', vlan_id)

        if (ret_name is True) or (ret_id is True):
            # If both name and vlan ID exists, Do nothing
            print 'Vlan ID {} and/or name {} already exists. \nNothing to do.'.format(vlan_id,
                                                                                      vlan_name)
        else:
            # ELSE cretae new VLAN
            print "VLAN id {} and name {} doesn't exist... creating...".format(vlan_id, vlan_name)
            c_vlan_id = 'vlan ' + vlan_id
            c_vlan_name = 'name ' + vlan_name
            command = [c_vlan_id, c_vlan_name]
            dev.config(command)
            dev.enable("write memory")
            print 'Vlan {} {} added to the {} device'.format(vlan_id, vlan_name, ARISTA_DEV)

    elif args.remove:
        dev = connect_arista(ARISTA_DEV)
        vlan_id = args.remove
        # Verify that vlan id exists before attempting to remove vlan
        ret_id = verify_vlan(dev, 'id', vlan_id)
        if ret_id is True:
        # Just found out of the vlans API and verification functionality ...
            vlans = dev.api('vlans')
            vlans.delete(vlan_id)
            dev.enable("write memory")
            print 'Vlan ID: {} has been removed from: {}'.format(vlan_id, ARISTA_DEV)
        else:
            print "Vlan ID: {} doesn't exist on device: {}\nNothing to do.".format(vlan_id,
                                                                                   ARISTA_DEV)

if __name__ == '__main__':
    main()
