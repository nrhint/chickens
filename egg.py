##Nathan Hinton
##This will be an egg class that will either be collected, rot or hatch

import pygame
from random import randint

class Egg:
    def __init__(self, screen, queue, image, x, y, value, rotTime = 1800, hatchChance = 1):
        self.x = x
        self.y = y
        self.value = value
        self.image = pygame.transform.scale(image, (25, 25))
        self.rect = self.image.get_rect().move(self.x, self.y)
        self.screen = screen
        self.hatchChance = hatchChance
        self.rotTime = rotTime
        self.lifeTime = 0
        self.queue = queue

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
    def update(self):
        self.lifeTime += 1
        if self.lifeTime > self.rotTime:
            # print("Destroy egg...")
            self.queue.put(['destroyEgg', self])
        else:
            if randint(0, 100*self.rotTime) <= self.hatchChance:
                #print("Egg hatched!")
                self.queue.put(['eggHatched', self, self.x, self.y])

    def input(self): #The egg was clicked on...
        self.queue.put(['eggCollected', self, self.value])