import intcode

incs = [complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0)]

with open("inputs/day_11_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

def run_hull_painter(init_white_square=False):
    white_squares = {complex(0, 0)} if init_white_square else set()
    painted = set()
    direction = 0
    position = complex(0, 0)
    painter = intcode.Intcode(program)
    while not painter.finished:
        input = int(position in white_squares)
        while len(painter.outputs) < 2:
            painter.inputs.append(input)
            painter.run()
        if painter.outputs[0]:
            if position not in white_squares:
                painted.add(position)
                white_squares.add(position)
        else:
            if position in white_squares:
                white_squares.discard(position)
                painted.add(position)
        if painter.outputs[1]:
            direction = direction + 1
        else:
            direction = direction - 1
        position = position + incs[direction % 4]
        painter.inputs = []
        painter.outputs = []
    return white_squares, painted

# Part 1
_, painted = run_hull_painter()
print("Part 1 solution: {}".format(len(painted)))

# Part 2
white_squares, _ = run_hull_painter(True)

# Now render the grid
print("Part 2 solution:")
minx = int(min([com.real for com in white_squares]))
maxx = int(max([com.real for com in white_squares]))
miny = int(min([com.imag for com in white_squares]))
maxy = int(max([com.imag for com in white_squares]))
for i in range(miny, maxy+1):
    row = [" "]*(maxx - minx + 1)
    for comp in white_squares:
        if comp.imag == miny - i:
            row[int(comp.real) - 1] = "#"
    print("".join(row))
