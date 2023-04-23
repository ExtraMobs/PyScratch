from .display import Display
from .hierarchicalobject import HierarchicalObject


class BaseChild(HierarchicalObject):
    surface = None
    rect = None

    def draw(self):
        super().draw()
        Display.surface.blit(self.surface, self.rect)
