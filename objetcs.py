class ProcessableObject:
    @property
    def process_priority(self):
        return self.process_manager.to_process.index(self)

    @property
    def process_manager(self):
        return self.program.process_manager

    @property
    def draw_manager(self):
        return self.program.process_manager

    def __init__(self, program):
        self.program = program

    def destroy(self):
        while (index := self.process_manager.to_process.index(self)) != -1:
            del self.process_manager.to_process[index]

    def process(self): ...


class GraphicObject(ProcessableObject):
    @property
    def draw_priority(self):
        return self.draw_manager.to_draw.index(self)

    def destroy(self):
        super().destroy()
        while (index := self.draw_manager.to_draw.index(self)) != -1:
            del self.draw_manager.to_draw[index]

    def draw(self): ...
