from gameengine.display import Display
from gameengine.engine import Engine
from gameengine.window import Window
from scenes.pathchoose import PathChooseScene
from scenesmanager import ScenesManager


class PyScratch(ScenesManager):
    def __init__(self):
        super().__init__()
        self.reset_configs()
        self.set_scenes("editor", PathChooseScene())

    def reset_configs(self):
        Window.set_size((1280, 720))
        Display.update_display_from_window()

    def start(self):
        Engine.set_scene(self.get_scene("editor"))

        Engine.start_loop()


if __name__ == "__main__":
    PyScratch().start()
