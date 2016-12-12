
import pygame
import os
import sys
#from pygame.locals import *
pygame.init()
black = (0,0,0)
#Variables for screen size
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
screen.fill((black))
#variable to keep the game running and the screen open until False
gameloop = True

clock = pygame.time.Clock()
#lists to hold values for certain pixel locations
ground = []
grass = []
snow = []
dirt = []
cement = []
sand = []
monsters = []


walls = [] #list to hold walls for collision detection

#Help define the x y coordinates of the top left corner
#of the pixel being drawn
x = 0
y = 0
#help define the size of the pixel and how much to move
#the pixel converter to draw
pixel_x = 16
pixel_y = 16

UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

#varaibles for loading items
hero = pygame.image.load('Hero/Hero1.png').convert_alpha()
monster = pygame.image.load('Enemy/Enemy1.png').convert_alpha()
file = open('TerrainTest.txt','r')


##classes for listing the rectangular objects of each pixel so they can be
##easily grouped and reclassified
class WALL(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        walls.append(self)
        self.image = pygame.image.load('Terrain/wall.png')
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
class GROUND(pygame.sprite.Sprite):
    def __init__(self, x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        ground.append(self)
        self.image = pygame.image.load('Terrain/dirt.png')
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class CEMENT(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        cement.append(self)
        self.image = pygame.image.load('Terrain/cement.png')
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class GRASS(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        grass.append(self)
        self.image = pygame.image.load('Terrain/grass.png')
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class SAND(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        sand.append(self)
        self.image = pygame.image.load('Terrain/sand.png')
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class SNOW(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        snow.append(self)
        self.image = pygame.image.load('Terrain/snow.png')
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class Monster(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = monster
        self.health = 20
        self.damage = 2
        monsters.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

    def alive(self):
        if self.health < 0:
            return False
        else:
            return True

        
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
monster_list = pygame.sprite.Group()
spritex = 16
spritey = 16
def pixel_converter(file_name, x, y):
    """Function that actually calls converts the pixels using the given file
    and the x,y coordinates it should begin drawing.

    IMPORTANT NOTE: The X,Y Coordinates are for the top left corner of the pixel
    and will be drawn from that point down.
    """
    ##this first for loop actually takes in the already opened and read file and
    ##seperates it according to the defined variable
    for line in file_name:
        letter = line.split(',')
        ##thie for loop cycles through every elemnt in the split file and tells
        ##pygame what to import for each letter and where to place it in the new screen
        for word in letter:     
            if  word == 's':
                all_sprite_list.add(SAND(x, y, spritex, spritey))
                pygame.display.flip()
                x+= pixel_x
            elif  word == 'w':
                wall_list.add(WALL((x, y)))
                all_sprite_list.add(WALL((x, y)))
                pygame.display.flip()
                x+= pixel_x
            elif  word == 'n':
                all_sprite_list.add(SNOW(x, y, spritex, spritey))
                pygame.display.flip()
                x+= pixel_x
            elif  word == 'g':
                all_sprite_list.add(GRASS(x, y, spritex, spritey))
                pygame.display.flip()
                x+= pixel_x
            elif  word == 'd':
                all_sprite_list.add(GROUND(x, y, spritex, spritey))
                pygame.display.flip()
                x+= pixel_x
            elif  word == 'c':
                all_sprite_list.add(CEMENT(x, y, spritex, spritey))
                pygame.display.flip()
                x+= pixel_x
            elif word == 'x':
                pygame.display.flip()
                x+= pixel_x
            elif word == 'm':
                mx = x - 16
                
                monster_list.add(Monster((mx,y)))
                pygame.display.flip()
                x += 0
            else:
                x = 0
                y+= pixel_y




class Player(object):
    """Object defining the player and aspects of the player such as movement
    attacking and health
    """
    def __init__(self):
        self.image = hero
        self.rect = pygame.Rect(16, 16, 16, 16)
        self.health = 50
        
        
    ##attack function for what to do when player makes contact with a monster
    def attack(self, dx, dy):
        damage = 5
        screen.blit(textsurface, (0,0))
        for monster in monster_list:
            if self.rect.colliderect(monster.rect):
                self.health -= monster.damage
                
                if dx > 0: #attack from the right
                    self.rect.right = monster.rect.left
                    if self.rect.right == monster.rect.left:
                        monster.health -= damage
                        if not monster.alive():
                            monster_list.remove(monster)
                        monster_list.update()
                        
                elif dx < 0: #attack from the left
                    self.rect.left = monster.rect.right
                    if self.rect.left == monster.rect.right:
                        monster.health -= damage
                        if not monster.alive():
                            monster_list.remove(monster)
                        monster_list.update()
                    
                if dy > 0: #attack from above
                    self.rect.bottom = monster.rect.top
                    if self.rect.bottom == monster.rect.top:
                        monster.health -= damage
                        if not monster.alive():
                            monster_list.remove(monster)
                        monster_list.update()
                    
                elif dy < 0: #attack from below
                    self.rect.top = monster.rect.bottom
                    if self.rect.top == monster.rect.bottom:
                        monster.health -= damage
                        if not monster.alive():
                            monster_list.remove(monster)
                        monster_list.update()

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
            self.attack(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
            self.attack(0, dy)
            
    def alive(self):
        if self.health <= 0:
            False
        else:
            True
            
    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        ##wall collision detection
        for wall in wall_list:
            if self.rect.colliderect(wall.rect):
                if dx > 0: #move right
                    self.rect.right = wall.rect.left
                elif dx < 0: #move left
                    self.rect.left = wall.rect.right
                    
                if dy > 0: #move down
                    self.rect.bottom = wall.rect.top
                    
                elif dy < 0: #move up
                    self.rect.top = wall.rect.bottom



player = Player()

background = pixel_converter(file, x, y)
##runs the function and keeps the pygame window open until told otherwise
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        
    ##draws all sprites in the list from pixel converter into actual pixels
    all_sprite_list.draw(screen)
    ##and then runs everything else on top of that background
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
        player.image = pygame.image.load('Hero/Hero2.png')
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
        player.image = pygame.image.load('Hero/Hero4.png')
    if key[pygame.K_UP]:
        player.move(0, -2)
        player.image = pygame.image.load('Hero/Hero3.png')
    if key[pygame.K_DOWN]:
        player.move(0, 2)
        player.image = pygame.image.load('Hero/Hero1.png')
    pixel_converter(file, x, y)
    wall_list.update()
    all_sprite_list.update()
    monster_list.update()
    monster_list.draw(screen)
    ##draws the player, very important
    screen.blit(player.image, (player.rect))
    myfont = pygame.font.SysFont('Comic Sans MS', 12)
    #loop to check players health and what to print
    if player.health > 0:
        textsurface = myfont.render("you have "+str(player.health)+" health left.", False, (255, 255, 255))
    else:
        textsurface = myfont.render("You Died!", False, (255, 255, 255))
        print "You died, Try again!"
        gameloop = False
    screen.blit(textsurface, (0,0))    
    pygame.init()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(80)
    screen.fill(black)
pygame.quit()
