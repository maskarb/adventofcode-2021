import os
import sys

import numpy as np

def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main_p1(lines):
    m = np.array([[int(v) for v in line.strip()] for line in lines]).transpose()
    x_max, y_max = m.shape

    def increment_value(x, y):
        if x >= 0 and y >= 0 and x <= x_max - 1 and y <= y_max - 1:
            m[x, y] += 1


    def increment_array(old_tmp):
        tmp = np.transpose(np.where(m > 9))
        if tmp.size == 0 and old_tmp.size == 0 or np.array_equal(tmp, old_tmp):
            return
        for i in tmp:
            if i.tolist() in old_tmp.tolist():
                continue
            x , y = i
            p = m[x, y]
            if p > 9:
                neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
                m[x, y] += 1
                for neighbor in neighbors:
                    increment_value(*neighbor)
        increment_array(tmp)

    count = 0
    for i in range(100):
        m += 1
        tmp = np.array([-1, -1])
        increment_array(tmp)

        for x in range(x_max):
            for y in range(y_max):
                p = m[x, y]
                if p > 9:
                    count += 1
                    m[x, y] = 0

    print(f"p1 result: {count}")

def main_p2(lines):
    m = np.array([[int(v) for v in line.strip()] for line in lines]).transpose()
    x_max, y_max = m.shape

    def increment_value(x, y):
        if x >= 0 and y >= 0 and x <= x_max - 1 and y <= y_max - 1:
            m[x, y] += 1


    def increment_array(old_tmp):
        tmp = np.transpose(np.where(m > 9))
        if tmp.size == 0 and old_tmp.size == 0 or np.array_equal(tmp, old_tmp):
            return
        for i in tmp:
            if i.tolist() in old_tmp.tolist():
                continue
            x , y = i
            p = m[x, y]
            if p > 9:
                neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
                m[x, y] += 1
                for neighbor in neighbors:
                    increment_value(*neighbor)
        increment_array(tmp)

    count = 0
    for i in range(1000):
        m += 1
        tmp = np.array([-1, -1])
        increment_array(tmp)

        for x in range(x_max):
            for y in range(y_max):
                p = m[x, y]
                if p > 9:
                    count += 1
                    m[x, y] = 0

        if np.all((m == 0)):
            break

    print(f"p2 result: {i+1}")

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ('p1', 'p2'):
        print('you done did it wrong')
        exit()
    filename = os.path.join(sys.argv[0].split('/', 1)[0], 'input.txt')
    lines = get_input(filename)
    part = sys.argv[1:]
    if 'p1' in part:
        main_p1(lines)
    if 'p2' in part:
        main_p2(lines)
