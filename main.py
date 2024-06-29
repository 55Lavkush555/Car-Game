import pygame
import sys
import random

pygame.init()

screen_w = 700
screen_h = 539
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Car-Game')

# Images
background = pygame.image.load("Images\\background.jpg")
player = pygame.image.load("Images\\player.png")
enmy_1 = pygame.image.load("Images\\enmy_1.png")
enmy_2 = pygame.image.load("Images\\enmy_2.png")
enmy_3 = pygame.image.load("Images\\enmy_3.png")
startup = pygame.image.load("Images\\startup.jpg")

# Sound
sound = pygame.mixer.music.load('Sound\\metal-clang-sound-81634.mp3')

def gameloop():
    # Veriables
    player_x = 160
    enmy_1_y = -1
    enmy_2_y = -1
    enmy_3_y = -1
    enmy_4_y = -1
    enmy_5_y = -1
    enmy_1_x = random.randint(0,3)
    enmy_2_x = random.randint(0,3)
    enmy_3_x = random.randint(0,3)
    enmy_4_x = random.randint(0,3)
    enmy_5_x = random.randint(0,3)

    if enmy_1_x == 0:
        enmy_1_x = 160
    elif enmy_1_x == 1:
        enmy_1_x = 265
    elif enmy_1_x == 2:
        enmy_1_x = 370
    elif enmy_1_x == 3:
        enmy_1_x = 475

    if enmy_2_x == 0:
        enmy_2_x = 160
    elif enmy_2_x == 1:
        enmy_2_x = 265
    elif enmy_2_x == 2:
        enmy_2_x = 370
    elif enmy_2_x == 3:
        enmy_2_x = 475

    if enmy_3_x == 0:
        enmy_3_x = 160
    elif enmy_3_x == 1:
        enmy_3_x = 265
    elif enmy_3_x == 2:
        enmy_3_x = 370
    elif enmy_3_x == 3:
        enmy_3_x = 475

    if enmy_4_x == 0:
        enmy_4_x = 160
    elif enmy_4_x == 1:
        enmy_4_x = 265
    elif enmy_4_x == 2:
        enmy_4_x = 370
    elif enmy_4_x == 3:
        enmy_4_x = 475

    if enmy_5_x == 0:
        enmy_5_x = 160
    elif enmy_5_x == 1:
        enmy_5_x = 265
    elif enmy_5_x == 2:
        enmy_5_x = 370
    elif enmy_5_x == 3:
        enmy_5_x = 475

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()

                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_RIGHT and player_x<=370:
                                        player_x+=105
                                        pygame.mixer.music.play()

                                    elif event.key == pygame.K_LEFT and player_x>=265:
                                        player_x-=105
                                        pygame.mixer.music.play()

                            enmy_1_y+=0.6
                            enmy_2_y+=0.5
                            enmy_3_y+=0.4
                            enmy_4_y+=0.7
                            enmy_5_y+=0.8
                            screen.blit(background, (0,0))
                            screen.blit(player, (player_x,420))
                            screen.blit(enmy_1, (enmy_1_x, enmy_1_y))
                            screen.blit(enmy_2, (enmy_2_x, enmy_2_y))
                            screen.blit(enmy_3, (enmy_3_x, enmy_3_y))
                            screen.blit(enmy_2, (enmy_4_x, enmy_4_y))
                            screen.blit(enmy_3, (enmy_5_x, enmy_5_y))

                            if abs (screen_w - enmy_1_y)<1:
                                enmy_1_y = 0
                                enmy_1_x = random.randint(0,3)
                                if enmy_1_x == 0:
                                    enmy_1_x = 160
                                elif enmy_1_x == 1:
                                    enmy_1_x = 265
                                elif enmy_1_x == 2:
                                    enmy_1_x = 370
                                elif enmy_1_x == 3:
                                    enmy_1_x = 475

                            if abs (screen_w - enmy_2_y)<1:
                                enmy_2_y = 0
                                enmy_2_x = random.randint(0,3)
                                if enmy_2_x == 0:
                                    enmy_2_x = 160
                                if enmy_2_x == 1:
                                    enmy_2_x = 265
                                if enmy_2_x == 2:
                                    enmy_2_x = 370
                                if enmy_2_x == 3:
                                    enmy_2_x = 475

                            if abs (screen_w - enmy_3_y)<1:
                                enmy_3_y = 0
                                enmy_3_x = random.randint(0,3)
                                if enmy_3_x == 0:
                                    enmy_3_x = 160
                                if enmy_3_x == 1:
                                    enmy_3_x = 265
                                if enmy_3_x == 2:
                                    enmy_3_x = 370
                                if enmy_3_x == 3:
                                    enmy_3_x = 475

                            if abs (screen_w - enmy_4_y)<1:
                                enmy_4_y = 0
                                enmy_4_x = random.randint(0,3)
                                if enmy_4_x == 0:
                                    enmy_4_x = 160
                                if enmy_4_x == 1:
                                    enmy_4_x = 265
                                if enmy_4_x == 2:
                                    enmy_4_x = 370
                                if enmy_4_x == 3:
                                    enmy_4_x = 475

                            if abs (screen_w - enmy_5_y)<1:
                                enmy_5_y = 0
                                enmy_5_x = random.randint(0,3)
                                if enmy_5_x == 0:
                                    enmy_5_x = 160
                                if enmy_5_x == 1:
                                    enmy_5_x = 265
                                if enmy_5_x == 2:
                                    enmy_5_x = 370
                                if enmy_5_x == 3:
                                    enmy_5_x = 475

                            pygame.display.update()

                            if abs (420 - enmy_1_y)<70 and (player_x == enmy_1_x):
                                gameloop()
                                break

                            if abs (420 - enmy_2_y)<70 and (player_x == enmy_2_x):
                                gameloop()
                                break

                            if abs (420 - enmy_3_y)<70 and (player_x == enmy_3_x):
                                gameloop()
                                break

                            if abs (420 - enmy_4_y)<70 and (player_x == enmy_4_x):
                                gameloop()
                                break

                            if abs (420 - enmy_5_y)<70 and (player_x == enmy_5_x):
                                gameloop()
                                break

        screen.blit(startup, (0,0))
        pygame.display.update()

gameloop()