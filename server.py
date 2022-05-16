import time
import json
import random
from snake import *
# Import socket module
from socket import *
import threading
theGameIsOn = True
apple = [random.randint(0, boardSize[0]), random.randint(0, boardSize[1])]

SERVER_ADDRESS = ("10.9.6.193", serverPort)
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Prepare a sever socket
#Fill in start
serverSocket.bind(SERVER_ADDRESS)

def playerSender(mySnake: Snake, otherSnake: Snake) -> None:
    while theGameIsOn  == True:
        # send data to the player
        message = {'mySnake': mySnake.__dict__(), 'otherSnake': otherSnake.__dict__(), 'apple':apple}
        serverSocket.sendto(str(message).encode(), mySnake.playerSocket)

def playerGetter(snake1: Snake, snake2:Snake):
    while theGameIsOn == True:
        print('message:')
        message, clientAddress = serverSocket.recvfrom(2048)
        message = message.decode()
        print(message)
        snake = 0
        if snake1.playerSocket == clientAddress:
            snake = snake1
        else:
            snake = snake2
        
        match message:
            case 'up':
                snake.direction = 'up'
            case 'down':
                snake.direction = 'down'
            case 'left':
                snake.direction = 'left'
            case 'right':
                snake.direction = 'right'



def moveSnake(snake: Snake, apple = apple) -> None:
    newHead = [0,0]
    newHead[0] = snake.body[-1][0]
    newHead[1] = snake.body[-1][1]
    
    match snake.direction:
        case 'up':
            newHead[1] -= 1
        case 'down':
            newHead[1] += 1
        case 'left':
            newHead[0] -= 1
        case 'right':
            newHead[0] += 1
    snake.body.append(newHead)
    if newHead == apple:
        apple = [random.randint(0, boardSize[0]), random.randint(0, boardSize[1])]
        while not (apple in snake1.body or apple in snake2.body):
            apple = [random.randint(0, boardSize[0]), random.randint(0, boardSize[1])]
    else:
        snake.body.pop(0)

def isSnakeLose(mySnake: Snake, otherSnake: Snake) -> bool:
    head = mySnake.body[-1]
    #the player out from board
    if head[0] < 0 or head[0] >= boardSize[1] or head[1] < 0 or head[1] >= boardSize[0]:
        return True
    # #is the player get into other snake
    # if head in otherSnake.body:
    #     return True
    # #is the player get into himself
    # for i in range(len(mySnake.body)-1):
    #     if head == mySnake.body[i]:
    #         return True
    return False

# Set up a new connection from the client
print('Waiting for player 1')
snake1 = Snake([5, 7], 'right' ,RED, serverSocket.recvfrom(2048)
[1])
print('Waiting for player 2')
snake2 = Snake([10, 7], 'left' ,BLUE, serverSocket.recvfrom(2048)
[1])

print('Connected')


playerSender1 = threading.Thread(target=playerSender, args=(snake1, snake2))
playerSender2 = threading.Thread(target=playerSender, args=(snake2, snake1))

playerSender1.start()
playerSender2.start()

playerGetter1 = threading.Thread(target= playerGetter, args= (snake1, snake2))
playerGetter1.start()
time.sleep(5)
# play the game:
print('The Game is Start:')
while theGameIsOn == True:
    moveSnake1 = threading.Thread(target=moveSnake, args=(snake1,))
    moveSnake2 = threading.Thread(target=moveSnake, args=(snake2,))
    moveSnake1.start()
    moveSnake2.start()
    moveSnake1.join()
    moveSnake2.join()
    isSnake1Lose = isSnakeLose(snake1, snake2)
    isSnake2Lose = isSnakeLose(snake2, snake1)
    if isSnake1Lose and isSnake2Lose:
        theGameIsOn = 'draw'
    elif isSnake1Lose:
        theGameIsOn = 'snake2'
    elif isSnake2Lose:
        theGameIsOn = 'snake1'
    time.sleep(1)

print(theGameIsOn)
playerSender1.join()
playerSender2.join()
playerGetter1.join()
serverSocket.sendto(theGameIsOn.encode(), snake1.playerSocket)
serverSocket.sendto(theGameIsOn.encode(), snake2.playerSocket)
serverSocket.close()
