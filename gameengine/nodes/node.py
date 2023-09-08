from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gameengine.generics import Program


class Node:
    parent: "Node"
    program: "Program"
    active = True
    visible = True

    def __init__(self, *children) -> None:
        """
        BaseNode is the base class for all objects in the scenes.

        Args:
            children (Iterable): Optional initial child nodes
        """
        self.children = []
        self.add_children(*children)

    def add_children(self, *children) -> None:
        """
        Add children to node.

        Args:
            children (Iterable): child nodes
        """
        for child in children:
            self.children.append(child)
            child.parent = self

    def kill(self) -> None:
        """
        Kill yourself. Killing a node removes it from its parent.
        """
        if self.parent is not None:
            self.parent.children.remove(self)

    def update(self) -> None:
        if self.active:
            if not self.program.request_quit:
                for child in list(self.children):
                    child.update()

    def draw(self) -> None:
        if self.visible:
            for child in self.children:
                child.draw()

    @property
    def priority(self):
        return self.parent.children.index(self)

    @property
    def path(self):
        if self.parent is None or not Node in self.parent.__class__.__mro__:
            return ()
        else:
            return *self.parent.path, self.priority

    @property
    def surface(self):
        return self.parent.surface

    def get_children_tree(self, __index=0):
        spaces = (__index * 4) * " "
        tree = f",\n".join(
            [child.get_children_tree(__index + 1) for child in self.children]
        )
        if len(self.children) == 0:
            list_children = f" []"
        else:
            list_children = " [\n" + f"{tree}" + f"\n{spaces}]"
        return spaces + repr(self) + list_children

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} | {id(self)}"
