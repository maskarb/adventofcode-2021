import copy
import os
import sys

def get_input(filename):
    with open(filename, 'r') as f:
        lis = f.readlines()
        return [v.strip() for v in lis]

def filter_lis(lis, filt, i):
    return [v for v in lis if v[i] == str(filt)]

def main_p1(filename):
    lis = get_input(filename)
    len_bin = len(lis[0])
    gamma = ''  # most common
    epsilon = ''  # least common
    for i in range(len_bin-1):
        zeros = 0
        ones = 0
        for v in lis:
            v_val = v[i]
            if v_val == '0':
                zeros += 1
            elif v_val == '1':
                ones += 1
        if zeros > ones:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    g = int(gamma, 2)
    e = int(epsilon, 2)
    print(g*e)


def main_p2(filename):
    lis = get_input(filename)
    len_bin = len(lis[0])
    results = []
    lists = [(copy.copy(lis), None), (copy.copy(lis), 1)]
    for lis, filt_correction in lists:
        for i in range(len_bin):
            zeros = 0
            ones = 0
            if len(lis) == 1:
                break
            for v in lis:
                v_val = v[i]
                if v_val == '0':
                    zeros += 1
                elif v_val == '1':
                    ones += 1
            filt = 0
            if zeros == ones or zeros <= ones:
                filt = 1
            if filt_correction:
                filt = filt_correction - filt
            lis = filter_lis(lis, filt, i)
        results.append(int(lis[0], 2))

    res = 1
    for v in results:
        res *= v
    print(res)

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
