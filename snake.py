from asyncio.windows_events import NULL
from enum import Enum
from sys import flags
from turtle import down

class Snake:
    def __init__(self, headPos: list, direction: str, color: tuple, playerSocket = NULL, ) -> None:
        self.playerSocket = playerSocket
        self.direction = direction
        if len(headPos) == 2:
            self.body = []
            dire = 0
            if direction == 'right':
                dire = -1
            else:
                dire = 1
            for i in range(5):
                i *= dire
                self.body.insert(0, [headPos[0]+i, headPos[1]])
        else:
            self.body = headPos
        self.color = color
    def copySnake(data: dict):
        return Snake(data['body'], data['direction'], data['color'])

    def __dict__(self) -> dict:
        return {'body': self.body, 'direction': self.direction, 'color': self.color}
  
serverPort = 5138
boardSize = (25, 25)
RED = (255,0,0)
BLUE = (0,0,255)
