import pygame
from managers import EventManager, FramerateManager, WindowManager
from objetcs import Container
from program import Program


class PyScratch(Program):
    def __init__(self):
        super().__init__(
            WindowManager(pygame.Window(self.__class__.__name__, (720, 405))),
            EventManager(),
            FramerateManager(60),
        )

        self.set_scene(EditorScene(self))

        self.run_loop()

    def set_scene(self, scene):
        super().set_scene(scene)

        scene.unpack(self)


class EditorScene(Container):
    def unpack(self):
        pass


PyScratch()
