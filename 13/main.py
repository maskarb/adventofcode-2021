import math
import os
import sys
from dataclasses import dataclass

import numpy as np

def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()

@dataclass
class Fold:
    axis: int
    index: int

    def __post_init__(self):
        self.axis = 1 if self.axis == 'x' else 0
        self.index = int(self.index)


def main_p1(filename):
    lines = get_input(filename)
    points = []
    folds = []
    for line in lines:
        if ',' not in line:
            if 'fold along' in line:
                folds.append(Fold(*line.split('fold along ')[1].split('=')))
            continue
        x, y = line.split(',')
        points.append([int(x), int(y)])
    x_max = max(p[0] for p in points) + 1
    y_max = max(p[1] for p in points) + 1

    m = np.zeros((x_max, y_max))

    for point in points:
        x, y = point
        m[x, y] = 1

    m = m.transpose()

    for i, fold in enumerate(folds):
        m1, _, m2 = np.split(m, [fold.index, fold.index+1], axis=fold.axis)
        m2 = np.flip(m2, axis=fold.axis)
        if m1.shape != m2.shape:
            smaller, larger = (m1, m2) if m1.shape[fold.axis] < m2.shape[fold.axis] else (m2, m1)
            padding = abs(m1.shape[fold.axis] - m2.shape[fold.axis])
            padding_arr = [(0, 0), (0, 0)]
            padding_arr[fold.axis] = (padding, 0)
            z = np.pad(smaller, padding_arr)
            m1, m2 = larger, z
        m = m1 + m2

        if i == 0:
            res = sum(sum(1 if x else 0 for x in row) for row in m)
            print(f'result p1: {res}')

    for row in m:
        string = ''.join('\u2593' if x else '\u2591' for x in row)
        print(string)


def main_p2(filename):
    pass

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
