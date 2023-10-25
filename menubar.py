import pygame

from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode


class MenuBarOption(GraphicNode):
    COLORS = {
        "idle": (150, 150, 150),
        "selected": (100, 100, 100),
        "expansible": (150, 125, 150),
    }

    top = False

    DEFAULT_WIDTH = 200
    DEFAULT_HEIGHT = 50
    PADING = 10

    surface_idle = None
    surface_selected = None

    function = None

    __tree_selected = False

    def __init__(self, data_to_display=None):
        super().__init__(
            resources.surface.new((self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT))
        )
        self.text = str(data_to_display)

    @property
    def selected(self):
        return self.surface is self.surface_selected

    @property
    def idle(self):
        return self.surface is self.surface_idle

    @property
    def tree_selected(self):
        children_selected = bool(sum([child.tree_selected for child in self.children]))
        return self.__tree_selected or children_selected

    def set_active_children(self, state: bool):
        for child in self.children:
            child.active = state

    def set_visible_children(self, state: bool):
        for child in self.children:
            child.visible = state

    def update(self):
        super().update()

        if self.active:
            if self.top:
                if self.priority == 0:
                    menubar = self.parent
                    self.rect.x = menubar.rect.x
                    self.rect.y = menubar.rect.y
                else:
                    last_opt = self.parent.children[self.priority - 1]
                    self.rect.x = last_opt.rect.right
                    self.rect.y = last_opt.rect.y
            else:
                if self.priority == 0:
                    if self.parent.top:
                        self.rect.x = self.parent.rect.x
                        self.rect.y = self.parent.rect.bottom
                    else:
                        self.rect.x = self.parent.rect.right
                        self.rect.y = self.parent.rect.y
                else:
                    last_opt = self.parent.children[self.priority - 1]
                    self.rect.x = last_opt.rect.x
                    self.rect.y = last_opt.rect.bottom
            if self.rect.collidepoint(self.program.devices.mouse.pos):
                if self.program.devices.mouse.get_pressed_down_in_frame(
                    pygame.BUTTON_LEFT
                ):
                    if not self.function is None:
                        self.function()
                self.surface = self.surface_selected
                self.__tree_selected = True
            else:
                self.__tree_selected = False

            if self.selected and not self.tree_selected:
                self.surface = self.surface_idle
                self.__tree_selected = False

            if self.selected:
                self.set_active_children(True)
                self.set_visible_children(True)
            elif self.idle:
                self.set_active_children(False)
                self.set_visible_children(False)

    def prepare_surface(self):
        font = resources.fonts.get_from_file_buffer(20, "MonoFonto")
        surface_text = font.render(self.text, True, (0, 0, 0))

        pretended_width = self.DEFAULT_WIDTH - 2 * self.PADING
        pretended_height = self.DEFAULT_HEIGHT - 2 * self.PADING

        surface_text = surface_text.subsurface(
            pygame.Rect(
                0,
                0,
                pretended_width
                if surface_text.get_width() + 2 * self.PADING > self.DEFAULT_WIDTH
                else surface_text.get_width(),
                pretended_height
                if surface_text.get_height() + 2 * self.PADING > self.DEFAULT_HEIGHT
                else surface_text.get_height(),
            )
        )

        blit_pos = (self.PADING, self.PADING)

        self.surface_idle = surface = self.surface.copy()
        surface.fill(self.COLORS["idle"])
        if len(self.children) > 0:
            marker_width = 10
            surface.fill(
                self.COLORS["expansible"],
                pygame.Rect(
                    -marker_width % self.rect.width, 0, marker_width, self.rect.height
                ),
            )
        surface.blit(surface_text, blit_pos)

        self.surface_selected = surface = self.surface.copy()
        surface.fill(self.COLORS["selected"])
        if len(self.children) > 0:
            marker_width = 5
            surface.fill(
                self.COLORS["expansible"],
                pygame.Rect(
                    -marker_width % self.rect.width, 0, marker_width, self.rect.height
                ),
            )
        surface.blit(surface_text, blit_pos)

        self.surface = self.surface_idle

    def draw(self):
        super().draw(self.parent.surface if self.top else self.program.display.surface)


class MenuBar(GraphicNode):
    COLOR = (170, 170, 170)

    def __init__(self, nested_data: dict):
        width = self.program.window.width

        super().__init__(resources.surface.new((width, MenuBarOption.DEFAULT_HEIGHT)))
        self.set_data_from_nested_tree(nested_data)

    def set_data_from_nested_tree(
        self, nested_tree: dict, parent_option=None, top_parent=None
    ):
        for key, value in nested_tree.items():
            new_option = MenuBarOption(key)
            new_option.top = top_parent is None
            if parent_option is None:
                self.add_children(new_option)
            else:
                parent_option.add_children(new_option)

            if callable(value):
                new_option.function = value
            elif type(value) is dict:
                self.set_data_from_nested_tree(
                    value, new_option, new_option if new_option.top else top_parent
                )
            new_option.prepare_surface()

    def draw(self):
        self.surface.fill(self.COLOR)
        super().draw()
