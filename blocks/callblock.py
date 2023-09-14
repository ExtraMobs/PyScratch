from blocks.defaultblock import DefaultBlock


class CallBlock(DefaultBlock):
    def __init__(self, func_name):
        self.func_name = func_name

        super().__init__((255, 127, 0))

        self.update_images(func_name)
