from gameengine.nodes.scene import Scene
from menubar import MenuBar
from project import Project


class MainMenuBar(MenuBar):
    project = None

    def __init__(self):
        super().__init__(
            {
                "Projeto": {
                    "Novo Projeto": self.new_project,
                    "Abrir Projeto": self.open_project,
                },
            }
        )

        self.project = Project()

    def new_project(self):
        self.project.kill()
        self.project = Project()
        self.add_children(self.project)
        print(id(self.project))

    def open_project(self):
        print("implementar o carregamento de um projeto já existente")


class MainScene(Scene):
    def __init__(self) -> None:
        self.bg = (200, 200, 200)

        super().__init__(MainMenuBar())
