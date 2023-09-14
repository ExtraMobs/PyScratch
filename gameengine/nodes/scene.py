import pygame

from gameengine.misc.shader import FakeShader
from gameengine.nodes.graphicnode import ShadingNode


class BackgroundColor(FakeShader):
    def __init__(self, target_color) -> None:
        super().__init__()
        self.target_color = target_color

    def draw(self, target_surf):
        if not self.target_color is None:
            target_surf.fill(self.target_color)


class Scene(ShadingNode):
    def __init__(self, *children):
        super().__init__(*children)
        self.parent = self.program.display
        self.bg_shader = BackgroundColor((0, 0, 0))

    def set_background_color(self, target_color):
        self.bg_shader.target_color = target_color

    def update(self) -> None:
        self.bg_shader.update()
        super().update()

    def draw(self):
        self.bg_shader.draw(self.surface)
        super().draw()

    @property
    def surface(self) -> pygame.Surface:
        return self.program.display.surface
