from gameengine.basechild import BaseChild
import enum

TEXT_STATIC = enum.auto()

class Text(BaseChild):
    def __init__(self, mode, font) -> None:
        super().__init__()
        
        if mode == TEXT_STATIC:
            