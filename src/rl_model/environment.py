import random

class TrafficEnvironment:
    def __init__(self):
        self.state = 0  # vehicle count

    def reset(self):
        self.state = random.randint(0, 20)
        return self.state

    def step(self, action):
        """
        action:
        0 → short green
        1 → medium green
        2 → long green
        """

        vehicle_count = self.state

        # reward logic
        if vehicle_count < 5 and action == 0:
            reward = 10
        elif 5 <= vehicle_count < 10 and action == 1:
            reward = 10
        elif vehicle_count >= 10 and action == 2:
            reward = 10
        else:
            reward = -5

        # next state
        next_state = random.randint(0, 20)

        return next_state, reward