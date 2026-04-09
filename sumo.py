import random

def generate_sumo_traffic():
    """
    Simulates traffic like SUMO
    """

    lane1 = random.randint(0, 15)
    lane2 = random.randint(0, 15)
    lane3 = random.randint(0, 15)

    return {
        "lane1": lane1,
        "lane2": lane2,
        "lane3": lane3,
        "total": lane1 + lane2 + lane3
    }