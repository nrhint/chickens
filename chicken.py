##Nathan Hinton
##This file will have all of the parts for the chickens

import pygame
from random import randint
from bar import Bar

vv = False

EGG_LAIED = pygame.USEREVENT+1
eggLaied = pygame.event.Event(EGG_LAIED, message="Egg!")


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
        self.foodBar = Bar(self.x, self.y, 100, 8, self.screen, color = (150, 150, 0))
        self.hydration = 50 #Range of 0-100
        self.hydrationBar = Bar(self.x, self.y+10, 100, 8, self.screen, color = (100, 100, 200))
        self.foodMax = 100
        self.hydrationMax = 100
        self.moving = False
        self.speed = 1
        self.targetPos = (self.x, self.y)
        
        self.v = v #verbose output
        if self.v: print(self.rect)

    def eat(self, foodItem = None):
        if foodItem is not None:
            if self.v: print("Giving %s to chicken %s"%(foodItem, self))
            if foodItem == 'basic':
                self.food += 5
            else:
                print("Invalid food (%s) given to chicken (%s)."%(self, foodItem))
        if self.food > self.foodMax: self.food = self.foodMax
        if self.v: self.status()
            
    def drink(self, drinkItem = None):
        if drinkItem is not None:
            if self.v: print("Giving %s to chicken %s"%(drinkItem, self))
            if drinkItem == 'water':
                self.hydration += 5
            else:
                print("Invalid hydrate (%s) given to chicken (%s)."%(drinkItem, self))
        if self.hydration > self.hydrationMax: self.hydration = self.hydrationMax
        if self.v: self.status()

    def hunger(self, chance = 4, amount = 1):
        if randint(0, 1000) < chance:
            self.food -= amount
            if vv:print("%s got hungry"%self)
        if self.v: self.status()

    def thirst(self, chance = 4, amount = 1):
        if randint(0, 1000) < chance:
            self.hydration -= amount
            if vv:print("%s got thirsty"%self)
        if self.v: self.status()

    def status(self):
        print()
        print("Status of chicken: %s"%self)
        print("Food level: %s"%self.food)
        print("Hydration level: %s"%self.hydration)

    def move(self):
        if not self.moving:
            if randint(0, 1000) < (self.food+self.hydration)/16:
                self.moving = True
                self.targetPos = (randint(50, 300), randint(50, 500))
                #print("Moving to (%s, %s)"%self.targetPos)
        else:
            if self.x > self.targetPos[0]:
                self.x -= self.speed
            elif self.x < self.targetPos[0]:
                self.x += self.speed
            if self.y > self.targetPos[1]:
                self.y -= self.speed
            elif self.y < self.targetPos[1]:
                self.y += self.speed
            if (self.x, self.y) == self.targetPos:
                self.moving = False
                pygame.event.post(eggLaied)
                #print("Finished moving")

    def update(self):
        self.hunger()
        self.thirst()
        self.move()
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
        self.foodBar.update(x = self.x, y = self.y, value = self.food)
        self.hydrationBar.update(x = self.x, y = self.y+8, value = self.hydration)
        if vv: pygame.draw.rect(self.screen, (200, 0, 0), self.rect, 1)
        return False

    def draw(self):
        self.foodBar.draw()
        self.hydrationBar.draw()
        self.screen.blit(self.image, (self.x, self.y))

    def input(self, mouseState, other = False): ##This will check if the chicken is clicked on.
        if self.v: print(mouseState)
        if mouseState == 1: # chicken is clicked
            if randint(1, 2) == 1: self.eat('basic')
            else: self.drink("water")
        if mouseState == 4: #The left button is clicked:
            self.eat('basic')
        elif mouseState == 5: #The right button is clicked:
            self.drink('water')
        else:
            print("Invalid click value on chicken %s"%self)
