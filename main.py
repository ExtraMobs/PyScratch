import pygame

window = pygame.display.set_mode((720, 405))

clock = pygame.time.Clock()

framerate = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit(0)

    clock.tick(framerate)
