from os.path import abspath

import pygame

sounds = {}


def load_from_file(path: str) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(abspath(path))


def add_from_file(name, path) -> None:
    sounds[name] = load_from_file(path)


def get(name) -> pygame.mixer.Sound:
    return sounds[name]
