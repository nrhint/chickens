##Nathan Hinton
##This file will contain the code for running the window.

import pygame
from random import randint

from chicken import Chicken
from text import Text

v = True
vv = False

pygame.init()
font = pygame.font.Font(None, 36)


width=350
height=400
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

##Setup the objects lists:
chickens = []
for x in range(0, 1):
    chickens.append(Chicken(screen, chickenImage, x = 50, y = 50, v = vv))

chickenCount = Text(screen, font, "loading...", BLACK, (200, 10))

screen.fill(BACKGROUND_GREEN)
pygame.display.flip()

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
    if randint(0, 1000) < 1:
        chickens.append(Chicken(screen, chickenImage, x = randint(50, 200), y = randint(50, 250), v = vv))
    ##Update screen:
    screen.fill(BACKGROUND_GREEN)
    for chicken in chickens:
        died = chicken.update()
        if died:
            chickens.remove(chicken)
            #print("Chicken %s died"%chicken)
        chicken.draw()
        #screen.blit(chickenImage, (chicken.x, chicken.y))
    fpsText.draw()
    fpsText.update(f"{fpsClock.get_fps():2.0f} FPS")
    chickenCount.draw()
    chickenCount.update("%s chicken(s)"%len(chickens))
    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.quit()
