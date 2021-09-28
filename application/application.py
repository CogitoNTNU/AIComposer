import pygame
from pygame import midi

def main():
    with open("HotelCalifornia.mid", "r") as f:
        midiFile = f

    try:
        pygame.mixer.music.load(midiFile)
    
    except:
        pass
    
    pygame.mixer.music.play()
    pygame.init()

    screen = pygame.display.set_mode([800, 400])

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))


        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
