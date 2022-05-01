import pygame

pygame.init()

BUTTON_DEFAULT_SIZE = [250, 100, 50]
BUTTON_DEFAULT_COLOR = [(39, 89, 46), (64, 166, 48)]
INPUT_FON_SIZE = 30


class Button:
    def __init__(self, surface, x, y, text, text_color, color=BUTTON_DEFAULT_COLOR[0], length=BUTTON_DEFAULT_SIZE[0],
                 width=BUTTON_DEFAULT_SIZE[1], height=BUTTON_DEFAULT_SIZE[2]):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width
        self.text = text
        self.text_color = text_color
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)

    def update(self):
        self.draw_button()
        self.write_text()

    def write_text(self):
        font_size = int(self.length // len(self.text))
        myFont = pygame.font.SysFont("Times New Roman", INPUT_FON_SIZE, bold=True)
        myText = myFont.render(self.text, 1, self.text_color)
        self.surface.blit(myText, (
            (self.x + self.length / 2) - myText.get_width() / 2, (self.y + self.height / 2) - myText.get_height() / 2))
        return self.surface

    def draw_button(self):
        for i in range(1, 10):
            s = pygame.Surface((self.length + (i * 2), self.height + (i * 2)))
            s.fill(self.color)
            alpha = (255 / (i + 2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, self.color, (self.x - i, self.y - i, self.length + i, self.height + i), self.width)
            self.surface.blit(s, (self.x - i, self.y - i))
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.length, self.height), 0)
        pygame.draw.rect(self.surface, BUTTON_DEFAULT_COLOR[1], (self.x, self.y, self.length, self.height))
        return self.surface

    def pressed(self):
        mouse = pygame.mouse.get_pos()
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        self.color = (100, 100, 100)
                        self.text_color = (100, 100, 100)
                        if pygame.mouse.get_pressed()[0]:
                            print("Mouse_pressed")
                            return True
                        return False
        self.color = (39, 89, 46)
        self.text_color = (250, 250, 250)
        return False
