def fifo(requests, frames):
    page_table = []
    faults = 0
    steps = []

    for r in requests:
        if r not in page_table:
            faults += 1
            if len(page_table) < frames:
                page_table.append(r)
            else:
                page_table.pop(0)
                page_table.append(r)
        steps.append(page_table.copy())

    return faults, steps
