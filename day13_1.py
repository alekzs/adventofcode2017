packetIndex = -1
totalSeverity = 0

def checkCaught(layers):
    global packetIndex
    global totalSeverity
    if packetIndex not in layers:
        return
    if (layers[packetIndex]["idx"] == 0):
        totalSeverity += packetIndex * layers[packetIndex]["range"]

def moveScanner(layers):
    for (key, value) in layers.iteritems():
        value["idx"] = (value["idx"] + 1 * value["dir"])
        if (value["idx"] == value["range"] - 1 or value["idx"] == 0):
            value["dir"] *= -1

def movePacket(layers):
    global packetIndex
    packetIndex += 1

    checkCaught(layers)

def solve(input):
    global totalSeverity
    layers = {}

# parse
    for line in input.split("\n"):
        depth = int(line.strip().split(": ")[0])
        range = int(line.strip().split(": ")[1])
        layers[depth] = { "range": range, "idx": 0, "dir": 1 }

    picoseconds = max(layers.keys()) + 1
    for i in xrange(picoseconds):
        movePacket(layers)
        moveScanner(layers)


#print layers
    print totalSeverity


input = """0: 3
    1: 2
    2: 4
    4: 8
    6: 5
    8: 6
    10: 6
    12: 4
    14: 6
    16: 6
    18: 17
    20: 8
    22: 8
    24: 8
    26: 9
    28: 8
    30: 12
    32: 12
    34: 10
    36: 12
    38: 12
    40: 8
    42: 12
    44: 12
    46: 10
    48: 12
    50: 12
    52: 14
    54: 14
    56: 12
    58: 14
    60: 14
    62: 14
    64: 14
    66: 14
    68: 12
    70: 14
    72: 14
    74: 14
    76: 14
    80: 18
    82: 14
    90: 18"""

solve(input)
