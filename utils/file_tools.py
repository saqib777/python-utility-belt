"""
File Tools
----------
Simple helper functions for file operations.
"""

def read_file(path: str) -> str:
    """
    Read the entire content of a file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    """
    Write content to a file (overwrites if file exists).
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
import os

def file_exists(path: str) -> bool:
    """
    Check if a file exists at the given path.
    """
    return os.path.isfile(path)


def append_to_file(path: str, content: str) -> None:
    """
    Append text to the end of a file.
    Creates the file if it does not exist.
    """
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)

import csv

def read_csv_file(filename: str) -> list[dict]:
    """Read a CSV file and return a list of dictionaries.
    Example: read_csv_file("data.csv") -> [{'name': 'Alice', 'age': '30'}, ...]
    """
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found.")

