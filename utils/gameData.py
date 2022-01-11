##Nathan Hinton
##This class will contain all of the game data variables that are needed by things to run

from chicken import *
from egg import *
from utils.loadSave import saveData, loadData

class GameData:
    def __init__(self, screen, chickenImage, gameQueue):
        #Open the save file and import the vars:
        self.result = loadData('save.dat', screen, chickenImage, gameQueue)
        #print(self.result)
        if self.result == []: #No chickens were found:
            print("No chickens found")
            ##Setup the objects lists:

            ##Chickens:
            self.eggs = 0
            self.speedLevel = 1
            self.FPS = 30
            self.spawnRate = 3
            self.chickens = []
            self.foodCost = 0.5
            self.hydrationCost = 0.5
            self.drawChickens = 1
            self.feeder = 0
            self.hydrator = 0
            for x in range(0, 1):
                self.chickens.append(Chicken(screen, chickenImage, gameQueue, self, x = 50, y = 50, v = vv))
        else:
            self.eggs = self.result[1][0]
            self.speedLevel = self.result[1][1]
            self.FPS = self.result[1][2]
            self.spawnRate = self.result[1][3]
            self.foodCost = self.result[1][4]
            self.hydrationCost = self.result[1][5]
            self.feeder = self.result[1][6]
            self.hydrator = self.result[1][7]
            self.drawChickens = 1
            self.chickens = self.result[0]
            for chicken in self.chickens:
                chicken.gameData = self
    def saveState(self):
        stats = [self.eggs, self.speedLevel, self.FPS, self.spawnRate, self.foodCost, self.hydrationCost, self.drawChickens, self.feeder, self.hydrator]
        saveData('save.dat', self.chickens, stats)

        
