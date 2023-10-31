import pygame

from gameengine.nodes.node import Node


class DragBlockManager:
    def __init__(self, block_manager):
        self.block_manager = block_manager
        self.drag_block = None

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

    @property
    def program(self):
        return self.block_manager.program


class BlockManager(Node):
    drag_block_manager = None

    def __init__(self) -> None:
        super().__init__()
        self.drag_block_manager = DragBlockManager(self)

    def add_blocks(self, *blocks):
        super().add_children(*blocks)

    def update(self):
        self.drag_block_manager.update()
        super().update()

    # temp
    @property
    def drag_block(self):
        return self.drag_block_manager.drag_block

    @drag_block.setter
    def drag_block(self, value):
        self.drag_block_manager.drag_block = value
