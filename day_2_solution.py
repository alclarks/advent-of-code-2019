def run_Intcode(m):
    ptr = 0
    while True:
        opcode = m[ptr]
        if opcode == 1:
            m[m[ptr+3]] = m[m[ptr+1]] + m[m[ptr+2]]
            ptr = ptr + 4
        elif opcode == 2:
            m[m[ptr+3]] = m[m[ptr+1]] * m[m[ptr+2]]
            ptr = ptr + 4
        elif opcode == 99:
            return m
        else:
            # Invalid opcode
            return None

with open("day_2_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

# Part 1
p1_program = program.copy()
p1_program[1] = 12
p1_program[2] = 2
print("Part 1 solution {}".format(run_Intcode(p1_program)[0]))

# Part 2
# I don't see a better way to do this than brute force
for noun in range(100):
    for verb in range(100):
        p2_program = program.copy()
        p2_program[1] = noun
        p2_program[2] = verb
        try:
            output = run_Intcode(p2_program)[0] 
        except TypeError:
            # Hit an invalid opcode, ignore
            pass
        if output == 19690720:
            print("Part 2 solution: {}".format(100*noun+verb))
            break
    else:
        continue
    break

