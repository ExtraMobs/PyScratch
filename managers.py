from collections import defaultdict
import pygame

from enums import CustomEvents


class EventManager:
    def __init__(self):
        none_event = pygame.Event(CustomEvents.NONE)
        self.__data = defaultdict(lambda: none_event)

    def process(self):
        self.__data.clear()
        for event in pygame.event.get():
            self.__data[event.type] = event

    def get(self, event_type):
        return self.__data[event_type]


class ProcessManager:
    def __init__(self):
        self.to_process = []

    def process(self):
        for processable_object in self.to_process:
            processable_object.process()


class DrawManager:
    def __init__(self):
        self.to_draw = []

    def process(self):
        for drawable_object in self.to_draw:
            drawable_object.draw()


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
