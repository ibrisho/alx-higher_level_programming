#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """loads (decodes/ converts) string to JSON"""
    return (json.loads(my_str))
