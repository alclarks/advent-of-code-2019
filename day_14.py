import math
import itertools
import collections

def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    equations = [line.split(" => ") for line in lines]
    reactions = {}
    for equation in equations:
        product = equation[1].split()
        reactions[product[1]] = {"yeild": int(product[0]), "reactants": {}}
        inputs = equation[0].split(", ")
        for input in inputs:
            info = input.split()
            reactions[product[1]]["reactants"][info[1]] = int(info[0])
    return reactions

def list_ingredients(reaction_dict):
    list_of_dicts = [reaction["reactants"] for reaction in reaction_dict.values()]
    return list(itertools.chain(*[list(chem_set.keys()) for chem_set in list_of_dicts]))

def find_req_ore(fuel):
    reactions = parse_file("inputs/day_14_input.txt")
    inventory = collections.defaultdict(int)
    inventory["FUEL"] = fuel  # We'll work backwards
    while list(inventory.keys()) != ["ORE"]:
        for product in dict(inventory):
            ingredients = list_ingredients(reactions)
            if product not in ingredients and ingredients:
                batches = math.ceil(inventory[product] / reactions[product]["yeild"])
                for input_name, input_quant in reactions[product]["reactants"].items():
                    inventory[input_name] = inventory[input_name] + input_quant * batches
                reactions.pop(product)
                inventory.pop(product)
    return inventory["ORE"]

def bisect(lower_bound, upper_bound, f, target):
    # Assumes increasing function
    mid = int((lower_bound + upper_bound) / 2)
    f_mid = f(mid)
    if f_mid > target:
        return lower_bound, mid
    else:
        return mid, upper_bound

# Part 1
part1 = find_req_ore(1)
print("Part 1 solution: {}".format(part1))

# Part 2
# Use interval bisection. Lower bound can be 1 trillion/(part 1), since bigger
# inputs will smooth leftover inefficiencies. Just choose a big upper bound.
TRILLION = 1000000000000
lower_bound = int(TRILLION / part1)
upper_bound = 2 * lower_bound
assert find_req_ore(upper_bound) > TRILLION

while (upper_bound - lower_bound != 1):
    lower_bound, upper_bound = bisect(lower_bound, upper_bound, find_req_ore, TRILLION)

print("Part 2 solution: {}".format(lower_bound))