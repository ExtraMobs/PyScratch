class FRect:
    def __init__(self, left=0, top=0, right=0, bottom=0, frect=None):
        if frect is None:
            self.left, self.top, self.right, self.bottom = left, top, right, bottom
        else:
            self.left, self.top, self.right, self.bottom = (
                frect.left,
                frect.top,
                frect.right,
                frect.bottom,
            )

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.bottom - self.top
