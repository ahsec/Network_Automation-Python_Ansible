#!/usr/bin/env python
import yaml
import json

'''
Python script that creates a list with one of the elements being a dictionary with 2 keys
The script will then write the list to both a JSON and YAML file
'''

YAML_FILENAME = 'yml_out.yml'
JSON_FILENAME = 'json_out.json'

def create_list():
    a_list = range(10)
    a_list.append("Hola")
    a_list.append({})
    a_list[-1]['version'] = "7.2(2)"
    a_list[-1]['vendor'] = "Cisco"
    return a_list

def write_yaml(a_list):
    with open(YAML_FILENAME, "w") as f:
        f.write(yaml.dump(a_list, default_flow_style=False))

def write_json(a_list):
    with open(JSON_FILENAME, "w") as f:
        json.dump(a_list, f)

def main():
    a_list = create_list()
    write_yaml(a_list)
    print "File {} with YAML format has been created" .format(YAML_FILENAME)
    write_json(a_list)
    print "File {} with JSON format has been created" .format(JSON_FILENAME)

if __name__ == '__main__':
    main()
