from sumo import generate_sumo_traffic
from src.rl_model.use_model import get_signal_from_rl

for i in range(10):
    traffic = generate_sumo_traffic()
    signal = get_signal_from_rl(traffic["total"])

    print("Traffic:", traffic)
    print("Signal:", signal)
    print("-" * 40)