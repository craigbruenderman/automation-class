#!/usr/bin/env python3

from __future__ import print_function, unicode_literals
from pprint import pprint
import yaml
import json

with open("ports.yml", 'r') as stream:
    try:
        interfaces = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
print(type(interfaces), len(interfaces), "\n")
for item in interfaces:
    print(type(item))
print("\n")
pprint(interfaces)

with open('ports.json', 'w') as outfile:
    json.dump(interfaces, outfile)
