import pygame

from gameengine import resources
from gameengine.core.program import Program
from gameengine.core.window import Window
from scenes.main import MainScene


class PyScratch(Program):
    def __init__(self):
        super().__init__(Window("PyScratch", (1280, 720)))

        self.load_assets()

        self.set_scene(MainScene())
        print(self.scene.get_children_tree())

    def load_assets(self):
        resources.files.add_from_path("MonoFonto", "assets/monofonto rg.otf")

        block_default_color = (127, 127, 127)

        width, height = 100, 50
        surface = resources.surface.new((width, height))
        radius = 10
        quarter_width = width / 4
        pygame.draw.rect(
            surface,
            block_default_color,
            pygame.Rect((0, 0), (quarter_width, height - height / 10)),
            border_top_left_radius=radius,
            border_bottom_left_radius=radius,
        )
        right_x = quarter_width + 30
        pygame.draw.polygon(
            surface,
            block_default_color,
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
            block_default_color,
            pygame.Rect((right_x, 0), (width - right_x, height - height / 10)),
        )
        resources.surface.set("block_start", surface)

        surface = resources.surface.new((20, height))
        pygame.draw.rect(
            surface,
            block_default_color,
            pygame.Rect((0, 0), (surface.get_width(), height - height / 10)),
            border_top_right_radius=radius,
            border_bottom_right_radius=radius,
        )
        resources.surface.set("block_end", surface)


if __name__ == "__main__":
    PyScratch().start_loop()
