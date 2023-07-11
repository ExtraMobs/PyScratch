from gameengine.basescene import BaseScene
from gameengine.engine import Engine
from gameengine.resources import Resources
from children.text import Text, TEXT_STATIC_MODE


class MainScene(BaseScene):
    def __init__(self) -> None:
        super().__init__()
        self.color_fill = (200, 200, 200)

    def update(self):
        super().update()

        if Engine.request_quit:
            Engine.system_exit()
