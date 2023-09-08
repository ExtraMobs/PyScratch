from gameengine.nodes.scene import Scene
from menubar import MenuBar


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
        print("implementar a criação de um novo projeto")

    def open_project(self):
        print("implementar o carregamento de um projeto já existente")


class MainScene(Scene):
    def __init__(self) -> None:
        self.bg = (200, 200, 200)

        super().__init__(MainMenuBar())
