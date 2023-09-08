from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gameengine.generics import Program


class Node:
    parent: "Node"
    program: "Program"

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

    def remove_children(self, *children) -> None:
        """
        Remove children from node.

        Args:
            children (Iterable): child nodes
        """
        for child in children:
            child.kill()

    def kill(self) -> None:
        """
        Kill yourself. Killing a node removes it from its parent.
        """
        if self.parent is not None:
            self.parent.children.remove(self)

    def update(self) -> None:
        if not self.program.request_quit:
            for child in list(self.children):
                child.update()

    def draw(self) -> None:
        for child in self.children:
            child.draw()

    @property
    def active(self) -> bool:
        return bool(sum(child.active for child in self.children))

    @active.setter
    def active(self, value: bool) -> None:
        for child in self.children:
            child.active = value

    @property
    def visible(self) -> bool:
        return bool(sum(child.visible for child in self.children))

    @visible.setter
    def visible(self, value: bool) -> None:
        for child in self.children:
            child.active = value

    @property
    def path(self):
        if self.parent is None:
            return None
        else:
            return self.parent.path + str(self.parent.children.index(self))

    @property
    def surface(self):
        return self.parent.surface

    def get_children_tree(self, __index=0):
        spaces = (__index * 4) * " "
        tree = f",\n{spaces}".join(
            [child.get_children_tree(__index + 1) for child in self.children]
        )
        return spaces + repr(self) + f" [\n{spaces}" + f"{tree}" + f"\n{spaces}]"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} | {id(self)}"
