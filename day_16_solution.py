import numpy as np

def read_file():
    with open("day_16_input.txt") as f:
        return [int(x) for x in f.read().strip()]

def get_pattern_matrix(i, j):
    base = [0, 1, 0, -1]
    return base[((j + 1) // (i + 1)) % len(base)]

# Part 1
signal = read_file()
length = len(signal)
matrix = np.array([[get_pattern_matrix(i, j) for j in range(length)] for i in range(length)])
signal = np.array([[x] for x in signal])
for _ in range(100):
    signal = matrix.dot(signal)
    signal = np.array([[abs(x[0]) % 10] for x in signal])

part1 = "".join(str(x[0]) for x in signal[:8])
print("Part 1 solution: {}".format(part1))

# Part 2
# In quadrants, M = [[A, B], [0, C]] where C is upper triangular with just 1s.
# The solution to part 1 puts the solution of part 2 in the second half of the
# signal, so we can just add adjacent elements instead of doing the full matrix
# multiplication. There's also no negative numbers to worry about.
signal = read_file()
offset = int("".join(str(x) for x in signal[:7]))
tail_length = length * 10000 - offset
q, r = divmod(tail_length, length)
signal.reverse()
tail = q * signal + signal[:r]
tail.reverse()
for _ in range(100):
    for i in range(tail_length - 1, 0, -1):
        tail[i-1] = (tail[i-1] + tail[i]) % 10
print("Part 2 solution: {}".format("".join(str(x) for x in tail[:8])))
