def read_lines(file_path: str) -> list:
    """Read all lines from a file safely. Returns a list of strings."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        return []
