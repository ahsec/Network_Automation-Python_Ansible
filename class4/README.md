# Class 4 Exercises.

#### * exercise_01.py *
Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2.

#### * exercise_02.py *
Use Paramiko to change the 'logging buffered <size>' configuration on
pynet-rtr2. This will require that you enter into configuration mode.

#### * exercise_03.py *
Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.

#### * exercise_04.py *
Use PExpect to change the logging buffer size (logging buffered <size>) on
pynet-rtr2. Verify this change by examining the output of 'show run'.

#### * exercise_05.py *
Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko
to verify your state (i.e. that you are currently in configuration mode).

#### * exercise_06.py *
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.

#### * exercise_07.py *
Use Netmiko to change the logging buffer size (logging buffered <size>) on
pynet-rtr2.

#### * exercise_08.py *
Use Netmiko to change the logging buffer size (logging buffered <size>) and
to disable console logging (no logging console) from a file on both pynet-rtr1
and pynet-rtr2 (see 'Errata and Other Info, item #4).

#### * exercise_09.py *
Bonus Question - Redo exercise 6 but have the SSH connections happen
concurrently using either threads or processes (see example). What main issue
is there with using threads in Python?
