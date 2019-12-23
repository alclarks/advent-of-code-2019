import intcode

with open("inputs/day_13_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

# Part 1
part1 = intcode.Intcode(program)
part1.run()
print("Part 1 solution: {}".format(part1.outputs[2::3].count(2)))

# Part 2
score = 0
program[0] = 2
part2 = intcode.Intcode(program)
while not part2.finished:
    part2.run()
    squares = [part2.outputs[3*i:3*(i+1)] for i in range(len(part2.outputs) // 3)]
    for square in squares:
        if square[:2] == [-1, 0]:
            score = square[2]
        if square[2] == 3:
            paddle = square[:2]
        if square[2] == 4:
            ball = square[:2]
    if ball[0] > paddle[0]:
        part2.inputs.append(1)
    elif ball[0] < paddle[0]:
        part2.inputs.append(-1)
    else:
        part2.inputs.append(0)
    part2.outputs = []
print("Part 2 solution: {}".format(score))
