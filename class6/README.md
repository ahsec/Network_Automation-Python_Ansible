# Class 6 Exercises.

#### * exercise_1.py *
Using Ansible, configure three VLANs on the Arista switch specifying both the VLAN IDs and the VLAN names.  For the VLAN IDs randomly pick three numbers between 100 and 999.

#### * exercise_2.py *
Use Ansible to configure your 'primary Ethernet interface' as follows:
```
interface description: *** IN USE ***
switchport mode:       access
VLAN:                  <one of the VLANs created in exercise1>
```
#### * exercise_3.py *
Use Ansible to configure your 'primary Ethernet interface' as follows:
```
switchport mode:       trunk
trunk native VLAN:     VLAN1
trunk allowed VLANs:   <the three VLANs created in exercise1>
```
#### * exercise_4.py *
Use Ansible to restore your 'primary Ethernet interface' back to the following state (or your secondary interface depending on which one you used):
```
description:          <none>
switchport mode:      access
access VLAN:          1
trunk allowed VLANs:  all
```
Also use Ansible to remove the three VLANs that you configured.

#### * exercise_5.py *
Use the cisco_file_transfer.py module to transfer a small file to the Cisco pynet-rtr1 router.
