from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from gameengine.nodes.graphicnode import GraphicNode
from gameengine.nodes.node import Node
from gameengine.nodes.scene import Scene
from gameengine.nodes.shadingnode import ShadingNode

Program = None
if TYPE_CHECKING:
    from gameengine.core.program import Program


Node = Node | GraphicNode | ShadingNode
Button = int
Key = int
KeySate = int
Vector2 = pygame.Vector2
Scene = Scene
