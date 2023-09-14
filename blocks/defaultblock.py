import pygame

from fakeshaders import ColorMAShader
from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode
from gameengine.nodes.node import Node


class DefaultBlock(Node):
    def __init__(self, color):
        self.rect = pygame.FRect(0, 0, 0, 0)
        self.color_shader = ColorMAShader(color, [0, 0, 0, 0])

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

    def update_images(self, text):
        font = resources.fonts.get_from_file_buffer(35, "MonoFonto")

        self.text_image.surface = text_surf = font.render(text, True, (255, 255, 255))

        width_sum = self.start_image.rect.width + self.end_image.rect.width

        if (text_w := text_surf.get_width()) > width_sum - 10:
            self.mid_image.visible = True
            self.mid_image.active = True
            self.mid_image.surface = mid_surf = resources.surface.new(
                mid_surf_size := (
                    text_w - (width_sum - 10) + 5,
                    self.start_image.surface.get_height(),
                )
            )
            mid_surf.fill(
                (255, 255, 255),
                pygame.Rect(
                    (0, 0), (mid_surf_size[0], mid_surf_size[1] - mid_surf_size[1] / 10)
                ),
            )
        else:
            self.mid_image.visible = False
            self.mid_image.active = False

    def set_position(self, new_pos):
        self.start_image.rect.topleft = new_pos

    def update(self):
        if self.priority - 4 > 0:
            block_above_ref = self.parent.children[self.priority - 1]
            self.set_position(block_above_ref.rect.bottomleft)

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