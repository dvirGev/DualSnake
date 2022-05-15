import ast
import sys 
from socket import *
from snake import *
from GUI import GUI
gui = GUI()
if len(sys.argv) == 1:
    print("what is the ip of the server?")
    serverName = input()
else:
    serverName = sys.argv[1]

clientSocket = socket(AF_INET,  SOCK_DGRAM)
clientSocket.sendto('up'.encode(),(serverName, serverPort))
isTheGameOn = True


while isTheGameOn:
    data = clientSocket.recvfrom(2048)[0].decode()
    
    data = ast.literal_eval(data)
    mySnake = Snake.copySnake(data['mySnake'])
    otherSnake = Snake.copySnake(data['otherSnake'])
    applePos = data['apple']
    data = gui.draw(mySnake, otherSnake, applePos)
    if data == 'Exit':
        isTheGameOn = False
    elif data != 'pass':
        clientSocket.sendto(data.encode(),(serverName, serverPort))
    





