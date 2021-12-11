import os
import sys

def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main_p1(filename):
    line = get_input(filename)[0].split(',')
    line = [int(v) for v in line]
    line_len = len(line)
    minim, maxim = min(line), max(line)
    vals = [0] * (maxim - minim + 1)
    for i in range(minim, maxim+1):
        arr = [0] * line_len
        for j, v in enumerate(line):
            arr[j] = abs(v - i)
        vals[i] = arr
    sums = [sum(arr) for arr in vals]
    print(f'result: {min(sums)}')


def main_p2(filename):
    line = get_input(filename)[0].split(',')
    line = [int(v) for v in line]
    line_len = len(line)
    minim, maxim = min(line), max(line)
    vals = [0] * (maxim - minim + 1)
    for i in range(minim, maxim+1):
        arr = [0] * line_len
        for j, v in enumerate(line):
            arr[j] = sum(range(abs(v - i) + 1))
        vals[i] = arr
    sums = [sum(arr) for arr in vals]
    print(f'result: {min(sums)}')

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
