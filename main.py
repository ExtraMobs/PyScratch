import pygame

from pygame_backend.managers import (EventManager, FramerateManager,
                                     WindowManager)
from pygame_backend.objects import Container
from pygame_backend.program import Program


class PyScratch(Program):
    def __init__(self) -> None:
        super().__init__(
            WindowManager(pygame.Window(self.__class__.__name__, (720, 405))),
            EventManager(),
            FramerateManager(60),
        )

        self.set_scene(EditorScene(self))

        self.run_loop()

    def set_scene(self, scene: Container) -> None:
        super().set_scene(scene)

        scene.unpack()


class EditorScene(Container):
    def unpack(self) -> None:
        pass


PyScratch()
