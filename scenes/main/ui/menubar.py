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
        project = self.program.scene.project
        project.reset()
        print(id(project))

    def open_project(self):
        print("implementar o carregamento de um projeto já existente")
