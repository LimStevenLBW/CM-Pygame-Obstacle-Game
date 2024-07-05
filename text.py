import pygame

class Text():
  #Constructor initialize the class
  def __init__(self, screen, text, size, color, x, y):
    
    self.screen = screen
    self.text = text
    self.size = size
    font_name = pygame.font.match_font("arial")
    self.font = pygame.font.Font(font_name, self.size)
    self.color = color
    self.x = x
    self.y = y


  def update(self, text):
    self.text = text
    
  def draw(self):
    pygame.font.init()
    text_surface = self.font.render(self.text, True, self.color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (self.x, self.y)
    self.screen.blit(text_surface, text_rect)
    