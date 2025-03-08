import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock_object = pygame.time.Clock()
    dt = 0
     
    # creating groups before creating a player
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() #asteroids group
    shot_group = pygame.sprite.Group() # group of shots

    # set container for Player class
    Player.containers = (updatable_group, drawable_group)

    # create the player object
    player = Player( SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)

    # set container to Asteroid class
    Asteroid.containers = (asteroids ,updatable_group, drawable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group) 

    # set container for AsteroidField
    AsteroidField.containers = (updatable_group)
    

    asteroid_field = AsteroidField()
 
    # game loop
    while True:

        # make the "x" button to close game when player hit it
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update the delta time
        delta_time = clock_object.tick(60) #the .tick() method returns the amount of time that has passed since the last time it was called: the delta time
        dt = delta_time/1000 #convert milliseconds to seconds

        # call player update AFTER getting the current delta time
        updatable_group.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shot_group:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        # render the screen and player
        screen.fill("black")

        # because draw() is custome, we gotta call it manually, using loop
        #explaination: the loop ensures that every sprite in drawable_group has its draw() method
        # carefully invoked, allowing the triangle to step into the visible world.
        # this is precisely the magic needed when draw() is a custome method and 
        # isn't automatically handled by Pygame's Group
        for sprite in drawable_group:
            sprite.draw(screen) # draw all sprites in the group of player onto the screen
        pygame.display.flip()



if __name__ == "__main__":
    main()