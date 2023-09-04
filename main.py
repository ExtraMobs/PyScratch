from gameengine import resources
from gameengine.core.program import Program
from gameengine.core.window import Window
from scenes.mainscene import MainScene


class PyScratch(Program):
    def __init__(self):
        super().__init__(Window("PyScratch", (1280, 720)))

        self.load_assets()

        self.set_scene(MainScene())

    def load_assets(self):
        resources.files.add_from_path("MonoFonto", "assets/monofonto rg.otf")


if __name__ == "__main__":
    PyScratch().start_loop()
