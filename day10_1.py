
def solve(input):
    pos = 0
    skipSize = 0
    
    items = [x for x in range(256)]

    inputs = [int(y) for y in input.split(",")]

    for length in inputs:
        target = pos + length
        subtarget = 0
        section = items[pos:target]
        subsection = []
        if target >= len(items):
            subtarget = target % len(items)
            subsection = items[0:subtarget]

        whole = list(reversed(section + subsection))
        section = whole[0:len(section)]
        subsection = whole[len(section):len(whole)]
        items[pos:target] = section
        if subtarget != 0:
            items[0:subtarget] = subsection
        pos += length
        pos += skipSize
        pos = pos % len(items)
        skipSize += 1

    print items[0] * items[1]

input = "94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243"

solve(input)
