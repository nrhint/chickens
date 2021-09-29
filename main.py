##Nathan Hinton
##This file will contain the code for running the window.

import pygame
from random import randint

from chicken import *
from button import Button
from text import Text
from loadSave import saveData, loadData

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
FPS = 30
fpsClock = pygame.time.Clock()
fpsText = Text(screen, font, "loading...", BLACK, (50, 10))

##Load the images. This may be moved to another file later on
chickenImage = pygame.image.load("images/chicken.png")

## Try to load from the save file:
result = loadData('save.dat', screen, chickenImage)
if result == []: #No chickens were found:
    print("No chickens found")
    ##Setup the objects lists:

    ##Chickens:
    eggs = 0
    speedLevel = 1
    spawnRate = 3
    chickens = []
    for x in range(0, 1):
        chickens.append(Chicken(screen, chickenImage, x = 50, y = 50, v = vv))
else:
    eggs = result[1][0]
    speedLevel = result[1][1]
    FPS = result[1][2]
    spawnRate = result[1][3]
    chickens = result[0]
    

chickenCount = Text(screen, font, "loading...", BLACK, (200, 10))
eggCount = Text(screen, font, "loading...", BLACK, (100, 580))

def costFormula(num):
    return int((num+1)*1.5)

##Buttons:
buttons = []
buttons.append(Button(200, 580, screen, font, "store", BLUE, BLACK, "store"))

menuItems = []
menuItems.append(Text(screen, font, "Add speed: ", RED, (125, 50), active = False))
menuItems.append(Button(350, 50, screen, font, "%s eggs"%costFormula(speedLevel), BLACK, RED, "remove %s"%costFormula(speedLevel), active = False, action2 = "addSpeed"))

menuItems.append(Text(screen, font, "Increase food: ", RED, (125, 100), active = False))
menuItems.append(Button(350, 100, screen, font, "%s eggs"%costFormula(chickens[0].foodMax/8), BLACK, RED, "remove %s"%costFormula(chickens[0].foodMax/8), active = False, action2 = "addFood"))

menuItems.append(Text(screen, font, "Increase Hydration: ", RED, (125, 150), active = False))
menuItems.append(Button(350, 150, screen, font, "%s eggs"%costFormula(chickens[0].hydrationMax/8), BLACK, RED, "remove %s"%costFormula(chickens[0].hydrationMax/8), active = False, action2 = "addHydration"))

menuItems.append(Text(screen, font, "Increase spawn: ", RED, (125, 200), active = False))
menuItems.append(Button(350, 200, screen, font, "%s eggs"%costFormula(spawnRate), BLACK, RED, "remove %s"%costFormula(spawnRate), active = False, action2 = "addSpawn"))


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
            for chicken in chickens:
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
                    elif button.action == 'game':
                        button.text = 'store'
                        button.action = 'store'
                        state = 'game'
                    for item in menuItems:
                        item.active = not item.active
                        if vv: print(item.active)
            if state == 'store':
                for item in menuItems:
                    if item.rect.collidepoint(x, y):
                        try:
                            #print('cost button clicked')
                            num = int(item.action.replace('remove ', ''))
                            if eggs - num >= 0:
                                eggs -= num
                                print("You spent %s eggs"%num)
                                item.text = "%s eggs"%costFormula(num)
                                item.action = "remove %s"%costFormula(num)
                                if item.action2 == 'addSpeed':
                                    speedLevel = int(num)
                                    for chicken in chickens:
                                        chicken.speed += 1
                                elif item.action2 == 'addFood':
#                                    speedLevel = int(num)
                                    for chicken in chickens:
                                        chicken.foodMax += int(chicken.foodMax/10)
                                        chicken.foodBar.valueMax = chicken.foodMax
                                elif item.action2 == 'addHydration':
#                                    speedLevel = int(num)
                                    for chicken in chickens:
                                        chicken.hydrationMax += int(chicken.hydrationMax/10)
                                        if vv: print(chicken.hydration, chicken.hydrationMax)
                                        chicken.hydrationBar.valueMax = chicken.hydrationMax
                                elif item.action2 == 'addSpawn':
                                    spawnRate = costFormula(spawnRate)
                                    print(spawnRate)
                            else:
                                if vv: print("Not enough money")
                        except AttributeError:
                            pass
        if event.type == EGG_LAIED:
            eggs += 1
    #Spawn chickens
    if randint(0, 10000) < spawnRate and fpsClock.get_fps() > FPS-10:
        tmp = Chicken(screen, chickenImage, x = randint(50, 350), y = randint(50, 500), v = vv)
        tmp.speed = chickens[0].speed
        tmp.foodMax = chickens[0].foodMax
        tmp.hydrationMax = chickens[0].hydrationMax
        chickens.append(tmp)
    #add eggs when needed:
    if frameCount % 1800 == 0:
        eggs += len(chickens)
    ##Update screen:
    screen.fill(BACKGROUND_GREEN)

    #Depending on the state the chickens may or may not be drawn...
    if state == "game":
        for chicken in chickens:
            died = chicken.update()
            if died:
                chickens.remove(chicken)
                #print("Chicken %s died"%chicken)
            chicken.draw()
            #screen.blit(chickenImage, (chicken.x, chicken.y))
    elif state == "store":
        for chicken in chickens:
            died = chicken.update()
            if died:
                chickens.remove(chicken)
        for item in menuItems:
            item.update()
            item.draw()
    else:
        print("INVALID STATE OF: %S RETURNING TO GAME"%state)
        state = "game"

    for button in buttons:
        button.update()
        button.draw()
    
    fpsText.draw()
    fpsText.update(f"{fpsClock.get_fps():2.0f} FPS")
    chickenCount.draw()
    chickenCount.update("%s chicken(s)"%len(chickens))
    eggCount.draw()
    eggCount.update("%s eggs"%eggs)
    frameCount += 1
    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.quit()
stats = [eggs, speedLevel, FPS, spawnRate]
saveData('save.dat', chickens, stats)
