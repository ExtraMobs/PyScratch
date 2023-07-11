import pygame

from children.option import Option
from gameengine.basescene import BaseScene
from gameengine.engine import Engine


class MainScene(BaseScene):
    def __init__(self) -> None:
        super().__init__()
        self.bg = (200, 200, 200)

        option_test = Option(pygame.Rect(10, 10, 100, 50), (100, 100, 100), "Test")
        self.add_children(option_test)

    def update(self):
        super().update()

        if Engine.request_quit:
            Engine.system_exit()
