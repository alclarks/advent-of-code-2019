import intcode

DIRS = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]

with open("inputs/day_17_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

# Part 1
part1 = intcode.Intcode(program)
part1.run()
scaffolds = set()
intersections = []
row = 0
column = 0
for char in part1.outputs:
    if char == 10:
        column = 0
        row = row + 1
        continue
    if char == 35:
        scaffolds.add(complex(column, row))
    column = column + 1

for scaffold in scaffolds:
    if all(scaffold + DIR in scaffolds for DIR in DIRS):
        intersections.append(scaffold)
sol = int(sum([(x.real * x.imag) for x in intersections]))
print("Part 1 solution: {}".format(sol))

# Part 2
program[0] = 2
part2 = intcode.Intcode(program)
# By inspection
path = """A,B,A,C,A,B,C,A,B,C
R,12,R,4,R,10,R,12
R,6,L,8,R,10
L,8,R,4,R,4,R,6
n
"""
part2.inputs = [ord(x) for x in path]
part2.run()
print("Part 2 solution: {}".format(part2.outputs[-1]))
