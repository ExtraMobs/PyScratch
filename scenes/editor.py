from children.menubutton import MenuButton
from gameengine.basescene import BaseScene
from gameengine.engine import Engine


class EditorScene(BaseScene):
    def __init__(self):
        super().__init__()
        opts = [MenuButton("Novo Projeto"), MenuButton("Carregar Projeto")]
        for index, opt in enumerate(opts):
            if index > 0:
                opt.rect.x = opts[index - 1].rect.right
        self.add_children(*opts)

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        if Engine.request_quit:
            Engine.system_exit()
