"""
Pulse Animation
Creates the heartbeat effect of the Arc Reactor.
"""


class PulseAnimation:
    """
    Controls the expanding and contracting glow.
    """

    def __init__(self,
                 minimum=0.95,
                 maximum=1.08,
                 speed=0.004):

        self.scale = 1.0
        self.minimum = minimum
        self.maximum = maximum
        self.speed = speed
        self.direction = 1

    def update(self):

        self.scale += self.speed * self.direction

        if self.scale >= self.maximum:
            self.scale = self.maximum
            self.direction = -1

        elif self.scale <= self.minimum:
            self.scale = self.minimum
            self.direction = 1

    def value(self):
        return self.scale

    def reset(self):
        self.scale = 1.0
        self.direction = 1