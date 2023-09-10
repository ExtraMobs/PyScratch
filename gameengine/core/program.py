import ctypes

import pygame

from gameengine.core.devices import Devices
from gameengine.core.window import Display, Window
from gameengine.nodes.node import Node
from gameengine.nodes.scene import Scene

ctypes.windll.user32.SetProcessDPIAware()

pygame.init()


class TimeManager:
    target_framerate: int
    delta: float
    clock: pygame.Clock

    def __init__(self, target_framerate: int) -> None:
        self.set_framerate(
            pygame.display.get_current_refresh_rate()
            if target_framerate is None
            else target_framerate
        )
        self.delta = 1 / self.target_framerate
        self.clock = pygame.time.Clock()

    def set_framerate(self, new_framerate: int) -> None:
        self.target_framerate = new_framerate

    def update(self) -> None:
        self.delta = self.clock.tick(self.target_framerate) / 1000


class EventsManager:
    uncaught_events: list[pygame.Event]

    def update(self):
        self.uncaught_events = pygame.event.get()


class Program:
    request_quit: bool

    window: Window
    display: Display

    time: TimeManager
    devices: Devices
    event: EventsManager

    scene: Scene

    def __init__(
        self, window: Window, display: Display = None, framerate: int = None
    ) -> None:
        self.request_quit = False
        Node.program = self
        pygame.register_quit(self.quit)
        self.window = window
        self.display = display
        if display is None:
            self.display = Display(window.size)
        self.devices = Devices(self)
        self.time = TimeManager(framerate)
        self.event = EventsManager()

        self.scene = Scene()

    def set_scene(self, new_scene: Scene) -> None:
        self.scene = new_scene

    def update(self) -> None:
        self.request_quit = len(pygame.event.get(pygame.QUIT)) > 0
        self.devices.update()
        self.event.update()

        self.scene.update()
        if not self.request_quit:
            self.scene.draw()

            self.window.update(self.display)

            self.time.update()

    def quit(self) -> None:
        pass

    def start_loop(self) -> None:
        while not self.request_quit:
            self.update()
        pygame.quit()
