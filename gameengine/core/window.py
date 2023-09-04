from __future__ import annotations

import math

import pygame


class Metrics:
    @property
    def size(self) -> tuple[int]:
        return self.surface.get_size()

    @property
    def width(self) -> int:
        return self.surface.get_width()

    @property
    def height(self) -> int:
        return self.surface.get_height()

    @property
    def rect(self) -> pygame.Rect:
        return self.surface.get_rect()

    @property
    def is_landscape(self) -> bool:
        return self.width > self.height

    @property
    def is_portrait(self) -> bool:
        return self.height > self.width


class Display(Metrics):
    window: Window
    surface: pygame.Surface
    __scale: pygame.Vector2

    def __init__(self, size: tuple[int, int]) -> None:
        self.set_size(size)

    def set_size(self, size: tuple[int, int]):
        window_size = pygame.display.get_window_size()
        self.set_scale(
            (window_size[0] / size[0], window_size[1] / size[1]), window_size
        )

    def set_scale(
        self, *scale: iter[float,] | pygame.Vector2, window_size: tuple[int, int] = None
    ) -> None:
        if window_size is None:
            window_size = pygame.display.get_window_size()
        self.__scale = pygame.Vector2(*scale).xy
        try:
            self.surface = pygame.Surface(
                (
                    math.ceil(window_size[0] / self.__scale.x),
                    math.ceil(window_size[1] / self.__scale.y),
                )
            ).convert_alpha()
        except pygame.error as err:
            print(err)

    @property
    def scale(self) -> pygame.Vector2:
        return self.__scale


class Window(Metrics):
    surface: pygame.Surface

    def __init__(self, title=None, size: tuple[int, int] = (1, 1), *flags) -> None:
        if not title is None:
            self.set_title(title)
        self.set_size(size, *flags)

    def update(self, display: Display) -> None:
        if display.size != self.size:
            pygame.transform.scale(
                display.surface,
                self.size,
                self.surface,
            )
        else:
            self.surface.blit(display.surface, (0, 0))
        pygame.display.update()

    def set_size(self, size: tuple[int, int], *flags) -> None:
        flag = pygame.SRCALPHA
        for f in flags:
            flag |= f
        self.surface = pygame.display.set_mode(size, flag)

    def set_title(self, title: str) -> None:
        pygame.display.set_caption(title)

    def get_title(self) -> None:
        return pygame.display.get_caption()

    def set_icon(self, icon: pygame.Surface) -> None:
        pygame.display.set_icon(icon)
