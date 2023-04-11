import pygame
import os

pygame.init()
screen = pygame.display.set_mode((500, 100))

music_dir = "./music/"
music_files = os.listdir(music_dir)
current_music = 0
pygame.mixer.music.load(music_dir + music_files[current_music])

font = pygame.font.SysFont(None, 24)

key_play = pygame.K_SPACE
key_stop = pygame.K_ESCAPE
key_next = pygame.K_RIGHT
key_prev = pygame.K_LEFT

pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == key_play:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == key_stop:
                pygame.mixer.music.stop()

            elif event.key == key_next:
                current_music = (current_music + 1) % len(music_files)
                pygame.mixer.music.load(music_dir + music_files[current_music])
                pygame.mixer.music.play()
                
            elif event.key == key_prev:
                current_music = (current_music - 1) % len(music_files)
                pygame.mixer.music.load(music_dir + music_files[current_music])
                pygame.mixer.music.play()

    pygame.display.update()