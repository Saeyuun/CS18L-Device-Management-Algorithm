def run(requests, head):
    """
    Shortest Seek Time First
    """
    seek_sequence = []
    total_head_movement = 0
    current = head
    reqs = requests.copy()

    while reqs:
        nearest = min(reqs, key=lambda x: abs(x - current))
        seek_sequence.append(nearest)
        total_head_movement += abs(nearest - current)
        current = nearest
        reqs.remove(nearest)

    return {"sequence": seek_sequence, "movement": total_head_movement}