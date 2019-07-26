import json
import yaml
from pprint import pprint

# Create a list
dns_servers = ['8.8.8.8', '8.8.4.4']
# Create a dictionary
core1 = {'hostname': 'core1.cbts.com', 'vendor': 'arista', 'dns': dns_servers, 'users': {'admin': 15, 'craigb': 0}, 'vlans': [{'name': 'Data', 'id': 10}, {'name': 'Voice', 'id': 50}] }

# Function to print list and dictionary
def as_python():
    print("------ As Python Native List ------")
    print(dns_servers)
    print("\n")
    print("------ As Python Native Dictionary ------")
    pprint(core1)
    print("\n")

# Function to convert Python dict to JSON
def as_json():
    print("------ As JSON ------")
    print(json.dumps(core1, indent=4))
    print("\n")

# Function to convert Python dict to YAML
def as_yaml():
    print("------ As YAML ------\n")
    print(yaml.dump(core1))
