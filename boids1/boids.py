import os, sys, pygame
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

poly = [
        (0,1),(2/3.0,-2/3.0),(0,1/3.0),(-2/3.0,-2/3.0),(0,1)
        ]

def normalize((x,y)):
    magn = sqrt(x**2+y**2)
    return (x/magn, y/magn)

def rotate((x,y),a):
    return (x*cos(a)-y*sin(a), x*sin(a)+y*cos(a))

def sign(x) :
	if x < 0:
		return -1
	else:
		return 1

def makeBoidPolly((pos,vel)):
    (x,y) = pos
    (dx,dy) = normalize(vel)
    angle = (asin(dx)-pi)
    scale = 10
    rotated = map(lambda c : rotate(c,angle),poly)
    offsetted = map(lambda (xx,yy) : ((x+xx*scale),(y+yy*scale)),rotated)
    return offsetted

def drawBoid((pos,vel),color):
    (x,y) = pos
    c_pos = (x*pos_scale + pos_offs,y*pos_scale + pos_offs)
    (cx,cy) = c_pos
    (vx,vy) = vel
    c_vel = (cx + vx*vel_scale,cy + vy*vel_scale)

    pygame.draw.polygon(
            screen, color,  makeBoidPolly((pos,vel)), 
            1)

def lameDraw(((x,y),(vx,vy)),index):
	(cx,cy) = (x*pos_scale + pos_offs,y*pos_scale + pos_offs)
	(cvx,cvy) = normalize((vx,vy))
	(cvx,cvy) = (cx+cvx*10,cy+cvy*10)
	pygame.draw.aaline(
	        screen, index, (cx,cy), 
	        (cvx,cvy), 
	        4)

def clearBoid((pos,vel)):
    (x,y) = pos
    c_pos = (x*pos_scale + pos_offs,y*pos_scale + pos_offs)
    (cx,cy) = c_pos
    (vx,vy) = vel
    c_vel = (cx + vx*vel_scale,cy + vy*vel_scale)

    pygame.draw.aaline(
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
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("pygame.draw functions ~ examples")
    pygame.init()

    boid_file = open("test.txt","r");
    line = boid_file.readline()
    while 1:
        if line != "":
						if(len(line.split(",")) == 5):
							(index,data) = buidBoid(line)
							if index in boids:
									#drawBoid(boids[index],BLACK)
									lameDraw(boids[index],BLACK)
							boids[index] = data
							lameDraw(data,WHITE)
							#drawBoid(data,WHITE)
        else:
					print "lol"
					quit()
        line = boid_file.readline()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.display.quit()
                sys.exit(0)
        pygame.display.update() 
        pygame.time.delay(1)
