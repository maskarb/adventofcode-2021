import os
import sys
from dataclasses import dataclass

@dataclass
class Pilot:
    movement: str
    distance: int

    def __post_init__(self):
        self.distance = int(self.distance)

def get_input(filename):
    with open(filename, 'r') as f:
        return [Pilot(*v.split(' ')) for v in f.readlines()]

def main_p1(filename):
    lis = get_input(filename)
    depth = 0
    horizontal = 0
    for i in lis:
        match i.movement:
            case 'forward':
                horizontal += i.distance
            case 'up':
                depth -= i.distance
            case 'down':
                depth += i.distance

    print(depth * horizontal)


def main_p2(filename):
    lis = get_input(filename)
    aim = 0
    depth = 0
    horizontal = 0
    for i in lis:
        match i.movement:
            case 'forward':
                horizontal += i.distance
                depth += aim * i.distance
            case 'up':
                aim -= i.distance
            case 'down':
                aim += i.distance

    print(depth * horizontal)


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
