import pygame
from button import Button


class ButtonLoadProject(Button):
    def __init__(self, program):
        background = pygame.Surface((200, 70))
        background_selected = background.copy()
        background_selected.fill((100, 100, 100))
        font = pygame.font.SysFont("Arial", 30)
        text = font.render("Carregar Projeto", True, (255, 255, 255))
        t_rect = text.get_rect()
        t_rect.center = background.get_rect().center
        background.blit(text, t_rect)
        background_selected.blit(text, t_rect)
        super().__init__(program, background, background_selected)

    def process_events(self, events):
        super().process_events(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.collide_point(event.pos):
                    if event.button == pygame.BUTTON_LEFT:
                        print(event)
                        ...
