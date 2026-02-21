import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_SPEED, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, position, rotation):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1)
        self.unit_vector = self.velocity.rotate(rotation)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.unit_vector * SHOT_SPEED * dt
