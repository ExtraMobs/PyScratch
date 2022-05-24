import pygame


class Window:
    """System window.
    """
    def __init__(self):
        self.size = (0, 0)
        self.flags = (0, )
        self.surface = None
        self.rect = None
        self.backgroud = pygame.Color(0, 0, 0)

    def set_background(self, color):
        """Set window background.

        Args:
            color (iterable|RGB|pygame.Color): Background color.
        """
        self.backgroud = pygame.Color(color)

    def get_flag(self):
        """Get a single flag.

        Returns:
            int: The flag.
        """
        flag = self.flags[0]
        for flag_ in self.flags[1:]:
            flag = flag | flag_
        return flag

    def update_size(self):
        """Update window size.
        """
        self.surface = pygame.display.set_mode(self.size, self.get_flag())
        self.rect = self.surface.get_rect()

    def set_size(self, width=1, height=1):
        """Set window size.

        Args:
            width (int, optional): Window width. Defaults to current width.
            height (int, optional): Window height. Defaults to current height.
        """
        self.size = (width, height)
        self.update_size()

    def set_flags(self, *flags):
        """Set flags to use in the window.
        """
        self.flags = flags

    def get_rect(self):
        return self.surface.get_rect()

    def update_display(self):
        pygame.display.update()

    def draw_widget(self, widget):
        self.surface.blit(widget.surface, widget.position)

    def clear_window(self):
        """Fill window with background color.
        """        
        self.surface.fill(self.backgroud)
