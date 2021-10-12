import pygame
import timeit
import time
from pygame import midi
from mido import MidiFile


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
        mid = MidiFile('application/HotelCalifornia.mid')
        song_length = mid.length
        print(song_length)
    except Exception as e:
        print(e)

    pygame.mixer.music.play()
    pygame.init()

    screen = pygame.display.set_mode([800, 400])

    running = True
    width = screen.get_width()
    height = screen.get_height()

    # stores the height of the
    # screen into a variable
    start_button = pygame.image.load('imgs/start_button.png')
    start_button_width = 200
    start_button_height = 100
    start_button_x = int(width / 2 - start_button_width/2)
    start_button_y = int(height / 2 - start_button_height/2)
    
    # progressBar
    barY = 50
    barX = 400
    color_dark = (100, 100, 100)
    filePlaying = True
    timerInit = True
    while running:
        if timerInit:
            starter = time.time()
            timerInit = False
        if filePlaying:
            total = time.time()
            progress = ((total-starter)*100)/song_length
            progress = progress/100
            
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, color_dark, [width*0.1, height*0.85, barX, barY], 2 )
        pygame.draw.rect(screen, color_dark, [width*0.1, height*0.85, (barX*progress), barY])
        screen.blit(start_button, (start_button_x, start_button_y))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_x <= mouse[0] <= start_button_x + start_button_width and start_button_y <= mouse[
                    1] <= start_button_y + start_button_height:
                    if filePlaying:
                        pygame.mixer.music.pause()
                        filePlaying = False
                    else:
                        pygame.mixer.music.unpause()
                        filePlaying = True
                        starter = time.time() - (total-starter)
        mouse = pygame.mouse.get_pos()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
