import intcode

def run_driod(x, y):
    droid = intcode.Intcode(program, [x, y])
    droid.run()
    return droid.outputs[0]

with open("day_19_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

# Part 1
count = sum([run_driod(i, j) for i in range(50) for j in range(50)])
print("Part 1 solution: {}".format(count))

# Part 2
x = 160
y = 200
while True:
    y = y + 1
    if run_driod(x, y) == 0:
        x = x + 1
    if (run_driod(x+99, y-99) == 1):
        break
print("Part 2 solution: {}".format(10000*x + (y - 99)))
