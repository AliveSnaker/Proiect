import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

