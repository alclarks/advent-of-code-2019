from collections import defaultdict

# There's only around 1000 entries here, so recursion is fine
def rec_orb_count(start, depth):
    count = depth
    for sat in child_dict[start]:
        count = count + rec_orb_count(sat, depth+1)
    return count

def path_seek(start, finish):
    path1 = []
    path2 = []
    parent = start
    while parent != "COM":
        path1.insert(0, parent)
        parent = par_dict[parent]
    parent = finish
    while parent != "COM":
        path2.insert(0, parent)
        parent = par_dict[parent]
    return len(set(path1) ^ set(path2)) - 2

with open("day_06_input.txt") as f:
    orbits = f.read().splitlines()

child_dict = defaultdict(list)
par_dict = defaultdict(str)
for orbit in orbits:
    info = orbit.split(")")
    child_dict[info[0]].append(info[1])
    par_dict[info[1]] = info[0]

print("Part 1 solution: {}".format(rec_orb_count("COM", 0)))
print("Part 2 solution: {}".format(path_seek("YOU", "SAN")))
