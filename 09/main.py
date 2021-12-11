import os
import sys

import numpy as np

def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main_p1(filename):
    lines = get_input(filename)
    m = np.array([[int(v) for v in line.strip()] for line in lines]).transpose()

    x_max, y_max = m.shape

    def get_value(x, y):
        if x < 0 or y < 0 or x > x_max-1 or y > y_max-1:
            return 9
        else:
            return m[x, y]

    count = 0
    for x in range(x_max):
        for y in range(y_max):
            p = m[x, y]
            if (
                get_value(x+1, y) > p
                and get_value(x-1, y) > p
                and get_value(x, y-1) > p
                and get_value(x, y+1) > p
            ):
                count += 1 + p
    print(f"result: {count}")

def main_p2(filename):
    lines = get_input(filename)
    m = np.array([[int(v) for v in line.strip()] for line in lines]).transpose()
    x_max, y_max = m.shape

    m2 = np.zeros(m.shape)

    def floodFill(x, y):
        def get_value(x, y):
            if x < 0 or y < 0 or x > x_max-1 or y > y_max-1:
                return 9
            else:
                return m[x, y]

        # Base cases
        if get_value(x, y) == 9 or m2[x, y] == 1:
            return

        # Replace the color at (x, y)
        m2[x, y] = 1

        # Recur for north, east, south and west
        floodFill(x + 1, y)
        floodFill(x - 1, y)
        floodFill(x, y + 1)
        floodFill(x, y - 1)

    basin_sizes = []
    for x in range(x_max):
        for y in range(y_max):
            current_m2_sum = np.sum(m2)
            if m2[x, y] == 1:
                continue
            floodFill(x, y)
            basin_sizes.append(np.sum(m2) - current_m2_sum)

    result = 1
    for v in sorted(basin_sizes, reverse=True)[:3]:
        result *= v
    print(f"result: {result}")



if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ('p1', 'p2'):
        print('you done did it wrong')
        exit()
    filename = os.path.join(sys.argv[0].split('/', 1)[0], 'input.txt')
    part = sys.argv[1]
    if part == 'p1':
        main_p1(filename)
    elif part == 'p2':
        main_p2(filename)
