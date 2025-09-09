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
