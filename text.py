##Code taken from stack overflow
##https://stackoverflow.com/questions/68509788/how-to-display-an-fps-counter-in-pygame

class Text:
    def __init__(self, surface, font, text, color, pos):
        self.surface = surface
        self.font = font
        #self.clock = clock
        self.pos = pos
        self.color = color

        #self.fps_text = self.font.render(str(int(self.clock.get_fps())) + "FPS", False, self.color)
        self.fps_text = self.font.render(str(text), False, self.color)
        self.fps_text_rect = self.fps_text.get_rect(center=(self.pos[0], self.pos[1]))

    def draw(self):
        self.surface.blit(self.fps_text, self.fps_text_rect)

    def update(self, text):
        #text = f"{self.clock.get_fps():2.0f} FPS"
        self.fps_text = self.font.render(str(text), False, self.color)
        self.fps_text_rect = self.fps_text.get_rect(center=(self.pos[0], self.pos[1]))

