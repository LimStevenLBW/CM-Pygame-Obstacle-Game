import pygame
import random

class Enemy(pygame.sprite.Sprite):
  
  def __init__(self, scale, pos, screen):
    #0 means that it is idle
    #1 wind up
    #2 charge attack

    self.state = 0
    self.stateCurrentTime = 0
    self.stateNextTime = 100
    
    #Load the image
    image = pygame.image.load("enemies/Dog.png")
    
    pygame.sprite.Sprite.__init__(self)
    
    width = image.get_width()
    height = image.get_width()

    scaled_width = int(width * scale)
    scaled_height = int(height * scale)
    self.image = pygame.transform.scale(image, (scaled_width, scaled_height))
    self.rect = self.image.get_rect()
    self.rect.scale_by_ip(0.5,0.5)
    #Sets the starting position 
    self.rect.center = pos
    self.screen = screen


  def stateCheck(self):
    self.stateCurrentTime += 1
    if(self.stateCurrentTime >= self.stateNextTime):
      self.state += 1
      self.stateCurrentTime = 0

    if(self.state > 2):
      self.state = 0
    if(self.state == 1): 
      self.stateNextTime = 50
      self.windup()
    elif(self.state == 2):
      self.stateNextTime = 200
      self.chargeAttack()
  
  def windup(self):
     self.rect.x += 1
  
  def chargeAttack(self):
    self.rect.x -= 10

    if(self.rect.x < -50):
      self.rect.x = self.screen.get_width()
      self.rect.y = random.randint(0, self.screen.get_height() - 50)

    

 

    