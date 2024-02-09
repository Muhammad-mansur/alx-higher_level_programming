#!/usr/bin/python3


""" Load, Add, Save """


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
write_file = __import__('1-write_file').write_file

try:
    json_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    json_list = []

if len(sys.argv) > 1:
    new_items = sys.argv[1:]
    json_list.extend(new_items)

save_to_json_file(json_list, "add_item.json")
