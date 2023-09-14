from blocks.callblock import CallBlock
from gameengine.nodes.scene import Scene
from project import Project
from scenes.main.ui import UI


class MainScene(Scene):
    project = None
    ui = None

    def __init__(self) -> None:
        self.project = Project()
        self.ui = UI()
        super().__init__(
            c1 := CallBlock("test"),
            c2 := CallBlock("test extended"),
            self.project,
            self.ui,
        )
        c1.rect.topleft = 100, 100
        c2.rect.topleft = 100, 200
        self.set_background_color((200, 200, 200))
