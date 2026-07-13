"""
Ring Animation
Handles smooth rotation for Arc Reactor rings.
"""


class RingAnimation:
    """
    Controls ring rotation.
    """

    def __init__(self, speed: float = 1.0):
        self.angle = 0.0
        self.speed = speed

    def update(self):
        self.angle += self.speed

        if self.angle >= 360:
            self.angle -= 360

    def set_speed(self, speed: float):
        self.speed = speed

    def reset(self):
        self.angle = 0.0

    @property
    def rotation(self):
        return self.angle