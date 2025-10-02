from collections import deque

def run(requests, head=None):
    """
    FIFO Queue for I/O requests
    (no head movement calculation needed)
    """
    queue = deque(requests)
    processed = []

    while queue:
        processed.append(queue.popleft())

    return {"sequence": processed, "movement": None}