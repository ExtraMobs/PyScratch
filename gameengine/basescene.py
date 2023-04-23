from gameengine.display import Display
from gameengine.hierarchicalobject import HierarchicalObject


class BaseScene(HierarchicalObject):
    color_fill = (0, 0, 0)

    def __init__(self):
        super().__init__()
        self.children = []

    def start(self):
        pass

    def reset(self):
        self.children.clear()

    def add_children(self, *children):
        for child in children:
            self.children.append(child)
            child.parent = self

    def remove_child(self, *children):
        for child in children:
            self.children.remove(child)

    def update(self, *args, **kwargs):
        for child in list(self.children):
            child.update()

    def draw(self):
        Display.surface.fill(self.color_fill)
        super().draw()
