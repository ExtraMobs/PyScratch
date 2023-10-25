from blockmanager import BlockManager
from blocks.callblock import CallBlock
from gameengine.nodes.scene import Scene
from project import Project
from scenes.main.ui import UI


class MainScene(Scene):
    project = None
    ui = None
    block_manager = None

    def __init__(self) -> None:
        self.project = Project()
        self.ui = UI()
        self.block_manager = BlockManager()
        super().__init__(
            self.project,
            self.block_manager,
            self.ui,
        )

        self.block_manager.add_blocks(c := CallBlock("test"))
        c.rect.topleft = (100, 100)
        self.set_background_color((200, 200, 200))
