import cmath
import math
import collections

with open("day_10_input.txt") as f:
    info = f.read().splitlines()

asteroids = []
for i, row in enumerate(info):
    for j, space in enumerate(row):
        if space == "#":
            asteroids.append(complex(j, i))

# Part 1
max = 0
best_place = 0
for asteroid in asteroids:
    rel_asteroids = asteroids.copy()
    rel_asteroids.remove((asteroid))
    grads = set()
    for rel_asteroid in rel_asteroids:
        grads.add(cmath.phase(rel_asteroid - asteroid))
    if len(grads) > max:
        max, best_place = len(grads), asteroid
print("Part 1 solution: {}".format(max))

# Part 2
polars = [cmath.polar(asteroid - best_place) for asteroid in asteroids]
# Can exploit the fact that a full sweep isn't completed, since part 1's
# solution is greater than 200
polar_dict = collections.defaultdict(list)
for polar in polars:
    polar_dict[polar[1]].append(polar[0])

arg_list = list(polar_dict.keys())
arg_list.sort()
list_len = len(arg_list)
start = arg_list.index(-math.pi/2)
finish = (start + 200 - 1) % list_len
finish_arg = arg_list[finish]
winner = cmath.rect(min(polar_dict[finish_arg]), finish_arg) + best_place
print("Part 2 solution: {}".format(int(winner.real * 100 + winner.imag)))
