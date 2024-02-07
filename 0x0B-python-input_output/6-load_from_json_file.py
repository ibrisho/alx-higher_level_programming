#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """creates json object from file"""
    with open(filename, mode='r', encoding='utf-8') as f_io:
        my_dict = json.loads(f_io.read())
        f_io.close()
    return my_dict
