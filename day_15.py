from collections import deque
import intcode

with open("inputs/day_15_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

MAPS = {complex(1, 0): 3, complex(0, 1): 1, complex(-1, 0): 4, complex(0, -1): 2}

# First depth-first search the whole maze with the intcode computer to map it
# out. This preprocessing can then be used for both parts of the problem.
REVERSE = {1: 2, 2: 1, 3: 4, 4: 3}
maze = {complex(0, 0): 0}
droid = intcode.Intcode(program)
def droid_dfs(start):
    for incr, inp in MAPS.items():
        next = start + incr
        if next not in maze:
            droid.inputs.append(inp)
            droid.run()
            maze[next] = droid.outputs[0]
            droid.outputs = []
            if maze[next] != 0:
                droid_dfs(start + incr)
                droid.inputs.append(REVERSE[inp])
                droid.run()
                droid.outputs = []
droid_dfs(0)
for loc, res in maze.items():
    if res == 2:
        oxygen_system = loc

# Part 1
visited = {complex(0, 0)}
to_visit = deque([(incr, 1) for incr in MAPS])
while True:
    destination = to_visit.popleft()
    if destination[0] not in visited:
        visited.add(destination[0])
        square = maze[destination[0]]
        if square == 1:
            for incr in MAPS:
                to_visit.append((destination[0] + incr, destination[1] + 1))
        if square == 2:
            print("Part 1 solution: {}".format(destination[1]))
            break

# Part 2
visited = {}
to_visit = deque([(oxygen_system, 0)])
while to_visit:
    destination = to_visit.popleft()
    if destination[0] not in visited:
        visited[destination[0]] = destination[1]
        for incr in MAPS:
            if maze[destination[0] + incr] == 1:
                to_visit.append((destination[0] + incr, destination[1] + 1))
print("Part 2 solution: {}".format(max(visited.values())))
