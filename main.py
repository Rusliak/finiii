import pygame
from gun import Gun
import controls
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Tetya Zina')
    bg_color = (101, 59, 20)
    gun = Gun(screen)
    bullets = Group()

    while True:
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()
        controls.events(screen, gun, bullets)
        controls.update(screen, gun, bg_color, bullets)
        bullets.update()
        gun.update_gun()
        gun.update_gun2()
        controls.kill(bullets)
        print('Тётя Зина: ',gun.rect.centerx)
        print('Паук: ',gun.rect2.centerx)


run()