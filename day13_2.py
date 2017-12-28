# stole this one from https://www.reddit.com/r/adventofcode/comments/7jgyrt/2017_day_13_solutions/dr6cl6z/ because I gave up

def solve(data):
    layers = [tuple(map(int,d.split(': '))) for d in data.split('\n')]
    i = 0
    while True:
        for layer in layers:
            if (i + layer[0]) % (2 * (layer[1] - 1)) == 0:
                break
        else:
            return i
        i += 1

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

print solve(input)
