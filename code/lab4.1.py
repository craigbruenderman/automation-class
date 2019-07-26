#!/usr/bin/python

import pyeapi

node = pyeapi.connect(host='192.168.0.14', username='arista', password='arista', return_node=True)
users = node.api('users')
users.create('testuser', secret='foo')
users.set_privilege('testuser', value='15')
users.set_role('testuser', value='network-admin')
