from .agent import QLearningAgent

# Load trained agent
agent = QLearningAgent()

# For now (simple version), we reuse learned Q-table
# (later you can save/load model)


def get_signal_from_rl(vehicle_count):
    state = min(vehicle_count, 20)  # limit to 0–20

    action = agent.get_action_for_state(state)

    # Convert action → signal time
    if action == 0:
        duration = 10
    elif action == 1:
        duration = 20
    else:
        duration = 30

    return {
        "action": "GREEN",
        "duration": duration
    }