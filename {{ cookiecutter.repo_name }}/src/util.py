import os

from src.config import INTERIM_DIR


def create_folder(path, prefix=INTERIM_DIR):
    """Create a folder if it does not exist and return path to it. Useful to ensure data folders
    are created."""
    if prefix is not None:
        path = prefix / path
    os.makedirs(path, exist_ok=True)
    return path
