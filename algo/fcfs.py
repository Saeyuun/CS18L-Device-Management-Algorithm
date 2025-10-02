def run(requests, head):
    """
    First-Come, First-Served
    """
    seek_sequence = []
    total_head_movement = 0
    current = head

    for req in requests:
        seek_sequence.append(req)
        total_head_movement += abs(req - current)
        current = req

    return {"sequence": seek_sequence, "movement": total_head_movement}