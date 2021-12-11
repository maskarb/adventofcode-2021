import os
import sys
from collections import defaultdict

COUNT_MAP = {
    'a': 8,
    'b': 6,
    'c': 8,
    'd': 7,
    'e': 4,
    'f': 9,
    'g': 7,
}

NUMBER_MAP = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

def get_from_count_map(v_in):
    return [k for k,v in COUNT_MAP.items() if v_in == v]

def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main_p1(filename):
    lines = get_input(filename)
    counter = 0
    for line in lines:
        vals = line.split('|')[1].split()
        print(vals)
        for val in vals:
            if len(val) in [2, 3, 4, 7]:
                counter += 1
    print(f'result: {counter}')


def main_p2(filename):
    lines = get_input(filename)
    final_lis = []
    len_2 = ''
    len_3 = ''
    len_4 = ''
    for line in lines:
        values_from_file = line.split('|')
        vals = values_from_file[0].split()
        num_map = {}
        values = defaultdict(int)
        for val in vals:
            for v in val:
                values[v] += 1
            match len(val):
                case 2:
                    len_2 = val
                case 3:
                    len_3 = val
                case 4:
                    len_4 = val

        for k,v in values.items():
            if v in [4, 6, 9]:
                key = get_from_count_map(v)[0]
                num_map[key] = k
        for c in len_3:
            if c not in len_2:
                num_map['a'] = c
                break
        for c in len_2:
            if c not in num_map.values():
                num_map['c'] = c
                break
        for c in len_4:
            if c not in len_3 and c not in num_map.values():
                num_map['d'] = c
                break
        for c in 'abcdefg':
            if c not in num_map.values():
                num_map['g'] = c

        key_map = {}
        for k, v in NUMBER_MAP.items():
            tmp = ''
            for c in k:
                tmp += num_map[c]
            key = ''.join(sorted(tmp))
            key_map[key] = v

        new_vals = values_from_file[1].split()
        tmp = ''
        for val in new_vals:
            s = ''.join(sorted(val))
            tmp += str(key_map[s])
        final_lis.append(int(tmp))

    print(f'result: {sum(final_lis)}')

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
