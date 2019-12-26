from collections import defaultdict
ADJS = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]

def parse_input():
    with open("inputs/day_24_input.txt") as f:
        # Pad state with empty squares
        state = defaultdict(lambda: ".")
        lines = [line.strip() for line in f.readlines()]
        for i, row in enumerate(lines):
            for j, char in enumerate(row):
                state[complex(j, i)] = char
        return state

def index_to_coordinates(index):
    return complex(index % 5, index // 5)

def adjacent_bugs(index, state):
    adjacents = [index_to_coordinates(index) + adj for adj in ADJS]
    return sum([state[adj] == "#" for adj in adjacents])

def find_new_state(state):
    new_state = defaultdict(lambda: ".")
    for i in range(25):
        pos = index_to_coordinates(i)
        bugs = adjacent_bugs(i, state)
        if state[pos] == "#":
            if bugs == 1:
                new_state[pos] = "#"
            else:
                new_state[pos] = "."
        if state[pos] == ".":
            if bugs in (1, 2):
                new_state[pos] = "#"
            else:
                new_state[pos] = "."
    return new_state

def bio_div(state):
    score = 0
    for i in range(25):
        pos = index_to_coordinates(i)
        if state[pos] == "#":
            score = score + pow(2, i)
    return score

def part1():
    state = parse_input()
    scores = [bio_div(state)]
    while True:
        new_state = find_new_state(state)
        state = new_state
        score = bio_div(state)
        if score in scores:
            return score
        scores.append(score)

print("Part 1 solution: {}".format(part1()))
