#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a file named add_item.json using JSON format.

- Uses save_to_json_file (from 5-save_to_json_file.py)
- Uses load_from_json_file (from 6-load_from_json_file.py)
- Creates the file if it does not exist
- Appends new arguments each time the script is executed
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try loading existing items from the file
try:
    items = load_from_json_file(filename)
except Exception:
    items = []

# Add all new command-line arguments
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
