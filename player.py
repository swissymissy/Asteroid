from circleshape import CircleShape
from constants import *
from shot import *
import pygame

class Player(CircleShape):
    def __init__(self, x , y ):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 #initial rotation
        self.timer = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "purple", self.triangle())

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt, direction=1):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction 

    def shoot(self):
        if self.timer > 0:
            return
        new_shot = Shot(self.position.x , self.position.y)
        new_shot.velocity = pygame.Vector2(0 , 1).rotate(self.rotation)
        new_shot.velocity *= PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN



    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_a]:
            # go left when A is pressed. reverse dt . multiply dt by -1
            self.rotate(-dt)

        if keys[pygame.K_d]:
            # go rightwhen D is pressed
            self.rotate(dt)

        if keys[pygame.K_w]:
            # moving forward with W
            self.move(dt,1)
        
        if keys[pygame.K_s]:
            # moving backward with S
            self.move(dt,-1)

        if keys[pygame.K_SPACE]:
            self.shoot()
