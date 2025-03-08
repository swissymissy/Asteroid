import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.x = x
        self.y = y 

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other_circle):
        #return pygame.math.Vector2.distance_to(self.position, other_circle.position) <= (self.radius + other_circle.radius)
        return self.position.distance_to(other_circle.position) <= self.radius + other_circle.radius