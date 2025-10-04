def sstf(requests, head):
    order = []
    movement = 0
    current = head
    reqs = requests.copy()

    while reqs:
        closest = min(reqs, key=lambda x: abs(x - current))
        order.append(closest)
        movement += abs(current - closest)
        current = closest
        reqs.remove(closest)

    return order, movement
