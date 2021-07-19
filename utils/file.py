from pathlib import Path

def remove_file_extension(filepath):
    pth = Path(filepath)
    fn = pth.with_suffix('').stem
    return fn 