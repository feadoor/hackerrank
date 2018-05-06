#!/usr/local/bin/pypy3

from collections import deque

def get_moves(curr_square, board_size, a, b):
    curr_x, curr_y = curr_square
    return {(x, y) for x, y in ((curr_x + a, curr_y + b), (curr_x + b, curr_y + a),
                                (curr_x + a, curr_y - b), (curr_x - b, curr_y + a),
                                (curr_x - a, curr_y + b), (curr_x + b, curr_y - a),
                                (curr_x - a, curr_y - b), (curr_x - b, curr_y - a))
                   if 0 <= x < board_size and 0 <= y < board_size}

def shortest_path(start_square, end_square, board_size, a, b):
    bfs, seen = deque([(start_square, 0)]), set(start_square)
    while bfs:
        curr_square, distance = bfs.popleft()
        for square in get_moves(curr_square, board_size, a, b):
            if square == end_square:
                return distance + 1
            elif square not in seen:
                seen.add(square)
                bfs.append((square, distance + 1))
    return -1


def main():
    board_size = int(input())
    start, end = (0, 0), (board_size - 1, board_size - 1)
    for a in range(1, board_size):
        print(' '.join(map(str, (shortest_path(start, end, board_size, a, b) for b in range(1, board_size)))))

if __name__ == '__main__':
    main()
