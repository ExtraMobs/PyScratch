from ..logic.events import Events
from ..visual.window import Window


class Loop:
    def __init__(self) -> None:
        self.active = True

    def run(self, container, window, events, time):
        while self.active:
            events.process_events(container)
            container.process()
            window.clear_window()
            container.draw()
            window.update_display()
            time.process()
