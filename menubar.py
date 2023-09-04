import pygame

from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode
from gameengine.nodes.node import Node


class Option(GraphicNode):
    COLORS = {
        "idle": (150, 150, 150),
        "selected": (100, 100, 100),
    }

    DEFAULT_WIDTH = 200
    DEFAULT_HEIGHT = 50
    PADING = 10

    surface_idle = None
    surface_selected = None

    def __init__(self, data_to_display=None):
        super().__init__(resources.surface.new((1, 1)))
        self.text = str(data_to_display)

        self.prepare_surface()

    def prepare_surface(self):
        font = resources.fonts.get_from_file_buffer(20, "MonoFonto")
        surface_text = font.render(self.text, True, (0, 0, 0))
        surface = resources.surface.new((self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT))

        pretended_width = self.DEFAULT_WIDTH - 2 * self.PADING
        pretended_height = self.DEFAULT_HEIGHT - 2 * self.PADING

        surface_text = surface_text.subsurface(
            pygame.Rect(
                0,
                0,
                pretended_width
                if surface_text.get_width() + 2 * self.PADING > self.DEFAULT_WIDTH
                else surface_text.get_width(),
                pretended_height
                if surface_text.get_height() + 2 * self.PADING > self.DEFAULT_HEIGHT
                else surface_text.get_height(),
            )
        )

        blit_pos = (self.PADING, self.PADING)

        self.surface_idle = surface.copy()
        self.surface_idle.fill(self.COLORS["idle"])
        self.surface_idle.blit(surface_text, blit_pos)

        self.surface_selected = surface.copy()
        self.surface_selected.fill(self.COLORS["selected"])
        self.surface_selected.blit(surface_text, blit_pos)

        self.surface = self.surface_idle


class Tree(Node):
    def __init__(self, nested_tree: dict) -> None:
        super().__init__()
        self.set_children_from_nested_tree(nested_tree)

    def set_children_from_nested_tree(self, nested_tree: dict, option=None):
        for key, value in nested_tree.items():
            new_option = Option(key)
            if option is None:
                self.add_children(new_option)
            else:
                option.add_children(new_option)

            # if callable(value):


class MenuBar(GraphicNode):
    COLOR = (170, 170, 170)

    def __init__(self):
        width = self.program.window.width

        super().__init__(resources.surface.new((width, Option.DEFAULT_HEIGHT)))

        self.surface.fill(self.COLOR)

        self.add_children(
            Tree(
                {
                    "aaaaaaaaaaaaaaaaaa1": {"b1": [], "b2": []},
                    "a2": {"b1": [], "b2": []},
                }
            )
        )
