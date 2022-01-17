##Code taken from stack overflow
##https://stackoverflow.com/questions/68509788/how-to-display-an-fps-counter-in-pygame

class Text:
    def __init__(self, surface, font, text, color, pos, active = True):
        self.surface = surface
        self.font = font
        self.active = active
        #self.clock = clock
        self.pos = pos
        self.color = color
        self.text = text

        #self.fps_text = self.font.render(str(int(self.clock.get_fps())) + "FPS", False, self.color)
        self.renderText = self.font.render(str(text), False, self.color)
        self.rect = self.renderText.get_rect(center=(self.pos[0], self.pos[1]))

    def draw(self):
        if self.active:
            self.surface.blit(self.renderText, self.rect)

    def update(self, text = None):
        if self.active:
            if text == None:
                text = self.text
            #text = f"{self.clock.get_fps():2.0f} FPS"
            self.renderText = self.font.render(str(text), False, self.color)
            self.rect = self.renderText.get_rect(center=(self.pos[0], self.pos[1]))

