import pygame
from managers import DrawManager, ProcessManager


class Program:
    def __init__(self, window_manager, event_manager, framerate_manager):
        self.event_manager = event_manager
        self.window_manager = window_manager
        self.framerate_manager = framerate_manager

        self.process_manager = ProcessManager()
        self.draw_manager = DrawManager()

    def run_loop(self):
        while True:
            self.event_manager.process()
            self.process_manager.process()
            self.draw_manager.process()

            match self.event_manager.get(pygame.QUIT).type:
                case pygame.QUIT:
                    raise SystemExit(0)

            self.window_manager.update_display()
            self.framerate_manager.process()
