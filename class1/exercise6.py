#!/usr/bin/env python
import yaml

YAML_FILENAME = 'yml_out'
JSON_FILENAME = 'json_out'

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

def main():
    a_list = create_list()
    write_yaml(a_list)
    print "File {} with YAML format has been created" .format(YAML_FILENAME)

if __name__ == '__main__':
    main()

