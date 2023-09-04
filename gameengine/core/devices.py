from __future__ import annotations

import pygame

from gameengine.generics import Button, Key, KeySate, Program, Vector2


class Mouse:
    pos: Vector2
    rel_pos: Vector2
    __pressed_in_frame: list
    __button_index: dict

    def __init__(self, program: "Program") -> None:
        self.display = program.display
        self.__pressed_in_frame = []
        self.pos = pygame.Vector2(0, 0)
        self.rel_pos = pygame.Vector2(0, 0)
        self.__button_index = {
            pygame.BUTTON_LEFT: 0,
            pygame.BUTTON_MIDDLE: 1,
            pygame.BUTTON_RIGHT: 3,
        }

    def update(self) -> None:
        down = pygame.event.get(pygame.MOUSEBUTTONDOWN)
        # up = pygame.event.get(pygame.MOUSEBUTTONUP)

        self.__pressed_in_frame.clear()
        for event in down:
            self.__pressed_in_frame.append(event.button)

        for event in pygame.event.get(pygame.MOUSEMOTION):
            self.pos.xy = (
                event.pos[0] / self.display.scale.x,
                event.pos[1] / self.display.scale.y,
            )
            self.rel_pos.xy = (
                event.rel[0] / self.display.scale.x,
                event.rel[1] / self.display.scale.y,
            )

    def get_pressed(self, button: Button) -> bool:
        return pygame.mouse.get_pressed()[self.__button_index[button]]

    def get_pressed_in_frame(self, button: Button) -> bool:
        return button in self.__pressed_in_frame


class KeyBoard:
    pressed_in_frame: dict
    keys: dict

    def __init__(self) -> None:
        self.pressed_in_frame = {pygame.KEYDOWN: [], pygame.KEYUP: []}
        self.keys = {}
        # self.key_sequence = []

    def update(self) -> None:
        # self.key_sequence.clear()
        self.pressed_in_frame[pygame.KEYDOWN].clear()
        self.pressed_in_frame[pygame.KEYUP].clear()

        down = pygame.event.get(pygame.KEYDOWN)
        up = pygame.event.get(pygame.KEYUP)

        for event in down:
            self.pressed_in_frame[pygame.KEYDOWN].append(event.key)
            self.keys[event.key] = event
        for event in up:
            self.pressed_in_frame[pygame.KEYUP].append(event.key)
            self.keys[event.key] = None

    def get_pressed(self, key: Key) -> bool:
        return self.get_key_event(key) is not None

    def get_key_event(self, key: Key) -> bool:
        return self.keys.get(key, None)

    def get_pressed_in_frame(self, state: KeySate, key: Key) -> bool:
        return key in self.pressed_in_frame[state]


class Devices:
    def __init__(self, program: Program) -> None:
        self.mouse = Mouse(program)
        self.keyboard = KeyBoard()

    def update(self) -> None:
        self.mouse.update()
        self.keyboard.update()
