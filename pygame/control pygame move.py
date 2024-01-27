#moving a picture
import pygame
import time

class ImageDemo:

    #default setting
    @staticmethod
    def do_image_demo():
        init_result = pygame.init()
        if init_result[1] != 0:
            print('pygame not installed properly')
            return

        width = 800
        height = 600
        size = (width,height)

        surface = pygame.display.set_mode(size)

        pygame.display.set_caption('Image example')

        #it can moving up, moving down, and save the track, and exit with esc 
        cheeseX = 40
        cheeseY = 60
        cheeseYSpeed = 2
        cheeseXSpeed = 2
        cheeseMovingUp = False
        cheeseMovingDown = False
        cheeseMovingLeft = False
        cheeseMovingRight = False
        cheeseClear = True
        cheeseImage = pygame.image.load('cheese.png')
        
        clock = pygame.time.Clock()
        while True:
            clock.tick(300)
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return

                    #moving in y-axis
                    elif e.key == pygame.K_UP:
                        cheeseMovingUp = True
                    elif e.key == pygame.K_DOWN:
                        cheeseMovingDown = True

                    #moving in x-axis
                    elif e.key == pygame.K_LEFT:
                        cheeseMovingLeft = True
                    elif e.key == pygame.K_RIGHT:
                        cheeseMovingRight = True

                    #save the track
                    elif e.key == pygame.K_SPACE:
                        cheeseClear = not cheeseClear
                        
                elif e.type == pygame.KEYUP:
                    if e.key ==pygame.K_UP:
                        cheeseMovingUp = False
                    elif e.key == pygame.K_DOWN:
                        cheeseMovingDown = False
                    elif e.key == pygame.K_LEFT:
                        cheeseMovingLeft = False
                    elif e.key == pygame.K_RIGHT:
                        cheeseMovingRight = False

            if cheeseMovingDown:
                if cheeseY < 550:
                    cheeseY = cheeseY + cheeseYSpeed
                    
            if cheeseMovingUp:
                if cheeseY > 0:
                    cheeseY = cheeseY - cheeseYSpeed
                    
            if cheeseMovingLeft:
                if cheeseX > 0:
                    cheeseX = cheeseX - cheeseXSpeed
                    
            if cheeseMovingRight:
                if cheeseX < 700:
                    cheeseX = cheeseX + cheeseXSpeed
                    
            if cheeseClear:
                white = (255,255,255)
                surface.fill(white)
            
            cheesePos = (cheeseX,cheeseY)
            surface.blit(cheeseImage,cheesePos)
            pygame.display.flip()
        
ImageDemo.do_image_demo()
