import pygame
import sys
from bullet import Bullet


def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.kright = True
            if event.key == pygame.K_a:
                gun.kleft = True
            if event.key == pygame.K_w:
                gun.kup = True
            if event.key == pygame.K_s:
                gun.kdown = True


            if event.key == pygame.K_l:
                gun.kright2 = True
            if event.key == pygame.K_j:
                gun.kleft2 = True
            if event.key == pygame.K_i:
                gun.kup2 = True
            if event.key == pygame.K_k:
                gun.kdown2 = True

            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                pygame.mixer.music.load('mp3/erro.mp3')
                pygame.mixer.music.play(0)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.kright = False

def update(screen, gun, bg_color, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    gun.output()
    pygame.display.flip()

def kill(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))