import os
import sys
import time

from functools import cached_property

def get_input(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

class Node:
    def __init__(self, val):
        self.name = val.lower()
        self.val = val
        self.edges = []

    @cached_property
    def big(self):
        return self.val == self.val.upper()

    def __eq__(self, other) -> bool:
        return self.val == other.val

    def __lt__(self, other) -> bool:
        return self.name < other.name

    def __hash__(self) -> int:
        concated_int = ''.join(str(ord(c)) for c in self.val)
        return int(concated_int)

    def __repr__(self):
        return f"Node {self.name}"

class Graph:
    def __init__(self, nodes={}):
        self.nodes = nodes

    def add_node(self, val):
        if self.nodes.get(val):
            return
        new_node = Node(val)
        self.nodes[new_node.val] = new_node

    def add_edge(self, node1, node2):
        node1.edges.append(node2)
        node2.edges.append(node1)

    def __repr__(self):
        return "".join((f"{key}: {value.edges}\n") for key, value in self.nodes.items())

    def any_double_small(self, path):
        return len(path) != len(set(path))

    def all_paths(self, node1, node2, path=[], level=0):
        path = path + [node1]
        if node1 == node2:
            return [path]
        paths = []
        for node in self.nodes[node1.val].edges:
            if node not in path or node.big:
                subpaths = self.all_paths(node, node2, path, level=level+1)
                for subpath in subpaths:
                    paths.append(subpath)
        return paths

    def all_paths_2(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return [path]
        paths = []
        for node in self.nodes[node1.val].edges:
            smalls_in_path = [node for node in path if not node.big]
            if node not in path or node.big or not self.any_double_small(smalls_in_path) and node.name != 'start':
                subpaths = self.all_paths_2(node, node2, path)
                for subpath in subpaths:
                    paths.append(subpath)
        return paths


def main_p1(lines):
    g = Graph()
    for line in lines:
        nodes = line.split('-')
        for n in nodes:
            g.add_node(n)
        g.add_edge(g.nodes[nodes[0]], g.nodes[nodes[1]])
    print(g)
    paths = g.all_paths(g.nodes['start'], g.nodes['end'])
    print(f'result p1: {len(paths)}')

    paths = g.all_paths_2(g.nodes['start'], g.nodes['end'])
    print(f'result p2: {len(paths)}')


def main_p2(lines):
    g = Graph()
    for line in lines:
        nodes = line.split('-')
        for n in nodes:
            g.add_node(n)
        g.add_edge(g.nodes[nodes[0]], g.nodes[nodes[1]])
    print(g)
    paths = g.all_paths_2(g.nodes['start'], g.nodes['end'])
    print(f'result: {len(paths)}')

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ('p1', 'p2'):
        print('you done did it wrong')
        exit()
    filename = os.path.join(sys.argv[0].split('/', 1)[0], 'input.txt')
    lines = get_input(filename)
    part = sys.argv[1:]
    if 'p1' in part or 'p2' in part:
        start = time.perf_counter()
        main_p1(lines)
        end = time.perf_counter()
        print(end - start)
