from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode
from gameengine.nodes.node import Node


class TreeNode(GraphicNode):
    def __init__(self):
        super().__init__(resources.surface.new((1, 1)))


class Option(TreeNode):
    COLORS = {
        "idle": (150, 150, 150),
        "selected": (100, 100, 100),
    }

    DEFAULT_WIDTH = 200
    PADING = 10

    def __init__(self, data_to_display=None):
        super().__init__()
        self.data = data_to_display

        self.prepare_surface()

    def prepare_surface(self):
        font = resources.fonts.get_from_file_buffer(20, "MonoFonto")
        print(font)
        # self.surface =


class Tree(Node):
    def __init__(self, nested_tree: dict) -> None:
        super().__init__()
        self.set_children_from_nested_tree(nested_tree)

    def set_children_from_nested_tree(self, nested_tree: dict, option=None):
        for key, value in nested_tree.items():
            new_option = Option(key)
            if option is None:
                self.add_children(new_option)
            else:
                option.add_children(new_option)


class MenuBar(GraphicNode):
    OPTION_HEIGHT = 50
    COLOR = (170, 170, 170)

    def __init__(self):
        width = self.program.window.width

        super().__init__(resources.surface.new((width, self.OPTION_HEIGHT)))

        self.surface.fill(self.COLOR)

        self.add_children(
            Tree({"a1": {"b1": [], "b2": []}, "a2": {"b1": [], "b2": []}})
        )
