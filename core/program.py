from .logic.time import Time
from .visual.window import Window
from .logic.loop import Loop
from .logic.events import Events
from .container import Container


class Program:
    def __init__(self):
        """Program.
        """
        self.container = Container(self)
        self.window = Window()
        self.events = Events()
        self.time = Time()
        self.loop = Loop()

    def get_deltatime(self):
        return self.time.deltatime

    def set_container(self, container_class):
        self.container = container_class(self)

    def run(self):
        """Execute the program.
        """        
        self.loop.run(self.container, self.window, self.events, self.time)

    def stop(self):
        self.loop.active = False
