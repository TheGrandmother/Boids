import os, sys, pygame, fileinput
from pygame.locals import *
from math import pi,sqrt,sin,cos,asin,atan


WHITE = 255,255,255
GREEN = 0,255,0
BLACK = 0,0,0
BLUE  = 0,0,255
RED   = 255,0,0

vel_scale = 5
pos_scale = 1
pos_offs = 0

def normalize((x,y)):
    magn = sqrt(x**2 + y**2)
    return (x/magn,y/magn)

def drawBoid(((x,y),(vx,vy)),index):
        (cx,cy) = (x*pos_scale + pos_offs,y*pos_scale + pos_offs)
        (cvx,cvy) = normalize((vx,vy))
        (cvx,cvy) = (cx+cvx*10,cy+cvy*10)

        pygame.draw.aaline(
                screen, index, (cx,cy), 
                (cvx,cvy), 
                4)

def buidBoid(line):
    line = line.replace("\n","")
    splitted = line.split(",")        
    return (
            float(splitted[0]),
            (
                (float(splitted[1]),float(splitted[2])),
                (float(splitted[3]),float(splitted[4]))
            )
            )

if __name__ == "__main__":
    boids = {}
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("pygame.draw functions ~ examples")
    pygame.init()

    boid_file = open("test.txt","r");
    line = raw_input()
    while 1:
        if line != "":
            if(len(line.split(",")) == 5):
                (index,data) = buidBoid(line)
                if index in boids:
                    drawBoid(boids[index],BLACK)
                boids[index] = data
                drawBoid(data,WHITE)
        line = raw_input()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.display.quit()
                sys.exit(0)

        pygame.display.update() 
        pygame.time.delay(1)
