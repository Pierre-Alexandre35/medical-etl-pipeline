import json
from pathlib import Path


def remove_file_extension(filepath: str) -> str:
    pth = Path(filepath)
    fn = pth.with_suffix('').stem
    return fn 


def save_to_file(input_data: str, filepath: str) -> None:
    with open(filepath, 'w') as the_file:
        the_file.write(input_data)