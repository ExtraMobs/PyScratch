class Container:
    def __init__(self, program):
        self.widgets = []
        self.program = program
    
    def add_widgets(self, *widgets):
        self.widgets.extend(widgets)
        
    def process_events(self, events):
        for widget in self.widgets:
            widget.process_events(events)

    def draw(self):
        for widget in self.widgets:
            if widget.is_drawable():
                self.program.window.draw_widget(widget)
