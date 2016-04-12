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
poly_scale = 10;
poly = [
        (1,0),
        (0,1/3.0),
        (0,-1/3.0),
        (1,0)
        ]

def rotate((x,y),a):
    return (x*cos(a)-y*sin(a), x*sin(a)+y*cos(a))

def sign(x):
    if(x < 0):
        return -1
    else:
        return 1

def normalize((x,y)):
    magn = sqrt(x**2 + y**2)
    return (x/magn,y/magn)

def computeAngle((dx,dy)):
    angle = atan(dy/dx)
    if (dx < 0):
      angle += pi
    return angle

def makeBoidPolly((pos,vel)):
    (x,y) = pos
    (dx,dy) = normalize(vel)
    angle = computeAngle((dx,dy)) 
    rotated = map(lambda c : rotate(c,angle),poly)
    offsetted = map(lambda (xx,yy) : ((x+xx*poly_scale),(y+yy*poly_scale)),rotated)
    return offsetted

def drawBoid(((x,y),(vx,vy)),index):

        pygame.draw.lines(
                screen, index,False, makeBoidPolly(((x,y),(vx,vy))),1)

def clearBoid(((x,y),(vx,vy))):

    pygame.draw.lines(
            screen, BLACK,True, makeBoidPolly(((x,y),(vx,vy))),1)

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
    counter = 0
    while 1:
        if line != "":
            if(len(line.split(",")) == 5):
                (index,data) = buidBoid(line)
                if index in boids:
                    clearBoid(boids[index])
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
        pygame.time.delay(0)
        counter += 1;

