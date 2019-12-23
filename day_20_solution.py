import copy
from collections import defaultdict, deque

# Input parsing - a bit gross
maze_points = []
portals = defaultdict(list)
ADJS = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]

with open("day_20_input.txt") as f:
    lines = [line.strip("\n") for line in f.readlines()]

for i, line in enumerate(lines):
    line_len = len(line)
    for j, char in enumerate(line):
        if char == ".":
            maze_points.append(complex(j, i))
    for j in range(line_len - 1):
        if (line[j].isalpha() and line[j+1].isalpha() and
                line[j].isupper() and line[j+1].isupper()):
            if line[j-1] == ".":
                if j+1 == line_len - 1:
                    portals[line[j] + line[j+1]].append((complex(j-1, i), True))
                else:
                    portals[line[j] + line[j+1]].append((complex(j-1, i), False))
            elif line[j+2] == ".":
                if j == 0:
                    portals[line[j] + line[j+1]].append((complex(j+2, i), True))
                else:
                    portals[line[j] + line[j+1]].append((complex(j+2, i), False))
for i in range(line_len):
    col = "".join([line[i] for line in lines])
    for j in range(len(col) - 1):
        if (col[j].isalpha() and col[j+1].isalpha() and
                col[j].isupper() and col[j+1].isupper()):
            if col[j-1] == ".":
                if j+1 == len(col) -1:
                    portals[col[j] + col[j+1]].append((complex(i, j-1), True))
                else:
                    portals[col[j] + col[j+1]].append((complex(i, j-1), False))
            elif col[j+2] == ".":
                if j == 0:
                    portals[col[j] + col[j+1]].append((complex(i, j+2), True))
                else:
                    portals[col[j] + col[j+1]].append((complex(i, j+2), False))
maze_graph = defaultdict(list)
for point in maze_points:
    for ADJ in ADJS:
        if point + ADJ in maze_points:
            maze_graph[point].append(point + ADJ)

# BFS implementation - used for both parts.
def bfs(graph, start, end):
    visited = set()
    to_visit = deque([(start, 0)])
    while True:
        position, depth = to_visit.popleft()
        if position == end:
            return depth
        if position not in visited:
            visited.add(position)
            for neighbour in graph[position]:
                to_visit.append((neighbour, depth+1))

# Part 1
part1_graph = copy.deepcopy(maze_graph)

for key in portals:
    if key not in ("AA", "ZZ"):
        part1_graph[portals[key][0][0]].append(portals[key][1][0])
        part1_graph[portals[key][1][0]].append(portals[key][0][0])

print("Part 1 solution: {}".format(
    bfs(part1_graph, portals["AA"][0][0], portals["ZZ"][0][0])))

# Part 2
part2_graph = defaultdict(list)
layers = 2 * (len(portals) - 2)
for i in range(layers):
    for key, nodes in maze_graph.items():
        for neighbour in nodes:
            part2_graph[(key, i)].append((neighbour, i))

for key in portals:
    if key not in ("AA", "ZZ"):
        if portals[key][0][1]:
            outer, inner = portals[key][0][0], portals[key][1][0]
        else:
            inner, outer = portals[key][0][0], portals[key][1][0]
        for i in range(layers - 1):
            part2_graph[(inner, i)].append((outer, i+1))
            part2_graph[(outer, i+1)].append((inner, i))

print("Part 2 solution: {}".format(
    bfs(part2_graph, (portals["AA"][0][0], 0), (portals["ZZ"][0][0], 0))))
