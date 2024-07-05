import pygame


class Player(pygame.sprite.Sprite):

  def __init__(self, scale, pos, screenSize):
    #Load the image
    image = pygame.image.load("Player.png")
    self.screenSize = screenSize
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

  def move(self, directionX, directionY):
    
    self.rect.x += directionX
    self.rect.y += directionY
    
    #if (self.rect.x >= self.screenSize[0]):
    #  self.rect.right = 0
