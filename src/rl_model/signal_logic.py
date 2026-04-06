def get_signal_time(vehicle_count):
    """
    Decide green signal time based on traffic
    """

    if vehicle_count < 5:
        return 10   # seconds
    elif vehicle_count < 10:
        return 20
    else:
        return 30


def get_signal_action(vehicle_count):
    """
    Convert count → action
    """
    green_time = get_signal_time(vehicle_count)

    return {
        "action": "GREEN",
        "duration": green_time
    }