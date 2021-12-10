import os
import sys
from collections import defaultdict
from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Point:
    X: int
    Y: int
    def __post_init__(self):
        object.__setattr__(self, 'X', int(self.X))
        object.__setattr__(self, 'Y', int(self.Y))

@dataclass
class Line:
    P1: Point
    P2: Point

    def next_point(self):
        min_point, max_point = sorted([self.P1, self.P2])
        if self.P1.X == self.P2.X:
            for i in range(min_point.Y, max_point.Y+1):
                yield Point(self.P1.X, i)
        elif self.P1.Y == self.P2.Y:
            for i in range(min_point.X, max_point.X+1):
                yield Point(i, self.P1.Y)

@dataclass
class Line2:
    P1: Point
    P2: Point
    def next_point(self):
        min_point, max_point = sorted([self.P1, self.P2])
        if self.P1.X == self.P2.X and self.P1.Y != self.P2.Y:
            for i in range(min_point.Y, max_point.Y+1):
                yield Point(self.P1.X, i)
        elif self.P1.Y == self.P2.Y and self.P1.X != self.P2.X:
            for i in range(min_point.X, max_point.X+1):
                yield Point(i, self.P1.Y)
        elif self.P1.X - self.P2.X == -(self.P1.Y - self.P2.Y):
            for i, j in zip(range(min_point.X, max_point.X+1), range(min_point.Y, max_point.Y-1, -1)):
                yield Point(i, j)
        elif self.P1.X - self.P2.X == self.P1.Y - self.P2.Y:
            for i, j in zip(range(min_point.X, max_point.X+1), range(min_point.Y, max_point.Y+1)):
                yield Point(i, j)


def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main_p1(filename):
    entries = get_input(filename)
    lines = []
    grid = defaultdict(int)
    for entry in entries:
        first, _, second = entry.split()
        p1 = Point(*first.split(','))
        p2 = Point(*second.split(','))
        if p1.X == p2.X or p1.Y == p2.Y:
            lines.append(Line(p1, p2))
    for line in lines:
        for v in line.next_point():
            grid[v] += 1

    print(f'result: {sum(v >= 2 for v in grid.values())}')


def main_p2(filename):
    entries = get_input(filename)
    lines = []
    grid = defaultdict(int)
    for entry in entries:
        first, _, second = entry.split()
        p1 = Point(*first.split(','))
        p2 = Point(*second.split(','))
        lines.append(Line2(p1, p2))
    for line in lines:
        for v in line.next_point():
            grid[v] += 1

    print(f'result: {sum(v >= 2 for v in grid.values())}')

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
