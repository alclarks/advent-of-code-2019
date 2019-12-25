import intcode

PASSWORD_START = "You should be able to get in by typing "
PASSWORD_END = " on the keypad"

# By playing the game:
PATH = """west
west
take bowl of rice
east
north
east
south
take dark matter
north
west
north
take candy cane
west
west
north
take dehydrated water
west
south
south"""

# Warnings for attempting automation:
#  - The geometry isn't a grid. In my maze there are squares from which you
#    can e.g. travel west, north, east then south and not finish on the
#    starting square.
#  - Some items will kill the droid.
#  - In my maze there's an "infinite loop" item that will put the Intcode VM
#    into (you guessed it) an infinite loop.

with open("inputs/day_25_input.txt") as f:
    program = [int(x) for x in f.read().split(",")]

droid = intcode.Intcode(program, [ord(x) for x in PATH])
droid.run()
output_dump = "".join([chr(x) for x in droid.outputs])
password = output_dump.split(PASSWORD_START)[1].split(PASSWORD_END)[0]
print("Part 1 solution: {}".format(password))
