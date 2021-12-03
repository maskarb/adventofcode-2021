import os
import sys

def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main_p1(filename):
    pass

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
