import pygame

from gameengine import resources
from lateralbar import LateralBar, LateralBarButton


class MainLateralBarButton(LateralBarButton):
    def __init__(self):
        super().__init__(resources.surface.new((50, 50)))
        border_radius = 10
        pygame.draw.rect(
            self.surface,
            (160, 160, 160),
            pygame.Rect((0, 0), self.rect.size),
            border_top_right_radius=border_radius,
            border_bottom_right_radius=border_radius,
        )

        padding = 10
        pygame.draw.polygon(
            self.surface,
            (50, 50, 50),
            [
                (padding, padding),
                (self.rect.width - padding, self.rect.centery),
                (padding, self.rect.bottom - 10),
            ],
        )


class MainLateralBar(LateralBar):
    def __init__(self, menubar):
        super().__init__(
            (300, self.program.display.height - menubar.rect.height),
            MainLateralBarButton(),
        )
        self.rect.y = menubar.rect.bottom
        self.surface.fill((160, 160, 160))

        self.default_speed = 2000

    def update(self):
        super().update()
