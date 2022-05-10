from ..visual.window import Window
from ..logic.events import Events


class Loop:
    def __init__(self) -> None:
        self.active = True

    def run(self, container, window, events, time):
        while self.active:
            events.process_events(container)
            window.clear_window()
            container.draw()
            window.update_display()
            time.process()