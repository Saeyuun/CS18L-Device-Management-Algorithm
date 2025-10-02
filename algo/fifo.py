from collections import deque

def run(pages, frames):
    """
    FIFO Page Replacement
    Input:
        pages (list[int]): sequence of page requests
        frames (int): number of page frames available
    Output:
        dict with 'steps' (page table status at each request) and 'faults'
    """
    memory = deque(maxlen=frames)
    page_faults = 0
    steps = []

    for page in pages:
        if page not in memory:
            # Page fault occurs
            if len(memory) == frames:
                memory.popleft()  # remove oldest
            memory.append(page)
            page_faults += 1
        # Record current memory state
        steps.append(list(memory))

    return {"sequence": steps, "faults": page_faults}
