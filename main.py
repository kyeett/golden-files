import os
import json
import logging 
from jinja2 import Template
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
def parse_hw_data(hw_data):
    hw_data_new = []

    for d in hw_data:
        d['id'] = d['id'] - 1
        d['last_name'] = d['last_name'].upper()
        d[u'location'] = d.get(u'location',u'Unknown')
        d.pop('gender')
        hw_data_new.append(d)
    return hw_data_new


def prettify_parsed_data(parsed_data):
    template = Template("""{% for result in data %}
INFORMATION
\tID:\t\t{{ result['id'] }}
\tName:\t\t{{ result['last_name'] }}, {{ result['first_name'] }}
\tLocation:\t{{ result['location'] }}
{% endfor %}""")
    return template.render(data=parsed_data)


def main():
    try:
        in_data = load_json_test_file('testdata/hardware.golden')
    except IOError as e:
        logging.error(e)
        exit(1)

    parsed_data = parse_hw_data(in_data)



    out_text = prettify_parsed_data(parsed_data)

    save_test_file('testdata/out_text.golden', prettify_parsed_data(out_text))
    save_json_test_file('testdata/out_json.golden', parsed_data)