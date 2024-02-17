import pygame
from pygame_backend.generics import typeIterableProcessableObjects

from pygame_backend.managers import (EventManager, FramerateManager,
                                     WindowManager)
from pygame_backend.objects import Container, DrawableObject, ProcessableObject
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


class EditorScene(Container):
    def __init__(self, program: Program) -> None:
        super().__init__(program)
        print(self.draw_manager.to_draw)

        self.clear()

        print(self.draw_manager.to_draw)


    def unpack(self) -> typeIterableProcessableObjects: 
        return ProcessableObject(self.program), DrawableObject(self.program)


PyScratch()
