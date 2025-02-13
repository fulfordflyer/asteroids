import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        asteroid_one_vector = self.velocity.rotate(random_angle)
        asteroid_two_vector = self.velocity.rotate(-random_angle)

        radius_new = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, radius_new)
        asteroid_two = Asteroid(self.position.x, self.position.y, radius_new)

        asteroid_one.velocity = 1.2 * asteroid_one_vector
        asteroid_two.velocity = 1.2 * asteroid_two_vector
