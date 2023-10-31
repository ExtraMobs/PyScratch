from blocks.defaultblock import DefaultBlock, Instruction


class CallBlock(DefaultBlock):
    def __init__(self, *args):
        super().__init__((255, 127, 0))

        self.block_images.remount(
            *(Instruction(Instruction.LABEL, data) for data in args)
        )
