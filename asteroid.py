from constants import ASTEROID_MIN_RADIUS
import pygame
import random

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Split logic for generating two new asteroids
        # Generate a random angle --> rotate both new asteroids by this angle in both directions
        # Make asteroids smaller by the amount ASTEROID_MIN_RADIUS
        # Speed them up by a factor of 1.2 and have them spawn in the location of the old one
        random_angle = random.uniform(20,50)

        split_vector1 = self.velocity.rotate(random_angle)
        split_vector2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = split_vector1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = split_vector2 * 1.2