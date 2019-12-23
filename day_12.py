import itertools
import numpy

class Moon():
    def __init__(self, position):
        self.position = position
        self.velocity = [0, 0, 0]
        self.accel = [0, 0, 0]
    
    def energy(self):
        return sum(map(abs, self.position)) * sum(map(abs, self.velocity))

    def update_accel(self, other):
        for i in range(3):
            if self.position[i] > other.position[i]:
                self.accel[i] = self.accel[i] - 1
            elif self.position[i] < other.position[i]:
                self.accel[i] = self.accel[i] + 1

    def update_vel(self):
        self.velocity = [sum(x) for x in zip(self.velocity, self.accel)]
        self.accel = [0, 0, 0]

def update(system):
    # Update velocity from gravity
    for pair in itertools.permutations(system, 2):
        pair[0].update_accel(pair[1])
    for moon in system:
        moon.update_vel()
    # Update position from velocity
    for moon in system:
        moon.position = [sum(x) for x in zip(moon.position, moon.velocity)]

A, B, C, D = [9, 13, -8], [-3, 16, -17], [-4, 11, -10], [0, -2, -2]

# Part 1:
sys = [Moon(A), Moon(B), Moon(C), Moon(D)]
steps = 1000
for _ in range(steps):
    update(sys)
print("Part 1 solution: {}".format(sum([moon.energy() for moon in sys])))

# Part 2
initpos = [[9, -3, -4, 0], [13, 16, 11, -2], [-8, -17, -10, -2]]
sys = [Moon(A), Moon(B), Moon(C), Moon(D)]
periods = [0, 0, 0]
i = 0
while not all(periods):
    update(sys)
    i = i + 1
    for j in range(3):
        if (all([(moon.velocity[j] == 0) for moon in sys])
            and [moon.position[j] for moon in sys] == initpos[j]
            and not periods[j]):
            periods[j] = i
period = numpy.lcm(periods[0], numpy.lcm(periods[1], periods[2]))
print("Part 2 solution: {}".format(period))