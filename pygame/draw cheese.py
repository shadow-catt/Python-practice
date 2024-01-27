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

        white = (255,255,255)
        surface.fill(white)


        #show a image of cheese
        cheeseImage = pygame.image.load('cheese.png')
        cheesePos = (0,0)
        surface.blit(cheeseImage,cheesePos)
        pygame.display.flip()

        #---------------------next operation-------------------
        time.sleep(2)
        #------------------------------------------------------

        #ove the cheese
        cheeseX = 40
        cheeseY = 60
        
        clock = pygame.time.Clock()

        #move the cheese for 30 times every second repeat 100 times
        for i in range(100):
            clock.tick(5)
            surface.fill(white)       #background color
            cheeseX = cheeseX + 1
            cheeseY = cheeseY + 1
            cheesePos = (cheeseX,cheeseY)
            surface.blit(cheeseImage,cheesePos)
            pygame.display.flip()
        
ImageDemo.do_image_demo()
