from bricks.tetrisBrick import TetrisBrick

class Square(TetrisBrick):
    def __init__(self, posHeight, posWidth):
        shape = [[1, 1], [1, 1]]
        super().__init__(posWidth, posHeight, shape)
