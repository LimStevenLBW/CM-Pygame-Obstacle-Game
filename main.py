import pygame, sys
from text import Text
from enemy import Enemy
from player import Player
from pygame.locals import QUIT

pygame.init()
width = 400
height = 250
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Hello World!')

#Parameters
#Screen, Color, Rect(x, y, w, h)


color = (255, 255, 255)
bg = (43, 0, 0)
black = (0,0, 0)
rect = (0, height * .85, width, height/7)

health = Text(screen, "Hello", 28, black, 82, height*.85)
currentHp = 100
maxHp = 100

#Enemy Positions
enemyFrontPos = (width*.70, height/2)
enemyBackPos = (200, 50)
enemyBackPosLeft = (200, 50)
enemyBackPosRight = (200, 50)

dogEnemy = Enemy(0.2, enemyFrontPos, screen)

enemyGroup = pygame.sprite.Group()
enemyGroup.add(dogEnemy)
#enemyGroup.empty()

me = Player(0.15, (width/5,height/2), (width, height))
playerGroup = pygame.sprite.Group()
playerGroup.add(me)

#Control Section
left = False
right = False
up = False
down = False
speed = 5

while True:
    directionX = 0
    directionY = 0
    if(left): directionX -= speed
    if(right): directionX += speed
    if(up): directionY -= speed
    if(down): directionY += speed
    healthText = str(currentHp) + "/" + str(maxHp) + " HP"
    health.draw()

    #currentHp -= 1

    #Checking for Collision
    isCollidingEnemy = me.rect.colliderect(dogEnemy.rect)

    if(isCollidingEnemy):
        currentHp -= 1

    if(currentHp <= 0):
        print("You're dead")

    
    health.update(healthText)
    #Last part of loop
    
    for event in pygame.event.get():
        keys = pygame.key.get_pressed() 
        left = bool(keys[pygame.K_LEFT]) or bool(keys[pygame.K_a])
        right = bool(keys[pygame.K_RIGHT]) or bool(keys[pygame.K_d])
        up = bool(keys[pygame.K_UP]) or bool(keys[pygame.K_w])
        down = bool(keys[pygame.K_DOWN]) or bool(keys[pygame.K_s])
        
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
        
    pygame.display.update()
    screen.fill(bg)

    dogEnemy.stateCheck()
    enemyGroup.draw(screen)
    playerGroup.draw(screen)
    me.move(directionX, directionY)
    bottomBorder = pygame.draw.rect(screen, color, rect)

    clock.tick(30)