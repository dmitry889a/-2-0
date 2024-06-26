import pygame 
import pygame. font
pygame.init()

win_width = 500
win_height = 500

bg  = pygame.image.load("town.png")
bg = pygame.transform.scale(bg,(win_width, win_height))

clock = pygame.time.Clock()

window = pygame.display.set_mode((win_width, win_height))
window_rect = window.get_rect()
 
pygame.display.set_caption("game")

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, new_image, x, y, width, height) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(new_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))