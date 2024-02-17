from collections import defaultdict
import pygame

from .enums import CustomEvents


class EventManager:
    def __init__(self) -> None:
        none_event = pygame.Event(CustomEvents.NONE)
        self.__data = defaultdict(lambda: none_event)

    def process(self) -> None:
        self.__data.clear()
        for event in pygame.event.get():
            self.__data[event.type] = event

    def get(self, event_type) -> pygame.Event:
        return self.__data[event_type]


class ProcessManager:
    def __init__(self) -> None:
        self.to_process = []

    def process(self) -> None:
        for processable_object in self.to_process:
            processable_object.process()


class DrawManager:
    def __init__(self) -> None:
        self.to_draw = []

    def process(self) -> None:
        for drawable_object in self.to_draw:
            drawable_object.draw()


class WindowManager:
    def __init__(self, pygame_window: pygame.Window) -> None:
        self.pygame_window = pygame_window
        self.display_surface = pygame_window.get_surface()
        self.background_color = (0, 0, 0)

    def update_display(self) -> None:
        self.pygame_window.flip()
        self.display_surface.fill(self.background_color)


class FramerateManager:
    @property
    def framerate(self) -> float:
        self.clock.get_fps()

    def __init__(self, target_framerate: int) -> None:
        self.clock = pygame.time.Clock()
        self.target_framerate = target_framerate

    def process(self) -> None:
        self.clock.tick(self.target_framerate)
