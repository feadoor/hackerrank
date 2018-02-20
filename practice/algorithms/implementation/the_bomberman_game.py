#!/usr/local/bin/pypy

BOMB = 'O'
EMPTY = '.'

def neighbours(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def next_value(board, x, y):
    if board[x][y] == 0:
        return 0
    elif any(board[n_x][n_y] == 1 for n_x, n_y in neighbours(x, y) if 0 <= n_x < len(board) and 0 <= n_y < len(board[n_x])):
        return 0
    else:
        return board[x][y] - 1

def add_bombs(board):
    return [[3 if board[x][y] == 0 else board[x][y] for y in xrange(len(board[x]))] for x in xrange(len(board))]

def do_tick(board):
    return [[next_value(board, x, y) for y in xrange(len(board[x]))] for x in xrange(len(board))]

def run(board, ticks):
    for tick in xrange(ticks):
        board = do_tick(board)
        if tick % 2 == 1:
            board = add_bombs(board)
    return board

def get_state(board, ticks):
    if ticks <= 5:
        return run(board, ticks)
    else:
        return run(board, 4 + ticks % 4)

def read_board(rows):
    return [[3 if c == BOMB else 0 for c in raw_input()] for _ in xrange(rows)]

def write_board(board):
    for row in board:
        print ''.join(BOMB if x > 0 else EMPTY for x in row)

def main():
    rows, _, ticks = map(int, raw_input().strip().split(' '))
    write_board(get_state(read_board(rows), ticks))

if __name__ == "__main__":
    main()