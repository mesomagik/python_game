class Map(object):
    def __init__(self, height, width, squareSize):
        self.squareSize = squareSize
        self.height = height
        self.width = width
        self.mapMatrix = [[0 for i in range(width)] for j in range(height)]
        self.connectedBricks = [[0 for i in range(width)] for j in range(height)]
        self.points = 0

    def ClearMap(self):
        print("\n" * 25)
        self.mapMatrix = [[0 for i in range(self.width)] for j in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if self.connectedBricks[i][j] == 1:
                    self.mapMatrix[i][j] = 1

    def PrintMap(self):
        for j in range(self.width):
            print("XX", end='')
        print()
        scoreString = "SCORE: " + str(self.points)
        print("XX  ", end='')
        print(scoreString, end='')
        for iter in range(self.width - 4):
            print(" ", end='')
        print("XX")
        for j in range(self.width):
            print("XX", end='')
        print()

        for i in range(self.height):
            for j in range(self.width):
                if self.mapMatrix[i][j] == 0:
                    print("  ", end='')
                else:
                    print("XX", end='')
            print("|")

    def AddBrick(self, brick):
        for lines in range(len(brick.shape)):
            for itemInLine in range(len(brick.shape[lines])):
                self.mapMatrix[brick.posWidth + lines][brick.posHeight + itemInLine] = brick.shape[lines][itemInLine]

    def AddConnectedBrick(self, brick):
        for lines in range(len(brick.shape)):
            for itemInLine in range(len(brick.shape[lines])):
                if brick.shape[lines][itemInLine] == 1:
                    self.connectedBricks[brick.posWidth + lines][brick.posHeight + itemInLine] = 1
        self.CheckIfLineIsFull()

    def CheckCollision(self, brick):
        for lines in range(len(brick.shape)):
            for itemInLine in range(len(brick.shape[lines])):
                if brick.posWidth + len(brick.shape) >= self.height:
                    return True
                elif  brick.shape[lines][itemInLine] == 1 and self.mapMatrix[brick.posWidth + lines][brick.posHeight + itemInLine] == 1:
                    self.UpBrick(brick)
                    return True

        return False

    def DropBrick(self, brick):
        brick.posWidth += 1

    def MoveLeft(self, brick):
        if brick.posHeight > 0:
            brick.posHeight -= 1

    def MoveRight(self, brick):
        if brick.posHeight + len(brick.shape[0]) < self.width:
            brick.posHeight += 1

    def UpBrick(self, brick):
        brick.posWidth -= 1

    def CheckIfLineIsFull(self):
        for line in range(self.height):
            counter = 0
            for itemInLine in range(self.width):
                if self.connectedBricks[line][itemInLine] == 0:
                    break
                counter += 1
                if counter == self.width:
                    self.DeleteLineAndAddPoint(line)

    def DeleteLineAndAddPoint(self, lineNumber):
        print(len(self.connectedBricks))
        del self.connectedBricks[lineNumber]
        newList = [[0 for i in range(self.width)]]
        newList = newList + self.connectedBricks
        self.connectedBricks = newList
        print(str(len(self.connectedBricks)))

        self.points += 1
