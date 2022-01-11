## Nathan Hinton
## This file will be for buttons

import pygame

class Button:
    def __init__(self, x, y, screen, font, text, color, textColor, action, action2 = None, active = True):
        self.x = x
        self.y = y
        self.screen = screen
        self.font = font
        self.text = text
        self.color = color
        self.textColor = textColor
        self.action = action
        self.action2 = action2
        self.active = active
        self.render_text = self.font.render(str(self.text), False, self.textColor)
        self.text_rect = self.render_text.get_rect(center=(self.x, self.y))
        self.rect = self.text_rect.inflate(10, 10)

    def update(self):
        if self.active:
            self.render_text = self.font.render(str(self.text), False, self.textColor)
            self.text_rect = self.render_text.get_rect(center=(self.x, self.y))
            self.rect = self.text_rect.inflate(10, 10)

    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, self.color, self.rect)
            self.screen.blit(self.render_text, self.text_rect)
            # self.screen.blit(self.font.render(str(self.text), False, self.textColor), self.render_text.get_rect(center=(self.pos[0], self.pos[1])))
        
