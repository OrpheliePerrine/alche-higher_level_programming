#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them into a file named add_item.json using JSON
representation.

- Uses save_to_json_file (Task 5)
- Uses load_from_json_file (Task 6)
- Creates the file if it does not exist
- Appends new arguments each time the script is executed
"""

import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, otherwise start with an empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Extend the list with all new command-line arguments
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
