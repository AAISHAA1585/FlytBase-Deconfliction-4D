import json

def load_primary(path):
    """
    Loads the primary drone's mission from JSON.
    """
    with open(path, 'r') as f:
        data = json.load(f)
    if 'waypoints' not in data or 't_start' not in data or 't_end' not in data:
        raise ValueError("Invalid primary JSON structure")
    return data

def load_others(path):
    """
    Loads simulated drones' flight schedules from JSON.
    """
    with open(path, 'r') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Others JSON must be a list")
    for d in data:
        if 'waypoints' not in d or 'times' not in d:
            raise ValueError("Invalid others JSON structure")
    return data