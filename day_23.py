import intcode

NETWORK_SIZE = 50
with open("inputs/day_23_input.txt") as f:
    PROGRAM = [int(x) for x in f.read().split(",")]

def three_split(input_list):
    return [input_list[i:i + 3] for i in range(0, len(input_list), 3)]

def get_packets(queue, i):
    to_i = []
    not_to_i = []
    for packet in queue:
        if packet[0] == i:
            to_i.append(packet)
        else:
            not_to_i.append(packet)
    return to_i, not_to_i

def initialise_network():
    network = NETWORK_SIZE * [None]
    for i in range(NETWORK_SIZE):
        network[i] = intcode.Intcode(PROGRAM, [i])
        network[i].run()
    packet_queue = []
    for comp in network:
        packet_queue = packet_queue + three_split(comp.outputs)
    return network, packet_queue

def run_network(network, packet_queue, return_first_255):
    "Takes network state,"
    while True:
        for i, comp in enumerate(network):
            while True:
                to_comp, packet_queue = get_packets(packet_queue, i)
                to_nat, _ = get_packets(packet_queue, 255)
                if return_first_255 and len(to_nat) > 0:
                    return to_nat[0][2]
                if len(to_nat) > 0:
                    nat_cache = to_nat[-1]
                for packet in to_nat:
                    packet_queue.remove(packet)
                if len(to_comp) == 0:
                    comp.inputs = [-1]
                else:
                    for packet in to_comp:
                        comp.inputs = comp.inputs + packet[1:]
                comp.run()
                if len(comp.outputs) == 0:
                    break
                packet_queue = packet_queue + three_split(comp.outputs)
                comp.outputs = []
        if len(packet_queue) == 0:
            break
    return network, packet_queue, nat_cache

def part1():
    return run_network(*initialise_network(), True)

def part2():
    network, packet_queue = initialise_network()
    sent_from_nat = []
    while True:
        network, packet_queue, nat_cache = run_network(network, packet_queue, False)
        network[0].inputs = nat_cache[1:]
        network[0].run()
        packet_queue = packet_queue + three_split(network[0].outputs)
        network[0].outputs = []
        sent_from_nat.append(nat_cache[2])
        if len(sent_from_nat) >= 2:
            if sent_from_nat[-1] == sent_from_nat[-2]:
                return sent_from_nat[-1]

print("Part 1 solution: {}".format(part1()))
print("Part 2 solution: {}".format(part2()))
