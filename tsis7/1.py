import pygame as pg
from datetime import datetime

pg.init()

WIDTH = 800
HEIGHT = 600
FPS = 45

pg.display.set_caption('clock')
screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()

background = pg.image.load("./images/background.jpg")
h = pg.image.load("./images/min.png")
h2 = pg.image.load("./images/sec.png")

def time(t):
    return 360 - t * 6

def rotate(surface, image, left_pos, angle):
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = left_pos).center)

    surface.blit(rotated_image, new_rect)
running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(background, (0,0))
    t = datetime.now()
    angle_sec = time(t.second)
    angle_min = time(t.minute)
    rotate(screen, h2, (255, 150), angle_sec)
    rotate(screen, h, (255, 150), angle_min)
    pg.display.flip()

pg.quit()