import itertools

import intcode

with open("inputs/day_07_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

# Part 1
max_thrust = 0
for perm in itertools.permutations([0, 1, 2, 3, 4]):
    thrust = 0
    for i in range(5):
        comp = intcode.Intcode(program, [perm[i], thrust])
        comp.run()
        thrust = comp.outputs[0]
    if thrust > max_thrust:
        max_thrust = thrust
print("Part 1 solution: {}".format(max_thrust))

# Part 2
max_thrust = 0
for perm in itertools.permutations([5, 6, 7, 8, 9]):
    thrust = 0
    amps = [intcode.Intcode(program, [mode]) for mode in perm]
    while not amps[-1].finished:
        for amp in amps:
            amp.inputs.append(thrust)
            amp.run()
            thrust = amp.outputs[-1]
    if thrust > max_thrust:
        max_thrust = thrust
print("Part 2 solution: {}".format(max_thrust))
