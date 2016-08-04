#!/usr/bin/env python 
import yaml
import json
from pprint import pprint as pp

'''
Python script that reads 2 files:
    1. yaml formatted file
    2. json formatted file

And prints the content of each one of them using pprint
'''

YAML_FILENAME = 'yml_out.yml'
JSON_FILENAME = 'json_out.json'

def read_yaml():
    with open(YAML_FILENAME, "r") as f:
        yaml_content = yaml.load(f)
    return yaml_content

def read_json():
    with open(JSON_FILENAME, "r") as f:
        json_content = json.load(f)
    return json_content

def main():
    yaml_content = read_yaml()
    print 'Content of YAML file {}: '.format(YAML_FILENAME)
    pp(yaml_content)
    print '======================================================='
    json_content = read_json()
    print 'Content of JSON file {}: ' .format(JSON_FILENAME)
    pp(json_content)

if __name__ == '__main__':
    main()

