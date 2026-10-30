from collections import deque

def water_jug():
    q = deque([(0, 0)])
    visited = set()

    while q:
        a, b = q.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print(a, b)

        if a == 2 or b == 2:
            print("Goal Reached")
            return

        q.extend([
            (4, b), (a, 3), (0, b), (a, 0),
            (max(0, a+b-3), min(3, a+b)),
            (min(4, a+b), max(0, a+b-4))
        ])

water_jug()
