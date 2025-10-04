def fcfs(requests, head):
    order = []
    movement = 0
    current = head

    for r in requests:
        order.append(r)
        movement += abs(current - r)
        current = r

    return order, movement
