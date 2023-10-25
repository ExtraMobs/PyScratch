import pygame

from gameengine.nodes.node import Node


class BlockManager(Node):
    drag_block = None

    def __init__(self) -> None:
        super().__init__()
        self.drag_block = None

    def add_blocks(self, *blocks):
        super().add_children(*blocks)

    def update(self):
        if self.program.devices.mouse.get_pressed_up_in_frame(pygame.BUTTON_LEFT):
            self.drag_block = None

        if not self.drag_block is None:
            self.drag_block.rect.x = (
                self.program.devices.mouse.pos.x - self.drag_block.drag_offset.x
            )
            self.drag_block.rect.y = (
                self.program.devices.mouse.pos.y - self.drag_block.drag_offset.y
            )
        super().update()
