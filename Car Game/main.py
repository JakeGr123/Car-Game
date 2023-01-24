import pygame
import time
import math
import os
from pygame.locals import *
from utils import scale_image, blit_rotate_center, blit_rotate_center1


GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load('imgs/track.png'), 0.9)


TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

FINISH = pygame.image.load("imgs/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITION = (130, 250)

RED_CAR = scale_image(pygame.image.load("imgs/pink car.png"), 0.75)
GREEN_CAR = scale_image(pygame.image.load("imgs/orange car.png"), 0.75)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

FPS = 120

class AbstractCar:

    def __init__(self, max_vel, rotation_vel):
        self.img= self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.25

        
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal


    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi
    
    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0

class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (140, 190)
    
    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()
    def bounce(self):
        self.vel = - self.vel 
        self.move()



            

def draw(win, images, player_car, player_car1):
    for img, pos in images:
        win.blit(img, pos)
    player_car1.draw1(win)
    player_car.draw(win)
    pygame.display.update()

def move_player(player_car):
        
    keys = pygame.key.get_pressed()
    moved = False
    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward() 
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward() 

    if not moved:
        player_car.reduce_speed()









class AbstractCar1:

    def __init__(self, max_vel1, rotation_vel1):
        self.img1= self.IMG1
        self.max_vel1 = max_vel1
        self.vel1 = 0
        self.rotation_vel1 = rotation_vel1
        self.angle1 = 0
        self.x1, self.y1 = self.START_POS1
        self.acceleration1 = 0.25

        
    def rotate1(self, left=False, right=False):
        if left:
            self.angle1 += self.rotation_vel1
        elif right:
            self.angle1 -= self.rotation_vel1

    def draw1(self, win1):
        blit_rotate_center1(win1, self.img1, (self.x1, self.y1), self.angle1)

    def move_forward1(self):
        self.vel1 = min(self.vel1 + self.acceleration1, self.max_vel1)
        self.move1()

    def move_backward1(self):
        self.vel1 = max(self.vel1 - self.acceleration1, -self.max_vel1/2)
        self.move1()

    def move1(self):
        radians = math.radians(self.angle1)
        vertical = math.cos(radians) * self.vel1
        horizontal = math.sin(radians) * self.vel1

        self.y1 -= vertical
        self.x1 -= horizontal


    def collide1(self, mask, x1=0, y1=0):
        car_mask1 = pygame.mask.from_surface(self.img1)
        offset1 = (int(self.x1 - x1), int(self.y1 - y1))
        poi1 = mask.overlap(car_mask1, offset1)
        return poi1
    
    def reset1(self):
        self.x1, self.y1 = self.START_POS1
        self.angle1 = 0
        self.vel1 = 0

class PlayerCar1(AbstractCar1):
    IMG1 = GREEN_CAR
    START_POS1 = (120, 190)
    
    def reduce_speed1(self):
        self.vel1 = max(self.vel1 - self.acceleration1 / 2, 0)
        self.move1()
    def bounce1(self):
        self.vel1 = - self.vel1
        self.move1()




 

def move_player1(player_car1):
    
    keys1 = pygame.key.get_pressed()
    moved1 = False
    if keys1[pygame.K_LEFT]:
        player_car1.rotate1(left=True)
    if keys1[pygame.K_RIGHT]:
        player_car1.rotate1(right=True)
    if keys1[pygame.K_UP]:
        moved1 = True
        player_car1.move_forward1() 
    if keys1[pygame.K_DOWN]:
        moved1 = True
        player_car1.move_backward1() 

    if not moved1:
        player_car1.reduce_speed1()




run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
player_car = PlayerCar(4, 4)
player_car1 = PlayerCar1(4, 4)
while run:
    clock.tick(FPS)
    
    draw(WIN, images, player_car, player_car1 )
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    move_player(player_car)

    move_player1(player_car1)


    if player_car.collide(TRACK_BORDER_MASK) != None:
        player_car.bounce()
        

    finish_poi_collide = player_car.collide(FINISH_MASK, *FINISH_POSITION)
    if finish_poi_collide != None:
        if finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            player_car.reset()
            print('finish')



    if player_car1.collide1(TRACK_BORDER_MASK) != None:
        player_car1.bounce1()

    finish_poi_collide = player_car1.collide1(FINISH_MASK, *FINISH_POSITION)
    if finish_poi_collide != None:
        if finish_poi_collide[1] == 0:
            player_car1.bounce1()
        else:
            player_car1.reset1()
            print('finish')




        


pygame.quit()