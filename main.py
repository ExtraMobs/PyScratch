from assets import load_assets
from gameengine.core.program import Program
from gameengine.core.window import Window
from scenes.main import MainScene


class PyScratch(Program):
    def __init__(self):
        super().__init__(Window("PyScratch", (1280, 720)))

        load_assets()

        self.set_scene(MainScene())
        print(self.scene.get_children_tree())


if __name__ == "__main__":
    PyScratch().start_loop()
