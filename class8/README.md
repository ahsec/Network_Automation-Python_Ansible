# Class 8 Exercises.

#### * exercise_1_a.txt *
Initialize your Django database. Add the seven NetworkDevice objects and two
credentials objects into your database.  After this initialization, you should
be able to do the following (from the ~/DJANGOX/djproject directory):
```python
$ python manage.py shell

>>> from net_system.models import NetworkDevice, Credentials
>>> net_devices = NetworkDevice.objects.all()
>>> net_devices
[<NetworkDevice: pynet-rtr1>, <NetworkDevice: pynet-sw1>, <NetworkDevice: pynet-sw2>, <NetworkDevice: pynet-sw3>, <NetworkDevice: pynet-sw4>, <NetworkDevice: juniper-srx>, <NetworkDevice: pynet-rtr2>]

>>> creds = Credentials.objects.all()
>>> creds
[<Credentials: pyclass>, <Credentials: admin1>]
```
#### * exercise_1_b.txt *
Update the NetworkDevice objects such that each NetworkDevice links to the
correct Credentials.

#### * exercise_2.txt *
Set the vendor field of each NetworkDevice to the appropriate vendor.
Save this field to the database.

#### * exercise_3.txt *
Create two new test NetworkDevices in the database. Use both direct object
creation and the .get_or_create() method to create the devices.

#### * exercise_4.txt *
Remove the two objects created in the previous exercise from the database.

#### * exercise_5.py *
Use Netmiko to connect to each of the devices in the database. Execute
'show version' on each device. Calculate the amount of time required to do this.
Note, your results will be more reliable if you use Netmiko's
send_command_expect() method. There is an issue with the Arista vEOS switches
and Netmiko's send_command() method.

#### * exercise_6.py *
Use threads and Netmiko to execute 'show version' on each device in the
database. Calculate the amount of time required to do this. What is the
difference in time between executing 'show version' sequentially versus using
threads?

#### * exercise_7.py *
Repeat exercise 6 except use processes.

#### * exercise_8.py *
Optional bonus question--use a queue to get the output data back from the child processes in question 7. Print this output data to the screen in the main
process.
