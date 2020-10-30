import cv2
import numpy as np
from random import choice
image=cv2.imread("abhi.png")
class Snake:
    def __init__(self,front,x,y):
        self.front=front
        self.x=x
        self.y=y
    def move(self):
        self.x=self.front.x
        self.y=self.front.y
class Head:
    def __init__(self,direction,x,y):
        self.direction=direction
        self.x=x
        self.y=y
    def move(self):
        if self.direction==0:
            self.x+=1
        elif self.direction==1:
            self.y+=1
        elif self.direction==2:
            self.x-=1
        elif self.direction==3:
            self.y-=1
cell_size=20
board_size=30
speed=7
growth=1
grow=0
# image=cv2.resize(image,(board_size,board_size))
eaten=True
quit=False
snake=[]
image=cv2.resize(image,(board_size,board_size))
head=Head(0,int((board_size-1)/2),int((board_size-1)/2))
snake.append(head)

board=np.zeros([board_size*cell_size,board_size*cell_size,3])
cv2.imshow("Snake Game",board)
cv2.waitKey(2000)
apple_x=0
apple_y=0
while True:
    if eaten:
        s=list(range(0,board_size**2))
        for i in snake:
            s.remove(i.x*board_size+i.y)
        a=choice(s)
        apple_x=int(a/board_size)
        apple_y=a%board_size
        eaten=False
    board=np.zeros([board_size,board_size,3])
    for i in snake:
        board[i.y,i.x]=[255,255,0]
    board[apple_y,apple_x]=[255,0,0]
    # cv2.putText(board,"Score",(),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
    cv2.imshow("Snake Game",np.uint8(board.repeat(cell_size,0).repeat(cell_size,1)))
    key=cv2.waitKey(int(1000/speed))
    if key==27 or key==8:
        break
    elif key==ord("d"):
        head.direction=0
    elif key==ord("w"):
        head.direction=3
    elif key==ord("a"):
        head.direction=2
    elif key==ord("s"):
        head.direction=1
    for i in snake[::-1]:
        i.move()
    if head.x<0 or head.y<0 or head.x>board_size-1 or head.y>board_size-1:
        break
    for i in snake[1:]:
        if head.x==i.x and head.y==i.y:
            quit=True
            break
    if quit:
        break
    if grow>0:
        snake.append(Snake(snake[-1],subx,suby))
        grow-=1
    if apple_x==head.x and apple_y==head.y:
        subx=snake[-1].x
        suby=snake[-1].y
        eaten=True
        grow+=growth
    print(f"Score={len(snake)-1}")
