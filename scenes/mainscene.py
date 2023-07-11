from children.menubar import MenuBar
from children.option import Option
from gameengine.basescene import BaseScene
from gameengine.engine import Engine


class MainScene(BaseScene):
    def __init__(self) -> None:
        super().__init__()
        self.bg = (200, 200, 200)

        menubar_test = MenuBar(
            {
                "a1": 
                    {"b1": lambda: print("hello world"),
                     "b2": lambda: print("hello world")},
                "a2": 
                    {"b1": lambda: print("hello world"), 
                     "b2": lambda: print("hello world")},
            },
            (self.surface.get_width(), 50),
        )
        self.add_children(menubar_test)

    def update(self):
        super().update()

        if Engine.request_quit:
            Engine.system_exit()
