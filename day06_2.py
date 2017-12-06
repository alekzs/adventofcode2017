import math

def solve(input):
    configsSeen = []
    config = [int(a) for a in input.split("    ")]
    configsSeen.append(config[:])
    stateSeenAgain = False
    loopState = None
    cycles = 0

    while not stateSeenAgain:
        next = max(config)
        nextIndex = config.index(next)
        redistAmount = max(math.ceil(next / len(config)), 1)

        config[nextIndex] = 0
        nextIndex = (nextIndex + 1) % len(config)

        while next > 0:
            config[nextIndex] += redistAmount
            next -= redistAmount
            nextIndex = (nextIndex + 1) % len(config)

        cycles = cycles + 1

        if config in configsSeen:
            if loopState == config:
                stateSeenAgain = True

            if not loopState:
                loopState = config[:]
                cycles = 0
        else:
            configsSeen.append(config[:])

    print cycles

input = """5    1    10    0    1    7    13    14    3    12    8    10    7    12    0    6"""
#input = """0    2    7    0"""

solve(input)
