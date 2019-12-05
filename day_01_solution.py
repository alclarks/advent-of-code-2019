def naive_fuel_from_mass(mass):
    return mass//3 - 2

def fuel_from_mass(mass):
    sum = 0
    fuel = naive_fuel_from_mass(mass)
    while fuel > 0:
        sum = sum + fuel
        fuel = naive_fuel_from_mass(fuel)
    return sum

with open("day_1_input.txt") as f:
    masses = f.read().splitlines()

# Part 1
fuel = 0
for mass in masses:
    fuel = fuel + naive_fuel_from_mass(int(mass))
print("Part 1 solution: {}".format(fuel))

# Part 2
fuel = 0
for mass in masses:
    fuel = fuel + fuel_from_mass(int(mass))
print("Part 2 solution: {}".format(fuel))

