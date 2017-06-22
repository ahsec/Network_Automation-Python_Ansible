# Class 1 Exercises.

#### * exercise_06.py *
Write a Python program that creates a list. One of the elements of the list
should be a dictionary with at least two keys. Write this list out to a file
using both YAML and JSON formats. The YAML file should be in the expanded form.

#### * exercise_07.py *
Write a Python program that reads both the YAML file and the JSON file created
in exercise6 and pretty prints the data structure that is returned.

#### * exercise_08.py *
Write a Python program using ciscoconfparse that parses the *cisco_ipsec.txt*
config file. Note, this config file is not fully valid (i.e. parts of the
  configuration are missing). The script should find all of the crypto map
  entries in the file (lines that begin with 'crypto map CRYPTO') and for each
 crypto map entry print out its children.

#### * exercise_09.py *
Find all of the crypto map entries that are using PFS group2
