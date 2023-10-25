import pygame

from fakeshaders import ColorMAShader
from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode
from gameengine.nodes.node import Node


class DefaultBlock(Node):
    def __init__(self, color):
        self.rect = pygame.FRect(0, 0, 0, 0)
        self.color_shader = ColorMAShader(color, [0, 0, 0, 0])

        self.drag_offset = False

        self.start_image = GraphicNode(resources.surface.get("block_start"))
        self.start_image.add_shader(self.color_shader)

        self.mid_image = GraphicNode(resources.surface.new((1, 1)))
        self.mid_image.add_shader(self.color_shader)

        self.end_image = GraphicNode(resources.surface.get("block_end"))
        self.end_image.add_shader(self.color_shader)

        self.text_image = GraphicNode(resources.surface.new((1, 1)))

        super().__init__(
            self.start_image, self.mid_image, self.end_image, self.text_image
        )

    def update_io_data(self, text):
        font = resources.fonts.get_from_file_buffer(35, "MonoFonto")

        self.text_image.surface = text_surf = font.render(text, True, (255, 255, 255))

        default_padding = 5
        double_padding = 2 * default_padding

        width_limit = (
            self.start_image.rect.width + self.end_image.rect.width - double_padding
        )

        if (text_w := text_surf.get_width()) > width_limit:
            self.mid_image.visible = True
            self.mid_image.active = True

            mid_surf_width = text_w - width_limit + default_padding
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

    def update(self):
        if self.program.scene.block_manager.drag_block is None:
            if self.program.devices.mouse.get_pressed_down_in_frame(pygame.BUTTON_LEFT):
                if self.rect.collidepoint(self.program.devices.mouse.pos):
                    self.drag_offset = (
                        self.program.devices.mouse.pos - self.rect.topleft
                    )
                    self.program.scene.block_manager.drag_block = self

        self.start_image.rect.topleft = self.rect.topleft

        if self.mid_image.visible:
            self.mid_image.rect.topleft = self.start_image.rect.topright
            self.end_image.rect.topleft = self.mid_image.rect.topright
        else:
            self.end_image.rect.topleft = self.start_image.rect.topright

        self.rect.width = self.end_image.rect.right - self.rect.x
        self.rect.height = self.end_image.rect.bottom - self.rect.y

        self.text_image.rect.x = 5 + self.start_image.rect.x
        self.text_image.rect.y = 2.5 + self.start_image.rect.y

        super().update()
