import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # In all cases, kill instance and create others if needed
        self.kill()
        # If asteroid is smallest, no need to spawn new
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Random angle between 20, 50 degrees
        random_rotation = random.uniform(20, 50)
        # Rotate new velocities to separate directions
        vel_1 = self.velocity.rotate(random_rotation)
        vel_2 = self.velocity.rotate(-random_rotation)
        # New radius is either 40 (med) or 20 (small)
        radius = self.radius - ASTEROID_MIN_RADIUS
        # Create and attach velocities (slightly faster)
        ast_1 = Asteroid(self.position.x, self.position.y, radius=radius)
        ast_2 = Asteroid(self.position.x, self.position.y, radius=radius)
        ast_1.velocity = vel_1 * 1.2
        ast_2.velocity = vel_2 * 1.2
