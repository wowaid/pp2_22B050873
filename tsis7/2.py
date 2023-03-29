import pygame as pg
import time
import random
pg.init()
 
pg.display.set_caption("Moving by keyboard")
 
 
clock = pg.time.Clock()
 
WIDTH = 800
HEIGHT = 600
FPS = 45
 
background_image = pg.image.load("./images/background.jpg")
background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))

pg.mixer.init()
pg.mixer.music.load("./music/BrunoMars.mp3")
# pg.mixer.music.play(-1)
 
font = pg.font.SysFont("Times New Roman", 40, True)
 
screen = pg.display.set_mode((WIDTH, HEIGHT))
 
WHITE = (255,255,255)
RED=(255,0,0)
ORANGE=(255,128,0)
 
dx, dy = 15, 15
 
x,y=WIDTH/2, HEIGHT/2
x_r,y_r = 10,10

dx_r = 50
dy_r = 50
running = True
lose = False
win = False
start_time = time.time()
end_time = 10
 
while running:
    clock.tick(FPS)
    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_DOWN and y+30<HEIGHT:
        #         y += dy
        #     if event.key == pg.K_UP and y-30>0:
        #         y -= dy
        #     if event.key == pg.K_RIGHT and x+30<WIDTH:
        #         x += dx
        #     if event.key == pg.K_LEFT and x-30>0:
        #         x -= dx
    # pg.key.get_pressed()[pg.K_RIGHT] == keys[pg.K_RIGHT]
    if keys[pg.K_RIGHT] and x+30<WIDTH:
        x += dx
    if keys[pg.K_LEFT] and x>30:
        x -= dx
    if keys[pg.K_DOWN] and y+30<HEIGHT:
        y += dy
    if keys[pg.K_UP] and y>30:
        y -= dy
    screen.fill(WHITE)
    screen.blit(background_image, (0,0))
    
    pg.draw.circle(screen, ORANGE, (x,y), 30)
    pg.draw.circle(screen, (123,215,54), (x_r,y_r), 10)
    x_r += dx_r
    y_r += dy_r
    # сделать коллизию маленького шарика, чтобы он выходил за скрин

    if x_r == x and y_r == y:
        win = True
    current_time = int(time.time() - start_time)
    if current_time == end_time:
        lose = True
        pg.mixer.music.play(-1)


    text = font.render(f"Time:{end_time-current_time}", False, False)
    screen.blit(text, (10, 10))
    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                lose = False
                running = False
        screen.fill(WHITE)
        pg.display.flip()
    

    while win:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                lose = False
                running = False
        screen.fill(RED)
        pg.display.flip()

    pg.display.flip()
 
pg.quit()  