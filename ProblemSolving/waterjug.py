from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()

    # state = (amount_in_jug1, amount_in_jug2)
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        # if target is achieved
        if x == target or y == target:
            print("solution found:", (x, y))
            return

        if (x, y) in visited:
            continue

        visited.add((x, y))

        # all possible actions
        states = [
            (jug1, y),              # fill jug1
            (x, jug2),              # fill jug2
            (0, y),                 # empty jug1
            (x, 0),                 # empty jug2
            (min(x + y, jug1), y - (min(x + y, jug1) - x)),  # pour jug2 → jug1
            (x - (min(x + y, jug2) - y), min(x + y, jug2))   # pour jug1 → jug2
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("no solution exists")
