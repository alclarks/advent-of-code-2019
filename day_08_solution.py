width = 25
height = 6
res = width * height

with open("inputs/day_08_input.txt") as f:
    img = [int(x) for x in f.read().strip()]
no_layers = int(len(img) / res)

layers = [None] * no_layers
for i in range(no_layers):
    layers[i] = img[i*res:(i+1)*res]

# Fingers crossed for a unique minimum
zeros = [layer.count(0) for layer in layers]
min_lay = layers[zeros.index(min(zeros))]
print("Part 1 solution: {}".format(min_lay.count(1) * min_lay.count(2)))

pixels = [None] * res
for i in range(res):
    pixels[i] = img[i::res]
    pixels[i] = [x for x in pixels[i] if x != 2]
processed = [pixel[0] for pixel in pixels]

print("Part 2 solution:")
for i in range(height):
    print("".join((" " if x == 0 else "#") for x in processed[i*width:(i+1)*width]))
