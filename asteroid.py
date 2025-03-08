import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):  # contructor
        super().__init__(x ,y ,radius) # inherit constructor from parents
        

    def draw(self, screen):
        pygame.draw.circle(screen , "white", self.position, self.radius , 2)

        
    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # generate random angles for new splitted asteroid
        random_angle = random.uniform(20 , 50)

        # create 2 new vectors and rotate them to random direction
        # rotate the new splitted asteroids to random angle or oposite angle
        first_new_vector = pygame.math.Vector2.rotate(self.velocity, random_angle) # self.velocity.rotate(random_angle)
        second_new_vector = pygame.math.Vector2.rotate(self.velocity, -random_angle) # self.velocity.rotate(-random_angle)

        # compute new radius for smaller asteroid thatjsut get splitted 
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # create two new asteroids 
        splitted_asteroid_one = Asteroid(self.position.x , self.position.y , new_radius)
        splitted_asteroid_two = Asteroid(self.position.x , self.position.y , new_radius)
        
        # assign the created new vectors to new created asteroids
        # scale their velocity up by 1.2 to make them move faster
        splitted_asteroid_one.velocity = first_new_vector * 1.2
        splitted_asteroid_two.velocity = second_new_vector * 1.2











    ''' === old version of update(self, dt) and draw(self, screen) that is not working ===
    def draw(self, screen):
        pygame.draw.circle(screen , "white", (self.x, self.y), self.radius , 2)
    
    def update(self,dt):
        self.x += self.x.velocity * dt
        self.y += self.y.velocity * dt
    
    why it is not working for the collision method in circles.py?
    - the self.postion remain a proper pygame.math.Vector2 object throughout the game's logic 
    to ensure all operations ,such as distance_to, function smoothly
    - replace self.position with a tuple (self.x, self.y) would no longer support distance_to
    and the collision detection would fail silently
    - by separating into self.x and self.y , the self. postion wasn't being updated in sync anymore.
    -> Therefore, when draw method was trying to reference to (self.x, self.y) as its positional
    information and the collision method relied on self.position -> mismatch occurred between 
    the logical and visual representations of the asteroid.
    '''
    