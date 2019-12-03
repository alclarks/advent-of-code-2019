complex_increment = {"U": complex(0, 1), "R": complex(1, 0),
                     "D": complex(0, -1), "L": complex(-1, 0)}

class Info():
    __slots__ = ["distance", "steps"]
    def __init__(self, distance, steps):
        self.distance = distance
        self.steps = steps

def manhattan_distance(point):
    return abs(point.real) + abs(point.imag)

def point_info_from_path(path):
    global complex_increment
    corner = complex(0, 0)
    steps = 0
    step_info = {}
    for segment in path:
        inc = complex_increment[segment[0]]
        for i in range(int(segment[1:])):
            steps = steps + 1
            point = corner + (i + 1) * inc 
            if point not in step_info:
                # Only count the first time a point is hit, to count minimum
                # steps
                step_info[point] = Info(manhattan_distance(point), steps)
        corner = corner + (i + 1) * inc
    return step_info

with open("day_3_input.txt") as f:
    lines = f.read().splitlines()
    paths = [line.split(",") for line in lines]

infos = [point_info_from_path(path) for path in paths]
points = [info.keys() for info in infos]
intersections = points[0] & points[1]

# Part 1
sol = min(infos[0][point].distance for point in intersections)
print("Part 1 solution: {}".format(int(sol)))

# Part 2
sol = min((infos[0][point].steps + infos[1][point].steps)
          for point in intersections)
print("Part 2 solution: {}".format(sol))
