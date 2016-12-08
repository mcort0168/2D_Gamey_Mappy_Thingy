
import pygame
import sys
from pygame.locals import *
pygame.init()
black = (0,0,0)
w = 300
h = 300
screen = pygame.display.set_mode((w, h))
screen.fill((black))
gameloop = True
x = 0
y = 0
sand = pygame.image.load('Terrain/sand.png')
wall = pygame.image.load('Terrain/wall.png')
dirt = pygame.image.load('Terrain/dirt.png')
grass = pygame.image.load('Terrain/grass.png')
snow = pygame.image.load('Terrain/snow.png')
cement = pygame.image.load('Terrain/sidewalk.png')
empty = pygame.image.load('Terrain/empty.png')
file = open('TerrainTest.txt','r')

def pixel_converter(file_name, x, y):
    for line in file:
        letter = line.split(',')
        for word in letter:     
            if  word == 's':
                screen.blit(sand,(x,y))
                pygame.display.flip()
                x+=16
            elif  word == 'w':
                screen.blit(wall,(x,y))
                pygame.display.flip()
                x+=16
            elif  word == 'n':
                screen.blit(snow,(x,y))
                pygame.display.flip()
                x+=16
            elif  word == 'g':
                screen.blit(grass,(x,y))
                pygame.display.flip()
                x+=16
            elif  word == 'd':
                screen.blit(dirt,(x,y))
                pygame.display.flip()
                x+=16
            elif  word == 'c':
                screen.blit(cement,(x,y))
                pygame.display.flip()
                x+=16
            elif word == 'x':
                screen.blit(empty,(x,y))
                pygame.display.flip()
                x+= 16                            
            else:
                x = 0
                y+= 16
            

while gameloop:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameloop = False
        pixel_converter(file, x, y)
pygame.quit()
