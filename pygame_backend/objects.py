import pygame

from .generics import (typeDrawManager, typeEventManager, typeFramerateManager,
                       typeProcessManager, typeProgram, typeWindowManager)


class ProcessableObject:
    @property
    def process_priority(self) -> int:
        return self.process_manager.to_process.index(self)

    @property
    def process_manager(self) -> typeProcessManager:
        return self.program.process_manager

    @property
    def draw_manager(self) -> typeDrawManager:
        return self.program.draw_manager

    @property
    def window_manager(self) -> typeWindowManager:
        return self.program.window_manager

    @property
    def event_manager(self) -> typeEventManager:
        return self.program.event_manager

    @property
    def framerate_manager(self) -> typeFramerateManager:
        return self.program.framerate_manager

    @property
    def display_surface(self) -> pygame.Surface:
        return self.window_manager.display_surface

    def __init__(self, program: typeProgram) -> None:
        self.program = program
        self.process_manager.to_process.append(self)

    def destroy(self) -> None:
        while (index := self.process_manager.to_process.index(self)) != -1:
            del self.process_manager.to_process[index]

    def process(self) -> None: ...


class GraphicObject(ProcessableObject):
    @property
    def draw_priority(self) -> int:
        return self.draw_manager.to_draw.index(self)

    def __init__(self, program: typeProgram) -> None:
        super().__init__(program)
        self.draw_manager.to_draw.append(self)

    def destroy(self) -> None:
        super().destroy()
        while (index := self.draw_manager.to_draw.index(self)) != -1:
            del self.draw_manager.to_draw[index]

    def draw(self) -> None: ...


class Container:
    def __init__(self, program: typeProgram) -> None:
        self.program = program

    def unpack(self) -> None:
        pass
