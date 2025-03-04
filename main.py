import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock_object = pygame.time.Clock()
    dt = 0
    player_object = Player( SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update the delta time
        delta_time = clock_object.tick(60) #the .tick() method returns the amount of time that has passed since the last time it was called: the delta time
        dt = delta_time/1000 #convert milliseconds to seconds

        # call player update AFTER getting the current delta time
        player_object.update(dt)

        # render the screen and player
        screen.fill("black")
        player_object.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()