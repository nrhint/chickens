##Nathan Hinton
##This file will have all of the parts for the chickens

from random import randint

vv = True

class Chicken:
    def __init__(self, image, x = 0, y = 0, v = False):
        self.food = 50 #Range of 0-100
        self.hydration = 50 #Range of 0-100
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.move(x, y)
        self.x = x
        self.y = y
        self.v = v #verbose output

    def eat(self, foodItem = None):
        if foodItem is not None:
            if self.v: print("Giving %s to chicken %s"%(foodItem, self))
            if foodItem == 'basic':
                self.food += 1
            else:
                print("Invalid food (%s) given to chicken (%s)."%(self, foodItem))
        if self.v: self.status()
            
    def drink(self, drinkItem = None):
        if drinkItem is not None:
            if self.v: print("Giving %s to chicken %s"%(drinkItem, self))
            if drinkItem == 'water':
                self.hydration += 1
            else:
                print("Invalid hydrate (%s) given to chicken (%s)."%(drinkItem, self))
        if self.v: self.status()

    def hunger(self, chance = 3, amount = 2):
        if randint(0, 100) < chance:
            self.food -= amount
            if vv:print("%s got hungry"%self)
        if self.v: self.status()

    def thirst(self, chance = 3, amount = 2):
        if randint(0, 100) < chance:
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
            if self.v or vv: print("Chicken %s died from hunger..."%self)
            if self.v or vv: self.status()
            return True
        if self.hydration <= 0:
            if self.v or vv: print("Chicken %s died from thirst..."%self)
            if self.v or vv: self.status()
            return True
        #if self.v: self.status()
        return False

    def input(self, mouseState): ##This will check if the chicken is clicked on.
        if self.v: print(mouseState)
        if mouseState == 1: #The left button is clicked:
            self.eat('basic')
        elif mouseState == 3: #The right button is clicked:
            self.drink('water')
        else:
            print("Invalid click value on chicken %s"%self)
