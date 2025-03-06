import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        #(surface, color, center, radius, width)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
       
        random_num = random.uniform(20,50)
       
        random_angle = self.velocity.rotate(random_num)
        random_angle2 = self.velocity.rotate(-random_num)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = random_angle *1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = random_angle2 *1.2