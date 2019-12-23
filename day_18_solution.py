from collections import defaultdict, deque

ADJS = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]
QUADRANTS = [0, 1, 2, 3]

def parse_input(filename):
    keys = {}
    doors = {}
    graph = defaultdict(list)
    starts = []
    with open(filename) as f:
        lines = [line.strip("\n") for line in f.readlines()]
    points = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                continue
            if char == "@":
                starts.append(complex(j, i))
            elif char.isupper():
                doors[complex(j, i)] = char
            elif char.islower():
                keys[complex(j, i)] = char
            points.append(complex(j, i))
    for point in points:
        for adj in ADJS:
            if point + adj in points:
                graph[point].append(point + adj)
    ignoredoors = [door for door in doors if doors[door].lower() not in keys.values()]
    for d in ignoredoors:
        del doors[d]
    return keys, doors, starts, graph

def bfs(keys, doors, start, graph):
    keys_to_collect = "".join(sorted(keys.values()))
    visited = set()
    to_visit = deque([((start, ""), 0)])
    while True:
        state, depth = to_visit.popleft()
        position, collected = state
        if position in keys:
            collected = "".join(sorted(list(set(collected + keys[position]))))
        if collected == keys_to_collect:
            return depth
        state = (position, collected)
        if state not in visited:
            visited.add(state)
            for neighbour in graph[position]:
                if (neighbour in doors and doors[neighbour].lower() not in collected):
                    continue
                to_visit.append(((neighbour, collected), depth+1))

def part1():
    keys, doors, starts, graph = parse_input("inputs/day_18_input_1.txt")
    return bfs(keys, doors, starts[0], graph)

def part2():
    total_steps = 0
    for quad in QUADRANTS:
        quad_file = "inputs/day_18_input_2.{}.txt".format(quad)
        keys, doors, starts, graph = parse_input(quad_file)
        total_steps = total_steps + bfs(keys, doors, starts[0], graph)
    return total_steps

print("Part 1 solution: {}".format(part1()))
print("Part 2 solution: {}".format(part2()))
