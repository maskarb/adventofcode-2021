import os
import sys
from dataclasses import dataclass, field


@dataclass(order=True)
class BingoNumber:
    number: str
    marked: bool = False

@dataclass()
class BingoBoard:
    rows: tuple
    win: bool = False
    rank: int = field(init=False)
    winning_draw: int = 0

    def __eq__(self, other):
        return self.rank == other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __lt__(self, other):
        return self.rank < other.rank


def get_input(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def p1(filename):
    rows = get_input(filename)
    draw_numbers = rows[0].split(',')
    boards_tmp = []
    board_rows = []
    for row in rows[2:]:
        if row == '':
            boards_tmp.append(board_rows)
            board_rows = []
            continue
        board_rows.append(tuple(BingoNumber(v) for v in row.split()))
    boards = []
    for board in boards_tmp:
        board_cols = [
            tuple(BingoNumber(row[i].number) for row in board)
            for i in range(5)
        ]
        boards.append((board, board_cols))

    for draw in draw_numbers:
        for board in boards:
            rows, cols = board
            for row in rows:
                for val in row:
                    if val.number == draw:
                        val.marked = True
        for board in boards:
            rows, cols = board
            for row in rows:
                if all(v.marked for v in row):
                    return board, draw
            for col in cols:
                if all(v.marked for v in col):
                    return board, draw

def p2(filename):
    rows = get_input(filename)
    draw_numbers = rows[0].split(',')
    boards = []
    board_rows = []
    for row in rows[2:]:
        if row == '':
            boards.append(BingoBoard(board_rows))
            board_rows = []
            continue
        board_rows.append(tuple(BingoNumber(v) for v in row.split()))
    boards.append(BingoBoard(board_rows))

    counter = 0
    for draw in draw_numbers:
        for board in boards:
            for row in board.rows:
                for val in row:
                    if val.number == draw and not board.win:
                        val.marked = True
        for board in boards:
            for row in board.rows:
                if all(v.marked for v in row) and not board.win:
                    counter += 1
                    board.win = True
                    board.rank = counter
                    board.winning_draw = draw
            for i in range(5):
                col = [row[i] for row in board.rows]
                if all(v.marked for v in col) and not board.win:
                    counter += 1
                    board.win = True
                    board.rank = counter
                    board.winning_draw = draw
    winners = sorted(boards)
    return winners[-1]

def main_p2(filename):
    b = p2(filename)
    print(b)
    s = sum(sum(int(v.number) for v in row if not v.marked) for row in b.rows)
    print(f"result: {s * int(b.winning_draw)}")

def main_p1(filename):
    b, v = p1(filename)
    print(b)
    rows, _ = b
    s = sum(sum(int(v.number) for v in row if not v.marked) for row in rows)
    print(f"result: {s * int(v)}")

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


(BingoNumber(number='38', marked=False), BingoNumber(number='46', marked=True), BingoNumber(number='18', marked=True), BingoNumber(number='54', marked=True), BingoNumber(number='76', marked=True)),
(BingoNumber(number='25', marked=False), BingoNumber(number='22', marked=False), BingoNumber(number='47', marked=True), BingoNumber(number='10', marked=True), BingoNumber(number='11', marked=True)),
(BingoNumber(number='63', marked=True), BingoNumber(number='29', marked=True), BingoNumber(number='74', marked=True), BingoNumber(number='71', marked=True), BingoNumber(number='92', marked=True)),
(BingoNumber(number='75', marked=False), BingoNumber(number='98', marked=True), BingoNumber(number='0', marked=False), BingoNumber(number='65', marked=False), BingoNumber(number='4', marked=False)),
(BingoNumber(number='87', marked=False), BingoNumber(number='14', marked=True), BingoNumber(number='13', marked=True), BingoNumber(number='64', marked=True), BingoNumber(number='12', marked=False))