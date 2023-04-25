from children.list import List
from gameengine.basescene import BaseScene
from gameengine.display import Display
from gameengine.engine import Engine


class PathChooseScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.add_children(List(Display.size, items=[chr(i) for i in range(64, 164)]))

    def update(self):
        super().update()

        if Engine.request_quit:
            Engine.system_exit()
