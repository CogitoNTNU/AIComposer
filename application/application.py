import pygame
from pygame import midi

def main():
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 1024  # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)
    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)
    try:
        pygame.mixer.music.load("application/HotelCalifornia.mid")
    
    except:
        pass
    
    pygame.mixer.music.play()
    pygame.init()

    screen = pygame.display.set_mode([800, 400])

    running = True
    width = screen.get_width()
  
# stores the height of the
# screen into a variable
    height = screen.get_height()
    color_dark = (100,100,100)
    filePlaying = True
    while running:
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, color_dark, [width/2,height*0.9,140,40])
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2 <= mouse[0] <= width/2+140 and height*0.9 <= mouse[1] <= height*0.9+40:
                    if filePlaying:
                        pygame.mixer.music.pause() 
                        filePlaying = False
                    else:
                        pygame.mixer.music.unpause()
                        filePlaying = True 
                pass
        mouse = pygame.mouse.get_pos()       

       


        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
