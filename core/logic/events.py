import pygame


class Events:
    def process_events(self, container):
        events = pygame.event.get()
        container.process_events(events)