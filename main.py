from gameengine.display import Display
from gameengine.engine import Engine
from gameengine.resources import Resources
from gameengine.window import Window
from scenes.mainscene import MainScene


class PyScratch:
    def __init__(self):
        self.load_assets()

        Window.set_size((1280, 720))
        Display.update_display_from_window()
        Engine.set_scene(MainScene())

    def load_assets(self):
        Resources.Files.add_from_path("MonoFonto", "monofonto rg.otf")

    def start(self):
        Engine.start_loop()


if __name__ == "__main__":
    PyScratch().start()
