def solve(input):
    table = [[0 for x in range(10000)] for y in range(10000)]
    x = len(table) / 2
    y = len(table) / 2

    directionsX = [1, 0, -1, 0]
    directionsY = [0, 1, 0, -1]

    directionIndex = 0

    stepsInDirection = 0
    directionStep = 1
    timesReachedDirectionStep = 0

    # populate
    value = 1
    table[x][y] = value
    valueReached = False

    while not valueReached:
        x = x + directionsX[directionIndex]
        y = y + directionsY[directionIndex]

        value = sumAdjacentSquares(table, x, y)
        table[x][y] = value

        stepsInDirection = stepsInDirection + 1
        if stepsInDirection == directionStep:
            timesReachedDirectionStep = timesReachedDirectionStep + 1
            if timesReachedDirectionStep == 2:
                directionStep = directionStep + 1
                timesReachedDirectionStep = 0

            stepsInDirection = 0
            directionIndex = (directionIndex + 1) % len(directionsX)

        if value > input:
            valueReached = True


    print value

def sumAdjacentSquares(table, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            row = (x + i) % len(table)
            sum = sum + table[row][(y + j) % len(table[row])]
    return sum


input = 347991

solve(input)
