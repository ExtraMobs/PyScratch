import pygame

from pygame_backend.generics import (typeProgram, typePygameSurface,
                                     typeRecursiveDict)
from pygame_backend.objects import DrawableObject


class MenuBar(DrawableObject):
    bar: typePygameSurface

    def __init__(self, program: typeProgram) -> None:
        super().__init__(program)

        self.bar = pygame.Surface((self.window_manager.pygame_window.size[0], 50))
        self.bar.fill((150, 150, 150))

        self.set_data(
            {
                "Projeto": {
                    "Novo Projeto": lambda: print("New Project"),
                    "Abrir Projeto": lambda: print("Load Project"),
                },
            }
        )

    def set_data(self, data: typeRecursiveDict) -> None:
        pass

    def draw(self) -> None:
        self.display_surface.blit(self.bar, (0, 0))
