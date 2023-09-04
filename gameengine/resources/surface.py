from os.path import abspath
from typing import Any

import pygame

surfaces = {}


def load_from_file(path: str, alpha=True) -> pygame.Surface:
    surface = pygame.image.load(abspath(path))
    try:
        if alpha:
            surface = surface.convert_alpha()
        else:
            surface = surface.convert()
        return surface
    except pygame.error:
        return surface


def add_from_file(name: Any, path: str, alpha=True) -> None:
    set(name, load_from_file(path, alpha))


def set(name: Any, surface: pygame.Surface, copy=False) -> None:
    if type(name) is pygame.Surface:
        raise Exception("The name cannot be a pygame surface.")
    if copy:
        surface = surface.copy()
    surfaces[name] = surface


def slice(asset: Any, *rects) -> pygame.Surface:
    surface = get(asset)
    return [surface.subsurface(rect).copy() for rect in rects]


def get(asset: Any, copy=True) -> pygame.Surface:
    if type(asset) is pygame.Surface:
        surface = asset
    else:
        surface = surfaces[asset]

    if copy:
        return surface.copy()
    else:
        return surface


def new(size: tuple, *flags, alpha=True) -> pygame.Surface:
    flag = 0
    for f in flags:
        if f != pygame.SRCALPHA:
            flag |= f
    if alpha:
        flag |= pygame.SRCALPHA
    return pygame.Surface(size, flag)
