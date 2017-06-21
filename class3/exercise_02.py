#!/usr/bin/env python
"""
Using SNMPv3 create two SVG image files.  

The first image file should graph the input and output octets on interface FA4 on pynet-rtr1 every 
five minutes for an hour.  Use the pygal library to create the SVG graph file. Note, you should be 
doing a subtraction here (i.e. the input/output octets transmitted during this five minute interval)

The second SVG graph file should be the same as the first except graph the unicast packets 
received and transmitted.

The relevant OIDs are as follows:

('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5')
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5')
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5')
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
"""
import exercise_01
import pygal
import time
import pygal

USER_NAME = 'USERNAME'
AUTH_KEY = 'AUTH_PASS1'
ENCRY_KEY = 'AUTH_PASS2'
SNMP_PORT = 161
DEV_TO_MONITOR = 'x.x.x.x'
POLL_TIME = 300 #secs or 5 min 

def compare_in_out(initial_values, new_values):
    ifInOctets_fa4_init = initial_values[1][1]
    ifInOctets_fa4_new = new_values[1][1]
    ifInUcastPkts_fa4_init = initial_values[2][1]
    ifInUcastPkts_fa4_new = new_values[2][1]
    ifOutOctets_fa4_init = initial_values[3][1]
    ifOutOctets_fa4_new = new_values[3][1]
    ifOutUcastPkts_fa4_init = initial_values[4][1]
    ifOutUcastPkts_fa4_new = new_values[4][1]

    ifInOctets_diff = int(ifInOctets_fa4_new) - int (ifInOctets_fa4_init)
    ifInUcastPkts_diff = int(ifInUcastPkts_fa4_new) - int(ifInUcastPkts_fa4_init)
    ifOutOctets_diff = int(ifOutOctets_fa4_new) - int(ifOutOctets_fa4_init)
    ifOutUcastPkts_diff = int(ifOutUcastPkts_fa4_new) - int(ifOutUcastPkts_fa4_init)

    return (ifInOctets_diff, ifOutOctets_diff, ifInUcastPkts_diff, ifOutUcastPkts_diff)

def create_graph_file(f_name, tittle, label1, line1, label2, line2, timeline):
    line_chart = pygal.Line()
    line_chart.x_labels = timeline
    line_chart.title = tittle 
    line_chart.add(label1, line1)
    line_chart.add(label2, line2)
    line_chart.render_to_file(f_name)
    return True

def main():
    snmp_dev = exercise_01.SNMP_v3_DEVICE(DEV_TO_MONITOR, USER_NAME, AUTH_KEY, ENCRY_KEY, SNMP_PORT)
    snmp_dev.snmp_oids = (
                            ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', False),
                            ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
                            ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
                            ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
                            ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5', True)
                        )
    inOct = []
    outOct = []
    inUnic = []
    outUnic = []
    timeline = range(5,65,5)
    # Initial reading
    initial_values = snmp_dev.read_all_oids()
    for minute in timeline:
        time.sleep(POLL_TIME)
        new_values = snmp_dev.read_all_oids()
        difference = compare_in_out(initial_values, new_values)
        inOct.append(difference[0])
        outOct.append(difference[1])
        inUnic.append(difference[2])
        outUnic.append(difference[3])
        initial_values = new_values
        
    graph1 = create_graph_file("InOutOctect.svg", "Input/Output Octects", "Input Octects", inOct, 
                                "Output Octects", outOct, timeline)
    graph2 = create_graph_file("InOutUnicast.svg", "Input/Output Unicast", "Input Unicast packets",
                                inUnic, "Output Unicast Packets", outUnic, timeline)

    if (graph1 == True) and (graph2 == True):
        print "Graphic files created on local directory"
    else:
        print "Error creating graphic files"

if __name__ == '__main__':
    main()


