import pygame

from .generics import (
    typeContainer,
    typeDrawManager,
    typeEventManager,
    typeFramerateManager,
    typeProcessManager,
    typeWindowManager,
)
from .managers import (
    DrawManager,
    EventManager,
    FramerateManager,
    ProcessManager,
    WindowManager,
)


class Program:
    scene: typeContainer
    event_manager: typeEventManager
    window_manager: typeWindowManager
    framerate_manager: typeFramerateManager
    process_manager: typeProcessManager
    draw_manager: typeDrawManager

    def __init__(
        self,
        window_manager: WindowManager,
        event_manager: EventManager,
        framerate_manager: FramerateManager,
    ) -> None:
        self.event_manager = event_manager
        self.window_manager = window_manager
        self.framerate_manager = framerate_manager

        self.process_manager = ProcessManager()
        self.draw_manager = DrawManager()

    def set_scene(self, scene: typeContainer) -> None:
        self.scene = scene

    def run_loop(self) -> None:
        while True:
            self.event_manager.process()
            self.process_manager.process()
            self.draw_manager.process()

            match self.event_manager.get(pygame.QUIT).type:
                case pygame.QUIT:
                    raise SystemExit(0)

            self.window_manager.update_display()
            self.framerate_manager.process()
