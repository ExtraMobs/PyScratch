import enum

import pygame

from fakeshaders import ColorMAShader
from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode
from gameengine.nodes.node import Node


class Instruction:
    LABEL = enum.auto()

    type_ = None

    def __init__(self, type_, data) -> None:
        self.type_ = type_
        self.data = data


class BlockImages(Node):
    default_padding = 5

    def __init__(self, color) -> None:
        self.rect = pygame.FRect(0, 0, 0, 0)
        self.color_shader = ColorMAShader(color, [0, 0, 0, 0])

        self.start_image = GraphicNode(resources.surface.get("block_start"))
        self.start_image.add_shader(self.color_shader)

        self.mid_image = GraphicNode(resources.surface.new((1, 1)))
        self.mid_image.add_shader(self.color_shader)

        self.end_image = GraphicNode(resources.surface.get("block_end"))
        self.end_image.add_shader(self.color_shader)

        super().__init__(self.start_image, self.mid_image, self.end_image)

    def remount(self, *instructions):
        del self.children[3:]
        font = resources.fonts.get_from_file_buffer(35, "MonoFonto")

        for instruction in instructions:
            if instruction.type_ is Instruction.LABEL:
                self.add_children(
                    GraphicNode(font.render(instruction.data, True, (255, 255, 255)))
                )

        text_w = (
            (len(instructions) - 1) * self.default_padding
            + sum(child.rect.width for child in self.children[3:])
            if len(instructions) > 0
            else 0
        )

        double_padding = 2 * self.default_padding

        width_limit = (
            self.start_image.rect.width + self.end_image.rect.width - double_padding
        )

        if text_w > width_limit:
            self.mid_image.visible = True
            self.mid_image.active = True

            mid_surf_width = text_w - width_limit + self.default_padding
            mid_surf_height = self.start_image.surface.get_height()

            self.mid_image.surface = mid_surf = resources.surface.new(
                (mid_surf_width, mid_surf_height)
            )
            mid_surf.fill(
                (255, 255, 255),
                pygame.Rect(
                    (0, 0), (mid_surf_width, mid_surf_height - mid_surf_height / 10)
                ),
            )
        else:
            self.mid_image.visible = False
            self.mid_image.active = False

    def update(self) -> None:
        self.start_image.rect.topleft = self.rect.topleft

        if self.mid_image.visible:
            self.mid_image.rect.topleft = self.start_image.rect.topright
            self.end_image.rect.topleft = self.mid_image.rect.topright
        else:
            self.end_image.rect.topleft = self.start_image.rect.topright

        self.rect.width = self.end_image.rect.right - self.rect.x
        self.rect.height = self.end_image.rect.bottom - self.rect.y

        last_img = None
        for index, img in enumerate(self.children[3:]):
            if index == 0:
                img.rect.x = self.default_padding + self.start_image.rect.x
                img.rect.y = self.default_padding / 2 + self.start_image.rect.y
            else:
                img.rect.x = self.default_padding + last_img.rect.right
                img.rect.y = last_img.rect.y
            last_img = img

        super().update()


class DefaultBlock(Node):
    def __init__(self, color):
        self.drag_offset = None

        self.block_images = BlockImages(color)

        super().__init__(self.block_images)

    def update(self):
        if self.program.scene.block_manager.drag_block is None:
            if self.program.devices.mouse.get_pressed_down_in_frame(pygame.BUTTON_LEFT):
                if self.rect.collidepoint(self.program.devices.mouse.pos):
                    self.drag_offset = (
                        self.program.devices.mouse.pos - self.rect.topleft
                    )
                    self.program.scene.block_manager.drag_block = self

        super().update()

    @property
    def rect(self):
        return self.block_images.rect
