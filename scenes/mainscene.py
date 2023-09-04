from gameengine.nodes.scene import Scene


class MainScene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.bg = (200, 200, 200)
