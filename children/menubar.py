from dataclasses import dataclass

import pygame

from children.option import Option
from gameengine.basechild import BaseChild
from gameengine.resources import Resources


@dataclass
class MenuBarConfigs:
    option_width: int = 200
    bg = (170,170,170)


class MenuBar(BaseChild):
    def __init__(self, tree, size, configs=MenuBarConfigs()) -> None:
        super().__init__()
        self.tree = {}
        self.surface = Resources.Surface.new(size)
        self.rect = self.surface.get_frect()
        
        self.bg = configs.bg
        
        self.configs = configs

        self.set_tree(tree)

    def set_tree(self, tree: dict, current_node=None, depth=0, root_index=None):
        if current_node is None and depth == 0:
            self.children.clear()
            self.tree.clear()
            current_node = self.tree

        for index, item in enumerate(tree.items()):
            name, data = item
            new_node = {}
            if type(data) is dict:
                self.set_tree(data, new_node, depth + 1, index if root_index is None else root_index)
            elif callable(data):
                new_node = data
            current_node[
                Option(
                    pygame.Rect(
                        self.configs.option_width * (index if depth == 0 else depth),
                        self.rect.h*depth,
                        self.configs.option_width,
                        self.rect.h,
                    ),
                    name,
                )
            ] = new_node
        if depth == 0:
            for key in current_node.keys():
                self.add_children(key)
