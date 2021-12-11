import os
import sys
from collections import defaultdict

def get_input(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
AUTOCOMPLETE_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

MATCH_PAIR = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
CLOSERS = [")", "]", "}", ">"]
OPENERS = ["(", "[", "{", "<"]
MATCHES = ["()", "[]", "{}", "<>"]

def main_p1(filename):
    lines = get_input(filename)

    def recurse(lis, compare, end):
        if len(lis) <= 2:
            return
        if compare in OPENERS:
            closing = MATCH_PAIR[compare]
        elif compare in CLOSERS:
            if compare == end[0]:
                return recurse(lis[1:], lis[1], end[1:])
            return compare
        if lis[1] == closing:
            return recurse(lis[2:], lis[2], end)
        elif lis[1] in OPENERS:
            return recurse(lis[1:], lis[1], closing + end)

        return lis[1]

    invalids = defaultdict(int)
    for line in lines:
        invalids[recurse(line, line[0], '')] += 1

    result = 0
    for k, v in POINTS.items():
        result += invalids[k] * v
    print(f"results: {invalids}\n{result}")


def main_p2(filename):
    lines = get_input(filename)

    def recurse(lis, compare, end):
        if len(lis) < 2:
            # hideous
            if compare in CLOSERS and compare == end[0]:
                return end[1:]
            if compare in OPENERS:
                closing = MATCH_PAIR[compare]
                return closing + end
            return
        if compare in CLOSERS:
            if compare == end[0]:
                return recurse(lis[1:], lis[1], end[1:])
            return
        else:
            closing = MATCH_PAIR[compare]
            end = closing + end
            return recurse(lis[1:], lis[1], end)

    autocorrected = []
    for line in lines:
        autocorrected.append(recurse(line, line[0], ''))

    results = []
    for chars in autocorrected:
        result = 0
        if not chars:
            continue
        for c in chars:
            result *= 5
            result += AUTOCOMPLETE_POINTS[c]
        results.append(result)
    len_results = len(results)
    ordered = sorted(results)
    for i, v in enumerate(ordered):
        print(i, v)
    final_result = ordered[int(len_results/2)]
    print(f"results: {autocorrected}\n{ordered}\n{final_result}")


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
