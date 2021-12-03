import os
import sys

def main_p1(filename):
    with open(filename, 'r') as f:
        count = 0
        prev = int(f.readline())
        for l in f.readlines():
            cur = int(l)
            if cur > prev:
                count += 1
            prev = cur
    print(count)

def main_p2(filename):
    with open(filename, 'r') as f:
        lis = [int(v) for v in f.readlines()]
    prev = sum(lis[0:3])
    mod_lis = len(lis) % 3
    count = 0
    for i in range(1, len(lis) - mod_lis + 1):
        cur = sum(lis[i:i+3])
        if cur > prev:
            count += 1
        prev = cur
    print(count)

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
