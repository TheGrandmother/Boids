
import os, sys, pygame
from pygame.locals import *
from math import pi


WHITE = 255,255,255
GREEN = 0,255,0
BLACK = 0,0,0
BLUE  = 0,0,255
RED   = 255,0,0

vel_scale = 1
pos_scale = 1
pos_offs = 0


def drawBoid((pos,vel)):
    (x,y) = pos
    c_pos = (x*pos_scale + pos_offs,x*pos_scale + pos_offs)
    (cx,cy) = c_pos
    (vx,vy) = vel
    c_vel = (cx + vx*vel_scale,cy + vy*vel_scale)

    pygame.draw.line(
            screen, WHITE, c_pos, 
            c_vel, 
            1)

def clearBoid((pos,vel)):
    (x,y) = pos
    c_pos = (x*pos_scale + pos_offs,x*pos_scale + pos_offs)
    (cx,cy) = c_pos
    (vx,vy) = vel
    c_vel = (cx + vx*vel_scale,cy + vy*vel_scale)

    pygame.draw.line(
            screen, BLACK, c_pos, 
            c_vel, 
            1)

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
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("pygame.draw functions ~ examples")
    pygame.init()

    boid_file = open("test.txt","r");
    line = boid_file.readline()
    while 1:
        if line != "":
            (index,data) = buidBoid(line)
            if index in boids:
                clearBoid(boids[index])
            boids[index] = data
            drawBoid(data)
            
        line = boid_file.readline()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.display.quit()
                sys.exit(0)
        pygame.display.update() 
        pygame.time.delay(50)
