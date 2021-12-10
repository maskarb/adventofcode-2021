import os
import sys
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class LanternFish:
    starting: int
    days: int = 8
    reproduce: bool = False

    def __post_init__(self):
        self.starting = int(self.starting)
        self.days = self.starting
        if self.days == 0:
            print('init fish with reproduce = True')
            self.reproduce = True

    def next_day(self, lis):
        if self.reproduce:
            lis.append(LanternFish(8))
            self.reproduce = False
            self.days = 6
        elif self.days > 0:
            self.days -= 1
            if self.days == 0:
                self.reproduce = True



def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def main_p1(filename):
    line = get_input(filename)[0].split(',')
    fish_list = [LanternFish(l) for l in line]

    for i in range(80):
        tmp_list = []
        for fish in fish_list:
            fish.next_day(tmp_list)
        fish_list.extend(tmp_list)
        print(f'result {i}: {len(fish_list)}')
    print(f'result: {len(fish_list)}')


def main_p2(filename):
    line = get_input(filename)[0].split(',')
    fish_count = [0] * 9
    for l in line:
        fish_count[int(l)] += 1

    for _ in range(256):
        # print(fish_count)
        fish_count[7] += fish_count[0]
        fish_count.append(fish_count[0])
        fish_count = fish_count[1:]

    print(f'result: {sum(fish_count)}')


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
