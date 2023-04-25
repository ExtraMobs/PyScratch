from gameengine.display import Display


class HierarchicalObject:
    def __init__(self) -> None:
        self.children = []

    def add_children(self, *children):
        for child in children:
            self.children.append(child)
            child.parent = self

    def remove_child(self, *children):
        for child in children:
            self.children.remove(child)

    def update(self, *args, **kwargs):
        for child in list(self.children):
            child.update()

    def reset(self):
        self.children.clear()

    def draw(self):
        for child in self.children:
            if hasattr(child, "draw"):
                child.draw()
