from .timer import Timer


class Animation(Timer):
    animations = {}

    def __init__(self, fps, *frames):
        """
        Animation object, responsible for handling animations
        being fully compatible with GraphicNode.

        Args:
            fps (int): animation frame per second
        """
        super().__init__(1 / fps, False)
        self.__frames = frames
        self.fps = fps
        self.frame_index = 0
        self.reverse = False

    @property
    def current_frame(self):
        """
        current animation frame.

        Returns:
            surface: a pygame Surface
        """
        return self.__frames[self.frame_index].copy()

    def update(self):
        super().update()
        for _ in range(self.reached):
            self.frame_index += -1 if self.reverse else 1
            self.frame_index %= len(self.__frames)

    @classmethod
    def from_assets(cls, fps, *assets):
        """
        Build an animation from some assets files.
        """
        return cls(fps, *assets)
