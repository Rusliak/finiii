import pygame

pygame.init()

res = (1366, 720)

screen = pygame.display.set_mode(res)
color = (234, 228, 62)
color_light = (2, 20, 253)
color_dark = (100, 100, 100)
color2 = (234, 228, 62)
color_light2 = (2, 20, 253)
color_dark2 = (100, 100, 100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('leave', True, color)
smallfont2 = pygame.font.SysFont('Corbel', 35)
text2 = smallfont2.render('start',True, color2)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 300 <= mouse[0] <= 600 and 80 <= mouse[1] <= 140:
                pygame()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 300 <= mouse[0] <= 600 and 300 <= mouse[1] <= 360:
                pygame.init()

    screen.fill((60, 25, 60))
    mouse = pygame.mouse.get_pos()
    print('x=', mouse[0],'y=', mouse[1])

    if 300 <= mouse[0] <= 600 and 80 <= mouse[1] <= 140:
        pygame.draw.rect(screen, color_light, [295, 80, 310, 85])
        screen.blit(text, (600 and 80, 140))
    else:
        pygame.draw.rect(screen, color_dark, [300, 80, 300, 80])
        screen.blit(text, (600 and 80, 140))
    if 300 <= mouse[0] <= 600 and 300 <= mouse[1] <= 360:
        pygame.draw.rect(screen, color_light, [295, 275, 310, 85])
        screen.blit(text2, (600 and 300, 360))
    else:
        pygame.draw.rect(screen, color_dark, [300, 280, 300, 80])
        screen.blit(text2, (600 and 300, 360))
    pygame.display.update()