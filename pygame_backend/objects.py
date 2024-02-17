import pygame

from .generics import (typeDrawManager, typeEventManager, typeFramerateManager,
                       typeIterableProcessableObjects, typeProcessManager,
                       typeProgram, typeWindowManager)


class ProgramObject:
    def __init__(self, program: typeProgram) -> None:
        self.program = program

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


class ProcessableObject(ProgramObject):
    @property
    def process_priority(self) -> int:
        return self.process_manager.to_process.index(self)

    def __init__(self, program: typeProgram) -> None:
        super().__init__(program)
        self.process_manager.to_process.append(self)

    def destroy(self) -> None:
        self.process_manager.to_process.remove(self)

    def process(self) -> None:
        pass


class DrawableObject(ProcessableObject):
    @property
    def draw_priority(self) -> int:
        return self.draw_manager.to_draw.index(self)

    def __init__(self, program: typeProgram) -> None:
        super().__init__(program)
        self.draw_manager.to_draw.append(self)

    def destroy(self) -> None:
        super().destroy()
        self.draw_manager.to_draw.remove(self)

    def draw(self) -> None:
        pass


class Container(ProgramObject):
    program_objects: typeIterableProcessableObjects

    def __init__(self, program: typeProgram) -> None:
        self.program = program
        self.program_objects = self.unpack()

    def clear(self) -> None:
        for object in self.program_objects:
            object.destroy()

    def unpack(self) -> typeIterableProcessableObjects:
        return ()
