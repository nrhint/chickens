##Nathan Hinton
##This file will contain the code for running the window.

import pygame
from random import randint

from chicken import *
from button import Button
from text import Text
from gameData import GameData

v = True
vv = False

pygame.init()
font = pygame.font.Font(None, 36)


width=450
height=600
screen = pygame.display.set_mode( (width, height ) )
pygame.display.set_caption('feed my chicken(s)')

#colors:
BACKGROUND_GREEN = (65, 132, 18)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#FPS stuff
fpsClock = pygame.time.Clock()
fpsText = Text(screen, font, "loading...", BLACK, (50, 10))

##Load the images. This may be moved to another file later on
chickenImage = pygame.image.load("images/chicken.png")

## Try to load from the save file:
gameData = GameData(screen, chickenImage)

chickenCount = Text(screen, font, "loading...", BLACK, (200, 10))
eggCount = Text(screen, font, "loading...", BLACK, (100, 580))

def costFormula(num):
    return int((num+1)*1.5)

##Buttons:
buttons = []
buttons.append(Button(400, 580, screen, font, "store", BLUE, BLACK, "store"))

menuItems = []
menuItems.append(Text(screen, font, "Add speed: ", RED, (125, 50), active = False))
menuItems.append(Button(350, 50, screen, font, "%s eggs"%costFormula(gameData.speedLevel), BLACK, RED, "remove %s"%costFormula(gameData.speedLevel), active = False, action2 = "addSpeed"))

menuItems.append(Text(screen, font, "Increase food: ", RED, (125, 100), active = False))
menuItems.append(Button(350, 100, screen, font, "%s eggs"%costFormula(gameData.chickens[0].foodMax/8), BLACK, RED, "remove %s"%costFormula(gameData.chickens[0].foodMax/8), active = False, action2 = "addFood"))

menuItems.append(Text(screen, font, "Increase Hydration: ", RED, (125, 150), active = False))
menuItems.append(Button(350, 150, screen, font, "%s eggs"%costFormula(gameData.chickens[0].hydrationMax/8), BLACK, RED, "remove %s"%costFormula(gameData.chickens[0].hydrationMax/8), active = False, action2 = "addHydration"))

menuItems.append(Text(screen, font, "Increase spawn: ", RED, (125, 200), active = False))
menuItems.append(Button(350, 200, screen, font, "%s eggs"%costFormula(gameData.spawnRate), BLACK, RED, "remove %s"%costFormula(gameData.spawnRate), active = False, action2 = "addSpawn"))

menuItems.append(Text(screen, font, "Decrease food cost: ", RED, (125, 250), active = False))
menuItems.append(Button(350, 250, screen, font, "%s eggs"%costFormula(1/gameData.foodCost), BLACK, RED, "remove %s"%costFormula(1/gameData.foodCost), active = False, action2 = "reduceFoodCost"))

menuItems.append(Text(screen, font, "Decrease Hydration cost: ", RED, (125, 300), active = False))
menuItems.append(Button(350, 300, screen, font, "%s eggs"%costFormula(1/gameData.hydrationCost), BLACK, RED, "remove %s"%costFormula(1/gameData.hydrationCost), active = False, action2 = "reduceHydrationCost"))

menuItems.append(Text(screen, font, "Upgrade feeder: ", RED, (125, 350), active = False))
menuItems.append(Button(350, 350, screen, font, "%s eggs"%(costFormula(gameData.feeder)+50), BLACK, RED, "remove %s"%(costFormula(gameData.feeder)+50), active = False, action2 = "upgradeFeeder"))

menuItems.append(Text(screen, font, "Upgrade waterer: ", RED, (125, 400), active = False))
menuItems.append(Button(350, 400, screen, font, "%s eggs"%(costFormula(gameData.hydrator)+50), BLACK, RED, "remove %s"%(costFormula(gameData.hydrator)+50), active = False, action2 = "upgradeHydrater"))


buttons.append(Button(400, 540, screen, font, "settings", BLUE, BLACK, "settings"))

settingItems = []
settingItems.append(Button(350, 50, screen, font, "Hide chickens", BLACK, RED, "hideChickens", active = False, action2 = ""))


screen.fill(BACKGROUND_GREEN)
pygame.display.flip()

frameCount = 0
state = "game" ## Posible states are: [game, store]
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            for chicken in gameData.chickens:
                if chicken.rect.collidepoint(x, y):
                    if vv: print('clicked on chicken')
                    chicken.input(event.button)
            for button in buttons:
                if button.rect.collidepoint(x, y):
                    if vv: print('Clicked on button')
                    if vv: print(button.action)
                    if button.action == 'store':
                        button.text = 'game'
                        button.action = 'game'
                        state = 'store'
                        for item in menuItems:
                            item.active = not item.active
                            if vv: print(item.active)
                    elif button.action == 'game':
                        button.text = 'store'
                        button.action = 'store'
                        state = 'game'
                        for item in menuItems:
                            item.active = not item.active
                            if vv: print(item.active)
                    elif button.action == 'settings':
                        button.text = 'back'
                        button.action = 'back'
                        state = 'settings'
                        for item in settingItems:
                            item.active = not item.active
                            if vv: print(item.active)
                    elif button.action == 'back':
                        button.text = 'settings'
                        button.action = 'settings'
                        state = 'game'
                        for item in settingItems:
                            item.active = not item.active
                            if vv: print(item.active)
            if state == 'store':
                for item in menuItems:
                    if item.rect.collidepoint(x, y):
                        try:
                            #print('cost button clicked')
                            num = int(item.action.replace('remove ', ''))
                            if gameData.eggs - num >= 0:
                                gameData.eggs -= num
                                print("You spent %s eggs"%num)
                                item.text = "%s eggs"%costFormula(num)
                                item.action = "remove %s"%costFormula(num)
                                if item.action2 == 'addSpeed':
                                    gameData.speedLevel = int(num)
                                    for chicken in gameData.chickens:
                                        chicken.speed += 1
                                elif item.action2 == 'addFood':
#                                   #gameData.speedLevel = int(num)
                                    for chicken in gameData.chickens:
                                        chicken.foodMax += int(chicken.foodMax/10)
                                        chicken.foodBar.valueMax = chicken.foodMax
                                elif item.action2 == 'addHydration':
#                                   #gameData.speedLevel = int(num)
                                    for chicken in gameData.chickens:
                                        chicken.hydrationMax += int(chicken.hydrationMax/10)
                                        if vv: print(chicken.hydration, chicken.hydrationMax)
                                        chicken.hydrationBar.valueMax = chicken.hydrationMax
                                elif item.action2 == 'addSpawn':
                                    gameData.spawnRate = costFormula(gameData.spawnRate)
                                    print(gameData.spawnRate)
                                elif item.action2 == 'reduceFoodCost':
                                    gameData.foodCost = gameData.foodCost/1.25
                                elif item.action2 == 'reduceHydrationCost':
                                    gameData.hydrationCost = gameData.hydrationCost/1.25
                            else:
                                if vv: print("Not enough money")
                        except AttributeError:
                            pass
            elif state == 'settings':
                for item in settingItems:
                    if item.rect.collidepoint(x, y):
                        if item.text == "Hide chickens":
                            gameData.drawChickens = 0
                            print("Hiding chickens")
                            item.text = "Show chickens"
                        elif item.text == "Show chickens":
                            gameData.drawChickens = 1
                            item.text = "Hide chickens"
        if event.type == EGG_LAIED:
            gameData.eggs += 1
    #Spawn gameData.chickens
    if randint(0, 10000) < gameData.spawnRate and fpsClock.get_fps() > gameData.FPS-10:
        tmp = Chicken(screen, chickenImage, gameData, x = randint(50, 350), y = randint(50, 500), v = vv)
        tmp.speed = gameData.chickens[0].speed
        tmp.foodMax = gameData.chickens[0].foodMax
        tmp.hydrationMax = gameData.chickens[0].hydrationMax
        gameData.chickens.append(tmp)
    #add eggs when needed:
    if frameCount % 1800 == 0:
        gameData.eggs += len(gameData.chickens)
    ##Update screen:
    screen.fill(BACKGROUND_GREEN)

    #Depending on the state the chickens may or may not be drawn...
    if state == "game":
        for chicken in gameData.chickens:
            died = chicken.update()
            if died:
                gameData.chickens.remove(chicken)
                #print("Chicken %s died"%chicken)
            if gameData.drawChickens:
                chicken.draw()
            #screen.blit(chickenImage, (chicken.x, chicken.y))
    elif state == "store":
        for chicken in gameData.chickens:
            died = chicken.update()
            if died:
                gameData.chickens.remove(chicken)
        for item in menuItems:
            item.update()
            item.draw()
    elif state == "settings":
        for chicken in gameData.chickens:
            died = chicken.update()
            if died:
                gameData.chickens.remove(chicken)
        for item in settingItems:
            item.update()
            item.draw()
        
    else:
        print("INVALID STATE OF: %s RETURNING TO GAME"%state)
        state = "game"

    for button in buttons:
        button.update()
        button.draw()
    
    fpsText.draw()
    fpsText.update(f"{fpsClock.get_fps():2.0f} FPS")
    chickenCount.draw()
    chickenCount.update("%s chicken(s)"%len(gameData.chickens))
    eggCount.draw()
    eggCount.update("%s eggs"%round(gameData.eggs, 2))
    frameCount += 1
    pygame.display.flip()
    fpsClock.tick(gameData.FPS)

pygame.quit()
gameData.saveState()
