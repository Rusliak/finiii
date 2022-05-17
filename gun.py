import pygame


class Gun():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/maxresdefault-removebg-preview.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.kright = False
        self.kleft = False
        self.kup = False
        self.kdown = False


        self.image2 = pygame.image.load('image/91c898b7003c432d990708f93b73cfdf.max-1200x800-removebg-preview.png')
        self.rect2 = self.image2.get_rect()
        self.rect2.centerx = self.screen_rect.centerx
        self.rect2.bottom = self.screen_rect.bottom
        self.kright2 = False
        self.kleft2 = False
        self.kup2 = False
        self.kdown2 = False

    def output(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)

    def update_gun(self):
        if self.kright == True:
            self.rect.centerx = 1
        if self.kleft == True:
            self.rect.centerx += 1
        if self.kup == True:
            self.rect.bottom -= 1
        if self.kdown == True:
            self.rect.bottom -= 1

    def update_gun2(self):
        if self.kright2 == True:
            self.rect2.centerx += 1
        if self.kleft2 == True:
            self.rect2.centerx += 1
        if self.kup2 == True:
            self.rect2.bottom -= 1
        if self.kdown2 == True:
            self.rect2.bottom -= 1