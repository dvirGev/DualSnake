from pickle import NONE
import string
from turtle import width
import pygame
from pygame import *
from snake import *
pygame.init()
# mixer.init()
# font.init()
WIDTH, HEIGHT = 760, 760
BLACK = (0, 0, 0)
apple = 'apple.png'

class GUI():
    def __init__(self) -> None:
        self.screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
        self.squareSize = [0,0]
        self.space = 0
        self.apple_image = image.load(apple)
        self.apple_image = pygame.transform.scale(self.apple_image, (35, 35))

    def draw(self, snake1:Snake, snake2:Snake, applePos: list) -> str:
        self.screen.fill((255,255,255))#Wite
        res = 'pass'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                return 'Exit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    res = 'up'
                elif event.key == pygame.K_DOWN:
                    res = 'down'
                elif event.key == pygame.K_LEFT:
                    res = 'left'
                elif event.key == pygame.K_RIGHT:
                    res = 'right'
                 
        self.space = int(self.screen.get_height()/10)
        self.squareSize[0] = int((self.screen.get_height() - self.space)/boardSize[0])
        self.squareSize[1] = int(self.screen.get_width()/boardSize[1])
        pygame.draw.line(self.screen, Color(0, 0, 0), (0, self.squareSize[0]*3), (self.screen.get_width(), self.squareSize[0]*3),1)
        
        self.drawSnake(snake1)
        self.drawSnake(snake2)
        self.drawApple(applePos)
        
        display.update()
        return res

            
    def drawSnake(self, snake:Snake):
        print(snake.body)
        for s in snake.body:
            print(s)
            x = s[0] * self.squareSize[0] + self.space
            y = s[1] * self.squareSize[1]
            pygame.draw.rect(self.screen, snake.color, (x,y,self.squareSize[0],self.squareSize[1]))
    def drawApple(self, pos: list):
        x = pos[0] * self.squareSize[0]  + self.space
        y = pos[1] * self.squareSize[1]
        self.screen.blit(self.apple_image, (x, y))


