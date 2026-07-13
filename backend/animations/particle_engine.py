"""
Particle Engine
Creates orbiting particles for the Arc Reactor.
"""

from math import cos, radians, sin


class Particle:
    def __init__(self, radius, angle, speed, size):

        self.radius = radius
        self.angle = angle
        self.speed = speed
        self.size = size

    def update(self):

        self.angle += self.speed

        if self.angle >= 360:
            self.angle -= 360

    def position(self, cx, cy):

        x = cx + cos(radians(self.angle)) * self.radius
        y = cy + sin(radians(self.angle)) * self.radius

        return x, y


class ParticleEngine:

    def __init__(self):

        self.particles = [

            Particle(70, 0, 1.5, 5),
            Particle(100, 90, 1.0, 6),
            Particle(130, 180, 0.8, 4),
            Particle(160, 270, 0.6, 7),

        ]

    def update(self):

        for particle in self.particles:
            particle.update()

    def all(self):
        return self.particles