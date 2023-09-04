from io import BytesIO
from os.path import abspath

files = {}


def add_from_path(name: str, path: str) -> None:
    with open(abspath(path), "rb") as font_file:
        files[name] = font_file.read()


def get(name: str) -> BytesIO:
    return BytesIO(files[name])
