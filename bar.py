##nathan hinton
##This file will have a bar graph for use in the chickens program

import pygame

class Bar:
    def __init__(self, x, y, width, height, screen, value = 50, valueMin = 0, valueMax = 100, color = (175, 0, 0), border = True, v = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.value = value
        self.valueMin = valueMin
        self.valueMax = valueMax
        self.color = color
        self.border = border
        self.v = v
        #Set up the rects:
        self.update()

    def update(self, x = None, y = None, value = None):
        # Do some error / input checking:
        if x != None: self.x = x
        if y != None: self.y = y
        if value != None: self.value = value
        if self.value < self.valueMin: self.value = self.valueMin
        if self.value > self.valueMax: self.value = self.valueMax
         #Update the rects:
        self.borderRect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.valueRect = pygame.rect.Rect(self.x, self.y, (self.value/(self.valueMax-self.valueMin))*self.width, self.height)

        if self.v: print(self.borderRect)
        if self.v: print(self.valueRect)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.valueRect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.borderRect, 1)
