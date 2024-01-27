import time
import pygame
import sys
import random


init_result = pygame.init()
if init_result[1] != 0:
    print('pygame not installed properly')
    sys.exit()
width = 800
height = 600
size = (width,height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("牛牛牛播放器")


soundStart = False

clock = pygame.time.Clock()
    
sound = pygame.mixer.Sound('niu.mp3')
 
while True:
    clock.tick(300)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                    soundStart = not soundStart
                    I_time = time.perf_counter()
                    
    white = (255,255,255)
    screen.fill(white)
    
    font = pygame.font.Font(None,30)
    text = font.render('Press \'Space\' to Start or Pause',True,(0,0,0))
    screen.blit(text,(width/2 - text.get_width()/2,250))
    text = font.render('Press Escape to exit',True,(0,0,0))
    screen.blit(text,(width/2 - text.get_width()/2,300))

        
    if(soundStart):
        sound.play()
        ran=random.uniform(0.01,0.05)
        time.sleep(0.1)
        time.sleep(ran)
        text = font.render('Sound start for '+ str(round(time.perf_counter() - I_time,3)) + ' second',True,(0,0,0))
        screen.blit(text,(width/2 - text.get_width()/2,350))
    else:
        text = font.render('Sound is not start',True,(0,0,0))
        screen.blit(text,(width/2 - text.get_width()/2,350))

    pygame.display.flip()
