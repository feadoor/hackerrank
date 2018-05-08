#!/usr/local/bin/pypy3

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def get_neighbours(square, n, m):
    curr_x, curr_y = square
    return [(x, y) for x, y in ((curr_x + 1, curr_y + 0), (curr_x + 1, curr_y + 1),
                                (curr_x + 0, curr_y + 1), (curr_x - 1, curr_y + 1),
                                (curr_x - 1, curr_y + 0), (curr_x - 1, curr_y - 1),
                                (curr_x + 0, curr_y - 1), (curr_x + 1, curr_y - 1))
                   if 0 <= x < n and 0 <= y < m]

def find_region_size(grid, start):
    n, m = len(grid), len(grid[0])
    squares_to_visit, seen_squares = [start], set([start])
    while squares_to_visit:
        curr_square = squares_to_visit.pop()
        for square in get_neighbours(curr_square, n, m):
            if grid[square[0]][square[1]] == 1 and square not in seen_squares:
                squares_to_visit.append(square)
                seen_squares.add(square)
    return len(seen_squares)

def main():
    n, m = int(input()), int(input())
    grid = [read_space_separated_integers() for _ in range(n)]
    print(max(find_region_size(grid, (x, y)) for x in range(n) for y in range(m) if grid[x][y] == 1))

if __name__ == '__main__':
    main()
