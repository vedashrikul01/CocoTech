from collections import deque

def is_valid(cell):
    return 0 <= cell < 25

def find_shortest_routes(blocked_cells):
    start = 0
    end = 24


    blocked_set = set(blocked_cells)

    #queue initialized
    queue = deque([(start, [start])])

  
    shortest_routes = []

    while queue:
        current, path = queue.popleft()

        if current == end:
            shortest_routes.append(path)
            continue

        for move in [-5, 5, -1, 1]:
            new_cell = current + move

            if is_valid(new_cell) and new_cell not in blocked_set:
                queue.append((new_cell, path + [new_cell]))
                blocked_set.add(new_cell)  #visited

    return shortest_routes

blocked_cells = [5, 6, 7, 12, 17,23]
shortest_routes = find_shortest_routes(blocked_cells)


for i, route in enumerate(shortest_routes, start=1):
    print(f"Shortest Route {i}: {route}")
