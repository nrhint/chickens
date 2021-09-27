##Nathan Hinton
##This file will have all of the parts for the chickens

import pygame
from random import randint
from bar import Bar

vv = False

class Chicken:
    def __init__(self, screen, image, x = 0, y = 0, v = False):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.screen = screen
        self.x = x
        self.y = y
        self.lastx = self.x
        self.lasty = self.y
        self.food = 50 #Range of 0-100
        self.foodBar = Bar(self.x, self.y, 100, 10, self.screen, color = (150, 150, 0))
        self.hydration = 50 #Range of 0-100
        self.hydrationBar = Bar(self.x, self.y+10, 100, 10, self.screen, color = (100, 100, 200))
        self.foodMax = 100
        self.hydrationMax = 100
        
        self.v = v #verbose output
        if self.v: print(self.rect)

    def eat(self, foodItem = None):
        if foodItem is not None:
            if self.v: print("Giving %s to chicken %s"%(foodItem, self))
            if foodItem == 'basic':
                self.food += 10
            else:
                print("Invalid food (%s) given to chicken (%s)."%(self, foodItem))
        if self.food > self.foodMax: self.food = self.foodMax
        if self.v: self.status()
            
    def drink(self, drinkItem = None):
        if drinkItem is not None:
            if self.v: print("Giving %s to chicken %s"%(drinkItem, self))
            if drinkItem == 'water':
                self.hydration += 10
            else:
                print("Invalid hydrate (%s) given to chicken (%s)."%(drinkItem, self))
        if self.hydration > self.hydrationMax: self.hydration = self.hydrationMax
        if self.v: self.status()

    def hunger(self, chance = 20, amount = 1):
        if randint(0, 1000) < chance:
            self.food -= amount
            if vv:print("%s got hungry"%self)
        if self.v: self.status()

    def thirst(self, chance = 20, amount = 1):
        if randint(0, 1000) < chance:
            self.hydration -= amount
            if vv:print("%s got thirsty"%self)
        if self.v: self.status()

    def status(self):
        print()
        print("Status of chicken: %s"%self)
        print("Food level: %s"%self.food)
        print("Hydration level: %s"%self.hydration)

    def update(self):
        self.hunger()
        self.thirst()
        if self.food <= 0:
            if self.v or vv or True: print("Chicken %s died from hunger..."%self)
            if self.v or vv: self.status()
            return True
        if self.hydration <= 0:
            if self.v or vv or True: print("Chicken %s died from thirst..."%self)
            if self.v or vv: self.status()
            return True
        #if self.v: self.status()
        self.rect = self.rect.move(self.x-self.lastx, self.y-self.lasty)
        self.lastx = self.x
        self.lasty = self.y
        self.foodBar.update(value = self.food)
        self.hydrationBar.update(value = self.hydration)
        if vv: pygame.draw.rect(self.screen, (200, 0, 0), self.rect, 1)
        return False

    def draw(self):
        self.foodBar.draw()
        self.hydrationBar.draw()
        self.screen.blit(self.image, (self.x, self.y))

    def input(self, mouseState): ##This will check if the chicken is clicked on.
        if self.v: print(mouseState)
        if mouseState == 4: #The left button is clicked:
            self.eat('basic')
        elif mouseState == 5: #The right button is clicked:
            self.drink('water')
        else:
            print("Invalid click value on chicken %s"%self)
