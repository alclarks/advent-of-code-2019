import intcode

with open("day_05_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

part1 = intcode.Intcode(program, [1])
part1.run()
print("Part 1 solution: {}".format(part1.outputs[-1]))
part2 = intcode.Intcode(program, [5])
part2.run()
print("Part 2 solution: {}".format(part2.outputs[0]))
