class TetrisBrick(object):
    def __init__(self, posWidth, posHeight, shape):
        self.posHeight = posHeight
        self.posWidth = posWidth
        self.shape = shape

    def RotateClockwise(self, mapWidth):
        if self.posWidth + len(self.shape) > mapWidth:
            self.posWidth = self.posWidth - (self.posWidth + len(self.shape) - mapWidth)
        self.shape = list(zip(*self.shape[::-1]))
