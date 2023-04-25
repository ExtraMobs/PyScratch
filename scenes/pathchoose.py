import pygame
from children.edittext import EditText
from children.list import List
from gameengine.basescene import BaseScene
from gameengine.display import Display
from gameengine.engine import Engine
from gameengine.mouse import Mouse


class PathChooseScene(BaseScene):
    color_fill = (127, 127, 127)

    def __init__(self):
        super().__init__()

        self.add_children(
            edittext := EditText((Display.width, 25)),
            List(
                (Display.width, Display.height - edittext.rect.height - 10),
                items=[chr(i) for i in range(64, 164)],
            ),
        )
        edittext.rect.bottom = Display.rect.bottom
        self.set_focus(edittext)

    def update(self):
        super().update()

        if Mouse.get_pressed_in_frame(pygame.BUTTON_LEFT):
            for obj in self.children:
                if obj.rect.collidepoint(Mouse.pos):
                    self.set_focus(obj)
                    break
        if Engine.request_quit:
            Engine.system_exit()
