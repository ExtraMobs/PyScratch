from gameengine.nodes.scene import Scene
from menubar import MenuBar


class MainScene(Scene):
    def __init__(self) -> None:
        self.bg = (200, 200, 200)

        super().__init__(MenuBar())
