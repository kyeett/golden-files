import os
import json
import logging 
from pprint import pprint

def load_json_test_file(filename):
    with open(filename) as f:
        return json.load(f)

def load_test_file(filename):
    with open(filename) as f:        
        return f.read()

def save_test_file(filename, content):
    with open(filename, "w+") as f:
        f.write(content)

def save_json_test_file(filename, obj):
    save_test_file(filename, json.dumps(obj, indent=4))

# Changes id to 0-index and turns last name to uppercase
def transform_hw_data_1(hw_data):
    hw_data_new = []

    for d in hw_data:
        d['id'] = d['id'] - 1
        d['last_name'] = d['last_name'].upper()
        d[u'location'] = d.get(u'location',u'Unknown')
        d.pop('gender')
        hw_data_new.append(d)
    return hw_data_new

try:
    hw_data = load_json_test_file('testdata/hardware.golden')
except IOError as e:
    logging.error(e)
    exit(1)
     
transformed_data = transform_hw_data_1(hw_data)
pprint(transformed_data)
save_json_test_file('testdata/transformed.golden', transformed_data)
