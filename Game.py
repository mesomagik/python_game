
import time

from map import Map
from bricks.Square import Square
from bricks.L_shape import L_shape

if __name__ == '__main__':
    map = Map(15,10,1)
    brick = L_shape(6, 1)
    score = 0

    map.AddBrick(brick)
    map.PrintMap()
    changeBrick = False
    while True:

        key = input()
        map.ClearMap()

        if key == "s":
            map.DropBrick(brick)
            if map.CheckCollision(brick):
                map.AddConnectedBrick(brick)
                changeBrick = True
        elif key == "a":
            map.MoveLeft(brick)
            if map.CheckCollision(brick):
                map.MoveRight(brick)
                map.AddConnectedBrick(brick)
                changeBrick = True
        elif key == "d":
            map.MoveRight(brick)
            if map.CheckCollision(brick):
                map.MoveLeft(brick)
                map.AddConnectedBrick(brick)
                changeBrick = True
        elif key == "r":
            brick.RotateClockwise(map.width)
            if map.CheckCollision(brick):
                map.MoveLeft(brick)
                map.AddConnectedBrick(brick)
                changeBrick = True
        else:
            map.DropBrick(brick)
            if map.CheckCollision(brick):
                map.UpBrick(brick)
                map.AddConnectedBrick(brick)
                changeBrick = True

        map.AddBrick(brick)
        map.PrintMap()
        if changeBrick:
            brick = L_shape(6, 1)
            changeBrick = False
            map.ClearMap()
            map.AddBrick(brick)
            map.PrintMap()
