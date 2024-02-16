import pygame
from managers import EventManager, FramerateManager, WindowManager
from program import Program


Program(
    WindowManager(pygame.Window("PyScratch", (720, 405))),
    EventManager(),
    FramerateManager(60),
).run_loop()
