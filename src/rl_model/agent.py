import numpy as np
import random

class QLearningAgent:
    def __init__(self):
        self.q_table = np.zeros((21, 3))  # states (0-20), actions (3)

        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, 2)
        else:
            return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state):
        best_next = np.max(self.q_table[next_state])

        self.q_table[state][action] += self.alpha * (
            reward + self.gamma * best_next - self.q_table[state][action]
        )

    def get_action_for_state(self, state):
        """
        Get best action (no exploration)
        """
        return int(np.argmax(self.q_table[state]))