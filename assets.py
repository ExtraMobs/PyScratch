import pygame

from gameengine import resources


def build_start_block(width, height, color, border_radius):
    surface = resources.surface.new((width, height))
    quarter_width = width / 4
    pygame.draw.rect(
        surface,
        color,
        pygame.Rect((0, 0), (quarter_width, height - height / 10)),
        border_top_left_radius=border_radius,
        border_bottom_left_radius=border_radius,
    )
    right_x = quarter_width + 30
    pygame.draw.polygon(
        surface,
        color,
        [
            (quarter_width, 0),
            (quarter_width + 10, height / 10),
            (quarter_width + 20, height / 10),
            (right_x, 0),
            (right_x, height - height / 10),
            (quarter_width + 20, height),
            (quarter_width + 10, height),
            (quarter_width, height - height / 10),
        ],
    )

    pygame.draw.rect(
        surface,
        color,
        pygame.Rect((right_x, 0), (width - right_x, height - height / 10)),
    )

    return surface


def build_end_block(height, color, border_radius):
    surface = resources.surface.new((20, height))
    pygame.draw.rect(
        surface,
        color,
        pygame.Rect((0, 0), (surface.get_width(), height - height / 10)),
        border_top_right_radius=border_radius,
        border_bottom_right_radius=border_radius,
    )

    return surface


def load_assets():
    resources.files.add_from_path("MonoFonto", "assets/monofonto rg.otf")

    width, height = 100, 50
    block_default_color = (255, 255, 255)
    radius = 10

    resources.surface.set(
        "block_start", build_start_block(width, height, block_default_color, radius)
    )

    resources.surface.set(
        "block_end", build_end_block(height, block_default_color, radius)
    )
