#!/usr/bin/env python

import pyeapi
from pprint import pprint

node = pyeapi.connect(host='192.168.0.14', username='arista', password='arista', return_node=True)

users = node.api('users')
users.create('testuser', secret='foo')
users.set_privilege('testuser', value='15')
users.set_role('testuser', value='network-admin')
print("Users on the device\n")
pprint(users.getall())
print("\n")

vlans = node.api('vlans')
d = (vlans.getall())
