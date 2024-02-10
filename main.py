import pygame


class ProgramLoop:
    def __init__(self, window_manager, framerate_manager):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit(0)

            window_manager.update_display()

            framerate_manager.process()


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
        self.target_framerate = 60

    def process(self):
        self.clock.tick(self.target_framerate)


ProgramLoop(WindowManager(pygame.Window("PyScratch", (720, 405))), FramerateManager(60))
