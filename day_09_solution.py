import intcode

with open("day_09_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

# Part 1
part1 = intcode.Intcode(program, [1])
part1.run()
print("Part 1 solution: {}".format(part1.outputs[0]))

# Part 1
part1 = intcode.Intcode(program, [2])
part1.run()
print("Part 2 solution: {}".format(part1.outputs[0]))
