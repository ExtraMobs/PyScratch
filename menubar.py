from inspect import isfunction

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

    function = None

    def __init__(self, data_to_display=None):
        super().__init__(
            resources.surface.new((self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT))
        )
        self.text = str(data_to_display)

        self.prepare_surface()

    @property
    def selected(self):
        return self.surface is self.surface_selected

    @property
    def idle(self):
        return self.surface is self.surface_idle

    def set_active_children(self, state: bool):
        for child in self.children:
            child.active = state

    def set_visible_children(self, state: bool):
        for child in self.children:
            child.visible = state

    def update(self):
        super().update()

        if self.rect.collidepoint(self.program.devices.mouse.pos):
            self.surface = self.surface_selected
        elif self.selected:
            self.surface = self.surface_idle

        if self.selected:
            self.set_visible_children(True)
            self.set_visible_children(True)
        elif self.idle:
            self.set_visible_children(False)
            self.set_visible_children(False)

    def prepare_surface(self):
        font = resources.fonts.get_from_file_buffer(20, "MonoFonto")
        surface_text = font.render(self.text, True, (0, 0, 0))

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

        self.surface_idle = self.surface.copy()
        self.surface_idle.fill(self.COLORS["idle"])
        self.surface_idle.blit(surface_text, blit_pos)

        self.surface_selected = self.surface.copy()
        self.surface_selected.fill(self.COLORS["selected"])
        self.surface_selected.blit(surface_text, blit_pos)

        self.surface = self.surface_idle

    def update_pos_recursively(self, last_opt=None):
        if last_opt is None:
            self.rect.y = 0
        else:
            self.rect.y = last_opt.rect.bottom
        for child in self.children:
            child.update_pos_recursively(self)


class Tree(Node):
    def __init__(self, nested_tree: dict) -> None:
        super().__init__()
        self.set_children_from_nested_tree(nested_tree)

    def set_children_from_nested_tree(
        self, nested_tree: dict, parent_option=None, top_parent=None
    ):
        for key, value in nested_tree.items():
            new_option = Option(key)
            if parent_option is None:
                self.add_children(new_option)
            else:
                parent_option.add_children(new_option)

            if isfunction(value):
                new_option.function = value
            elif type(value) is dict:
                self.set_children_from_nested_tree(
                    value, new_option, new_option if top_parent is None else top_parent
                )

        if parent_option is None:
            last_child = None
            for child in self.children:
                if not last_child is None:
                    child.rect.x = last_child.rect.right

                child.update_pos_recursively()
                last_child = child


class MenuBar(GraphicNode):
    COLOR = (170, 170, 170)

    def __init__(self):
        width = self.program.window.width

        super().__init__(resources.surface.new(self.program.window.size))
        self.surface_bar = resources.surface.new((width, Option.DEFAULT_HEIGHT))

        self.surface_bar.fill(self.COLOR)
        self.add_children(
            Tree(
                {
                    "a1": {"b1": [], "b2": []},
                    "a2": {"b1": [], "b2": []},
                }
            )
        )

    def draw(self):
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.surface_bar, (0, 0))
        super().draw()
