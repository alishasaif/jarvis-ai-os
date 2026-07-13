"""
State Animation
Controls Arc Reactor visual states.
"""


class StateAnimation:

    STATES = {
        "IDLE": {
            "color": "#00E5FF",
            "ring_speed": 2.0,
            "pulse_speed": 0.004,
        },
        "LISTENING": {
            "color": "#00FF88",
            "ring_speed": 4.0,
            "pulse_speed": 0.006,
        },
        "THINKING": {
            "color": "#FFC107",
            "ring_speed": 6.0,
            "pulse_speed": 0.008,
        },
        "SPEAKING": {
            "color": "#AA66FF",
            "ring_speed": 3.5,
            "pulse_speed": 0.005,
        },
        "OFFLINE": {
            "color": "#FF5252",
            "ring_speed": 0.0,
            "pulse_speed": 0.0,
        },
    }

    def __init__(self):
        self.state = "IDLE"

    def set_state(self, state: str):
        if state in self.STATES:
            self.state = state

    def current(self):
        return self.STATES[self.state]