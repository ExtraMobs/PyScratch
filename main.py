from gameengine.display import Display
from gameengine.engine import Engine
from gameengine.window import Window
from scenes.mainscene import MainScene


class PyScratch:
    def __init__(self):
        Window.set_size((1280, 720))
        Display.update_display_from_window()
        Engine.set_scene(MainScene())

    def start(self):
        Engine.start_loop()


if __name__ == "__main__":
    PyScratch().start()
