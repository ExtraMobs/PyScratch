from os.path import abspath
from typing import Any

import pygame

from .files import get as __get_file


def load_from_file(size: int, path: str) -> pygame.Font:
    return pygame.Font(abspath(path), size)


def get_from_file_buffer(size: int, name: Any) -> pygame.Font:
    return pygame.Font(__get_file(name), int(size))
