from collections import defaultdict
from copy import deepcopy

ADJS = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]
STEPS = 200
LAYERS = STEPS + 1

OUTER_TOP = (0, 1, 2, 3, 4)
OUTER_RIGHT = (4, 9, 14, 19, 24)
OUTER_LEFT = (0, 5, 10, 15, 20)
OUTER_BOTTOM = (20, 21, 22, 23, 24)

def parse_input():
    with open("inputs/day_24_input.txt") as f:
        state = defaultdict(lambda: ".")
        lines = [line.strip() for line in f.readlines()]
        for i, row in enumerate(lines):
            for j, char in enumerate(row):
                state[complex(j, i)] = char
        return state

def index_to_coordinates(index):
    return complex(index % 5, index // 5)

def adjacent_bugs(index, layer_num, state):
    """ Yep - it's this ugly."""
    def _get(l, i):
        return state[layer_num+l][index_to_coordinates(i)]
    neighbours = []
    pos = index_to_coordinates(index)
    # Outer layer
    if index == 0:
        neighbours = [_get(-1, 7), _get(-1, 11), _get(0, 1), _get(0, 5)]
    elif index in (1, 2, 3):
        neighbours = [_get(-1, 7), _get(0, index-1), _get(0, index+1), _get(0, index+5)]
    elif index == 4:
        neighbours = [_get(-1, 7), _get(-1, 13), _get(0, 3), _get(0, 9)]
    elif index in (5, 10, 15):
        neighbours = [_get(-1, 11), _get(0, index-5), _get(0, index+5), _get(0, index+1)]
    elif index in (9, 14, 19):
        neighbours = [_get(-1, 13), _get(0, index-5), _get(0, index+5), _get(0, index-1)]
    elif index == 20:
        neighbours = [_get(-1, 17), _get(-1, 11), _get(0, 15), _get(0, 21)]
    elif index in (21, 22, 23):
        neighbours = [_get(-1, 17), _get(0, index-1), _get(0, index+1), _get(0, index-5)]
    elif index == 24:
        neighbours = [_get(-1, 17), _get(-1, 13), _get(0, 19), _get(0, 23)]
    # Inners
    elif index == 7:
        neighbours = [_get(1, x) for x in OUTER_TOP] + [_get(0, 2), _get(0, 6), _get(0, 8)]
    elif index == 11:
        neighbours = [_get(1, x) for x in OUTER_LEFT] + [_get(0, 6), _get(0, 10), _get(0, 16)]
    elif index == 13:
        neighbours = [_get(1, x) for x in OUTER_RIGHT] + [_get(0, 8), _get(0, 14), _get(0, 18)]
    elif index == 17:
        neighbours = [_get(1, x) for x in OUTER_BOTTOM] + [_get(0, 16), _get(0, 18), _get(0, 22)]
    # Normal 
    elif index in (6, 8, 16, 18):
        neighbours = [_get(0, index+1), _get(0, index-1), _get(0, index+5), _get(0, index-5)]
    return sum([neighbour == "#" for neighbour in neighbours])

def find_new_layer(state, layer_num):
    new_layer = defaultdict(lambda: ".")
    for i in range(25):
        pos = index_to_coordinates(i)
        bugs = adjacent_bugs(i, layer_num, state)
        if state[layer_num][pos] == "#":
            if bugs == 1:
                new_layer[pos] = "#"
            else:
                new_layer[pos] = "."
        if state[layer_num][pos] == ".":
            if bugs in (1, 2):
                new_layer[pos] = "#"
            else:
                new_layer[pos] = "."
    return new_layer

def part2():
    state = {}
    state[0] = parse_input()
    for i in range(1, LAYERS + 1):
        state[i] = defaultdict(lambda: ".")
        state[-i] = defaultdict(lambda: ".")
    new_state = {}
    for i in range(STEPS):
        new_state = deepcopy(state)
        for j in range(-i-1, i+2):
            new_state[j] = find_new_layer(state, j)
        state = deepcopy(new_state)
    bugs = 0
    for i in range(-LAYERS + 1, LAYERS):
        bugs = bugs + list(state[i].values()).count("#")
    return bugs

print("Part 2 solution: {}".format(part2()))
