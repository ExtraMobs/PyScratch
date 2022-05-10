import pygame


class Time:
    def __init__(self, fps=30):
        self.deltatime = 1/fps
        self.clock = pygame.time.Clock()
        self.fps = fps

    def set_fps(self, fps):
        self.fps = fps

    def process(self):
        self.deltatime = self.clock.tick(self.fps) / 1000
