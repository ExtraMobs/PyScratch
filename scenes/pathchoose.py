from children.edittext import EditText
from children.list import List
from gameengine.basescene import BaseScene
from gameengine.display import Display
from gameengine.engine import Engine


class PathChooseScene(BaseScene):
    def __init__(self):
        super().__init__()

        self.color_fill = (127, 127, 127)

        self.add_children(
            edittext := EditText((Display.width, 25)),
            List(
                (Display.width, Display.height - edittext.rect.height - 10),
                items=[chr(i) for i in range(64, 164)],
            ),
        )
        edittext.rect.bottom = Display.rect.bottom

    def update(self):
        super().update()

        if Engine.request_quit:
            Engine.system_exit()
