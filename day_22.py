class ModularLinearFunc():
    def __init__(self, a, b, p):
        self.a = a % p
        self.b = b % p
        self.p = p
    
    def apply(self, x):
        return (self.a * x + self.b) % self.p

    def solve(self, y):
        return pow(self.a, -1, self.p) * (y - self.b) % self.p

def compose(func1, func2):
    assert func1.p == func2.p
    p = func1.p
    return ModularLinearFunc((func2.a * func1.a) % p,
                             (func2.a * func1.b + func2.b) % p,
                             p)

def self_compose(func1, n):
    b = func1.b * (pow(func1.a, n, func1.p) - 1) * pow(func1.a - 1, -1, func1.p)
    return ModularLinearFunc(pow(func1.a, n, func1.p),
                             b,
                             func1.p)

def compose_input(size):
    with open("inputs/day_22_input.txt") as f:
        shuffles = [x.strip() for x in f.readlines()]
    shuffle_func = ModularLinearFunc(1, 0, size)
    for shuffle in shuffles:
        if shuffle == "deal into new stack":
            next_func = ModularLinearFunc(-1, size - 1, size)
        elif shuffle.startswith("deal with increment "):
            n = int(shuffle[len("deal with increment "):])
            next_func = ModularLinearFunc(n, 0, size)
        elif shuffle.startswith("cut "):
            n = int(shuffle[len("cut "):])
            next_func = ModularLinearFunc(1, size - n, size)
        shuffle_func = compose(shuffle_func, next_func)
    return shuffle_func

# Part 1
overall = compose_input(10007)
print("Part 1 solution: {}".format(overall.apply(2019)))

# Part 2
repeated = self_compose(compose_input(119315717514047), 101741582076661)
print("Part 2 solution: {}".format(repeated.solve(2020)))