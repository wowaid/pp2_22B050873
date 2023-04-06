#Imports
import pygame , sys
import random, time
from pygame.locals import *

#Initializing
pygame.init()

#Colors
color_black = pygame.Color(0, 0, 0)         # Black
color_white = pygame.Color(255, 255, 255)   # White
color_grey = pygame.Color(128, 128, 128)   # Grey
color_red = pygame.Color(255, 0, 0)       # Red
color_green = pygame.Color(0, 255, 0)      #Green

#Set Clock
clock = pygame.time.Clock()

#Variables
screen_w, screen_h = 400, 600
speed = 5
speed_coin = 2
score = 0
coin_score = 0

#Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 25)
game_over = font.render("Game Over", True, color_black )

background = pygame.image.load("./elements/AnimatedStreet.png")

#Screen Creation
screen = pygame.display.set_mode((400, 600))
screen.fill(color_white)
pygame.display.set_caption("Game")


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./elements/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, screen_w - 30), 0)
    def move(self):
        self.rect.move_ip(0,speed_coin)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, screen_w - 30), 0)
    def new(self):
        screen.blit(self.image, self.rect)
        self.rect.top = 0
        self.rect.center = (random.randint(30, screen_w - 30), 0)
        self.rect.move_ip(0,speed_coin)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./elements/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_w - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_w - 40), 0)
    def new(self):
        self.rect.center = (random.randint(40, screen_w - 40), 0)
        self.rect.move_ip(0,speed)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./elements/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < screen_h:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_w:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    

#Setting up sprites
p1 = Player()
e1 = Enemy() 
c1 = Coin()

#Creating Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(e1)
all_sprites.add(p1)

coinss = pygame.sprite.Group()
coinss.add(c1)

#Adding Userevent 
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

#Game Loop
while True:
    #Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == inc_speed:
            speed += 0.2

    #Background, font settings 
    screen.blit(background, (0, 0))
    scores = font_small.render(str(score), True, color_black)
    coin_scores = font_small.render(str(coin_score), True, color_black)
    screen.blit(scores, (10, 10))
    screen.blit(coin_scores, (375, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    for entity in coinss:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #Collect coins
    if pygame.sprite.spritecollideany(p1, coinss):
        pygame.mixer.Sound("./elements/coin_collect.wav").play()
        for entity in coinss:
            coin_score += 1
            entity.kill()
        c2 = Coin()
        coinss.add(c2)
        c2.new()
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound("./elements/crash.wav").play()
        time.sleep(0.5)

        screen.fill(color_red)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in enemies:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)