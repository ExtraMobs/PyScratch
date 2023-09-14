from blocks.defaultblock import DefaultBlock
from gameengine import resources
from gameengine.nodes.node import Node


class Module(Node):
    def __init__(self, name):
        self.name = name

        self.starter_block = DefaultBlock(resources)

        super().__init__(self.starter_block)


class Project(Node):
    def __init__(self) -> None:
        super().__init__()
        self.modules = []

    def reset(self) -> None:
        pass
