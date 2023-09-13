from gameengine.nodes.scene import Scene
from project import Project

from .ui import UI


class MainScene(Scene):
    project = None
    ui = None

    def __init__(self) -> None:
        self.project = Project()
        self.ui = UI()
        super().__init__(self.ui, self.project)

        self.set_background_color((200, 200, 200))
