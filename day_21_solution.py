import intcode

with open("inputs/day_21_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

def run_spring_droid(script):
    springdriod = intcode.Intcode(program, [ord(x) for x in script])
    springdriod.run()
    return springdriod.outputs[-1]

# Part 1
part1 = """OR A J
AND B J
AND C J
NOT J J
AND D J
WALK
"""
print("Part 1 solution: {}".format(run_spring_droid(part1)))

# Part 2
part2 = """OR A J
AND B J
AND C J
NOT J J
AND D J
NOT E T
AND H T
OR E T
AND T J
RUN
"""
print("Part 2 solution: {}".format(run_spring_droid(part2)))