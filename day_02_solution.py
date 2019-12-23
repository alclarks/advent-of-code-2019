import intcode

with open("inputs/day_02_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

# Part 1
p1_program = program.copy()
p1_program[1] = 12
p1_program[2] = 2
part1 = intcode.Intcode(p1_program)
part1.run()
print("Part 1 solution: {}".format(part1.m[0]))

# Part 2
# I don't see a better way to do this than brute force
for noun in range(100):
    for verb in range(100):
        p2_program = program.copy()
        p2_program[1] = noun
        p2_program[2] = verb
        part2 = intcode.Intcode(p2_program)
        part2.run()
        if part2.m[0] == 19690720:
            print("Part 2 solution: {}".format(100*noun+verb))
            break
    else:
        continue
    break
