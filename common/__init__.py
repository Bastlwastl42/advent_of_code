import os


def load_input_file(folder: str, file: str = 'input.txt'):
    """load the file input.txt from the given folder"""
    with open(os.path.join(folder, file), 'r') as f:
        return [e.rstrip() for e in f.readlines()]
