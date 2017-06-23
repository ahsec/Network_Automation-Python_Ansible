# Class 3 Exercises.

#### * exercise_01.py *
Using SNMPv3 create a script that detects router configuration changes.

If the running configuration has changed, then send an email notification to
yourself identifying the router that changed and the time that it changed.

Note, the running configuration of pynet-rtr2 is changing every 15 minutes
(roughly at 0, 15, 30, and 45 minutes after the hour).  This will allow you to
test your script in the lab environment

Here are some interesting OIDs from Cisco Devices

* Uptime when running config last changed
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'   

* Uptime when running config last saved (note any 'write' constitutes a save)    
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'   

* Uptime when startup config last saved   
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'

To do this, we'll compare old values retrieved by OIDs against new values


#### * exercise_02.py *
Using SNMPv3 create two SVG image files.  

The first image file should graph the input and output octets on interface FA4
on pynet-rtr1 every five minutes for an hour.  Use the pygal library to create
the SVG graph file. Note, you should be doing a subtraction here (i.e. the
input/output octets transmitted during this five minute interval)

The second SVG graph file should be the same as the first except graph the
unicast packets received and transmitted.

The relevant OIDs are as follows:
* ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5')
* ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5')
* ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5')
* ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
* ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
