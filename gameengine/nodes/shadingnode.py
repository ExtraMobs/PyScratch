import pygame

from .node import Node


class ShadingManager(Node):
    def draw(self, surf: pygame.Surface) -> None:
        for shader in self.children:
            shader.draw(
                surf,
            )


class ShadingNode(Node):
    def __init__(self, *children) -> None:
        super().__init__(*children)
        self.shader_manager = ShadingManager()

    def add_shader(self, *new_shaders) -> None:
        self.shader_manager.add_children(*new_shaders)

    def update(self) -> None:
        super().update()
        self.shader_manager.update()

    def draw(self) -> None:
        super().draw()
        self.shader_manager.draw(self.surface)
