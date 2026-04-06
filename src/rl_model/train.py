from .environment import TrafficEnvironment
from .agent import QLearningAgent

env = TrafficEnvironment()
agent = QLearningAgent()

episodes = 1000

for episode in range(episodes):
    state = env.reset()

    for _ in range(20):
        action = agent.choose_action(state)

        next_state, reward = env.step(action)

        agent.update(state, action, reward, next_state)

        state = next_state

print("Training complete!")

print("\nLearned Policy:")
for i in range(0, 21):
    action = agent.choose_action(i)
    print(f"Traffic: {i} → Action: {action}")