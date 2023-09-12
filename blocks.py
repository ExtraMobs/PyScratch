from gameengine.nodes.graphicnode import GraphicNode


class Block(GraphicNode):
    type_ = None

    def __init__(self, image):
        super().__init__(image)

    def update(self):
        if self.priority != 0:
            block_above_ref = self.parent.children[self.priority - 1]
            self.rect.x = block_above_ref.rect.x
            self.rect.y = block_above_ref.rect.bottom

        super().update()
