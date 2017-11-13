from bricks.tetrisBrick import TetrisBrick

class L_shape(TetrisBrick):
    def __init__(self, posHeight, posWidth):
        shape = [[1, 0], [1, 0],[1, 0],[1, 1]]
        super().__init__(posWidth, posHeight, shape)
