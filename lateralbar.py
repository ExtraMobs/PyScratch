import enum

from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode


class LateralBarButton(GraphicNode):
    def __init__(self, image):
        super().__init__(image)

    def update(self):
        self.rect.x = self.parent.rect.right
        self.rect.centery = self.parent.rect.centery
        super().update()

    def draw(self, surface=None):
        super().draw(self.parent.parent.surface)


class LateralBar(GraphicNode):
    RIGHT = enum.auto()
    LEFT = enum.auto()

    def __init__(self, size, button):
        super().__init__(resources.surface.new(size))
        self.orientation = self.LEFT

        self.add_children(button)

    def update(self):
        if self.orientation == self.LEFT:
            self.rect.x = -self.rect.width
        elif self.orientation == self.RIGHT:
            self.rect.x = self.program.display.width

        super().update()
