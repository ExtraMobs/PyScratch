from gameengine.nodes.node import Node
from scenes.main.ui.lateralbar import MainLateralBar
from scenes.main.ui.menubar import MainMenuBar


class UI(Node):
    menubar = None
    lateral_bar = None

    def __init__(self) -> None:
        self.menubar = MainMenuBar()
        self.lateral_bar = MainLateralBar(self.menubar)
        super().__init__(self.lateral_bar, self.menubar)
