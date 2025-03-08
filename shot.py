from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen,"pink" , self.position , self.radius , 2 )
    
    def update(self, dt):
        self.position += self.velocity * dt


'''
this constructor won't work for Shot class if you just pass new_shot = Shot()
it caused the player shoot away with the bullet the moment Space key got hit

def __init__(self, x, y, radius):

simply remove the the radius parameter or either pass the correct value in the parameter
'''