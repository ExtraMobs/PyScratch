import pygame

from gameengine import resources
from gameengine.nodes.node import Node
from lateralbar import LateralBar, LateralBarButton
from menubar import MenuBar


class UI(Node):
    menubar = None
    lateral_bar = None

    def __init__(self) -> None:
        self.menubar = MainMenuBar()
        self.lateral_bar = MainLateralBar(self.menubar)
        super().__init__(self.lateral_bar, self.menubar)


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


class MainMenuBar(MenuBar):
    def __init__(self):
        super().__init__(
            {
                "Projeto": {
                    "Novo Projeto": self.new_project,
                    "Abrir Projeto": self.open_project,
                },
            }
        )

    def new_project(self):
        project = self.program.scene.project
        project.reset()
        print(id(project))

    def open_project(self):
        print("implementar o carregamento de um projeto já existente")
