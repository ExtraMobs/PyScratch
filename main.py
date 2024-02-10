import pygame
from collections import defaultdict


class Program:
    def __init__(self, window_manager, event_manager, framerate_manager):
        self.event_manager = event_manager
        self.window_manager = window_manager
        self.framerate_manager = framerate_manager

    def run_loop(self):
        while True:
            self.event_manager.process()

            self.window_manager.update_display()
            self.framerate_manager.process()


class EventManager:
    def __init__(self):
        self.__data = defaultdict(lambda: None)

    def process(self):
        self.__data.clear()
        for event in pygame.event.get():
            self.__data[event.type] = event

    def get(self, type):
        return self.__data[type]


class DrawManager:
    def __init__(self):
        self.to_draw = []

    def process(self, window):
        for drawable_object in self.to_draw:
            pass


class WindowManager:
    def __init__(self, pygame_window):
        self.pygame_window = pygame_window
        self.display_surface = pygame_window.get_surface()

    def update_display(self):
        self.pygame_window.flip()


class FramerateManager:
    @property
    def framerate(self):
        self.clock.get_fps()

    def __init__(self, target_framerate):
        self.clock = pygame.time.Clock()
        self.target_framerate = target_framerate

    def process(self):
        self.clock.tick(self.target_framerate)


Program(
    WindowManager(pygame.Window("PyScratch", (720, 405))),
    EventManager(),
    FramerateManager(60),
)
