class ProcessableObject:
    @property
    def process_priority(self):
        return self.process_manager.to_process.index(self)

    @property
    def process_manager(self):
        return self.program.process_manager

    @property
    def draw_manager(self):
        return self.program.draw_manager

    @property
    def window_manager(self):
        return self.program.window_manager

    @property
    def event_manager(self):
        return self.program.event_manager

    @property
    def framerate_manager(self):
        return self.program.framerate_manager

    @property
    def display_surface(self):
        return self.window_manager.display_surface

    def __init__(self, program):
        self.program = program
        self.process_manager.to_process.append(self)

    def destroy(self):
        while (index := self.process_manager.to_process.index(self)) != -1:
            del self.process_manager.to_process[index]

    def process(self): ...


class GraphicObject(ProcessableObject):
    @property
    def draw_priority(self):
        return self.draw_manager.to_draw.index(self)

    def __init__(self, program):
        super().__init__(program)
        self.draw_manager.to_draw.append(self)

    def destroy(self):
        super().destroy()
        while (index := self.draw_manager.to_draw.index(self)) != -1:
            del self.draw_manager.to_draw[index]

    def draw(self): ...


class Container:
    def __init__(self, program):
        self.program = program

    def unpack(self):
        pass
