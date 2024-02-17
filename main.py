import pygame

from pygame_backend.generics import typeIterableProcessableObjects, typeProgram
from pygame_backend.managers import (EventManager, FramerateManager,
                                     WindowManager)
from pygame_backend.objects import Container
from pygame_backend.program import Program
from ui.menubar import MenuBar


class PyScratch(Program):
    def __init__(self) -> None:
        super().__init__(
            WindowManager(pygame.Window(self.__class__.__name__, (1280, 720))),
            EventManager(),
            FramerateManager(60),
        )

        self.window_manager.background_color = (200, 200, 200)

        self.set_scene(EditorScene(self))


class EditorScene(Container):
    def __init__(self, program: typeProgram) -> None:
        super().__init__(program)

    def unpack(self) -> typeIterableProcessableObjects:
        return (MenuBar(self.program),)


if __name__ == "__main__":
    PyScratch().run_loop()
