# -*- coding:utf-8 -*-

import pygame
from Fileplayer import Player
from Platforms import Platform
'''from pygame import mixer'''

SIZE = (800, 640)

#создание окна
window = pygame.display.set_mode(SIZE)
#создание рабочей поверхности (игровой экран)
screen = pygame.Surface(SIZE)

#создание героя
hero = Player(55, 55)
left = right = up = False


#создание уровня
level = [
    '--------------------',
    '-                  -',
    '-                  -',
    '-                  -',
    '-       ---        -',
    '-                  -',
    '-   ----           -',
    '-                  -',
    '-            --    -',
    '-                  -',
    '---                -',
    '-                  -',
    '-    -----         -',
    '-               -- -',
    '-                  -',
    '--------------------', ]

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
platforms = []

x = 0
y = 0
for row in level:
    for col in row:
        if col == '-':
            pl = Platform(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        x += 40
    y += 40
    x = 0

'''# Загрузка музыки и звука
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
music = pygame.mixer.Sound('music/Crazy.ogg')
music.play(-1)'''


#открытие игрового цикла
done = True
timer = pygame.time.Clock()


while done:
    #блок управления событиями
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        #нажатие клавиш
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_UP:
                up = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_UP:
                up = False

    # закрашиваем рабочую поверхность
    screen.fill((10, 120, 10))

    #отображение героя
    hero.update(left, right, up, platforms)
    sprite_group.draw(screen)

    # отображаем рабочую поверхность в окне
    window.blit(screen, (0, 0))
    # обновляем окно
    pygame.display.flip()
    timer.tick(200)

'''создаем меню'''
punkts = [(120, 140, u'Game', (250, 250, 30), (250, 30, 250), 0),
		  (130, 210, u'Quit', (250, 250, 30), (250, 30, 250), 1)]
game = Menu(punkts)
game.menu()
