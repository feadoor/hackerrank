#!/usr/local/bin/pypy

from itertools import permutations

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
CLEAN = 'CLEAN'

DIRTY = 'd'

def find_dirty_squares(grid):
    dirty_squares = []

    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == DIRTY:
                dirty_squares.append((x, y))

    return dirty_squares

def manhattan_distance(from_square, to_square):
    from_x, from_y = from_square
    to_x, to_y = to_square
    return abs(to_x - from_x) + abs(to_y - from_y)

def total_distance(squares):
    return sum(manhattan_distance(squares[ix], squares[ix + 1]) for ix in range(len(squares) - 1))

def first_step(from_square, to_square):
    from_x, from_y = from_square
    to_x, to_y = to_square

    if from_x < to_x:
        return RIGHT
    elif from_x > to_x:
        return LEFT
    elif from_y < to_y:
        return DOWN
    elif from_y > to_y:
        return UP


def next_move(robot_square, grid):
    robot_x, robot_y = robot_square
    if grid[robot_y][robot_x] == DIRTY:
        return CLEAN

    best_distance = float("inf")
    best_ordering = ()
    for ordering in permutations(find_dirty_squares(grid)):
        distance = total_distance((robot_square,) + ordering)
        if distance < best_distance:
            best_distance = distance
            best_ordering = ordering

    return first_step(robot_square, best_ordering[0])

def main():
    robot_y, robot_x = [int(i) for i in raw_input().strip().split()]
    grid = [[j for j in raw_input().strip()] for i in xrange(5)]
    print next_move((robot_x, robot_y), grid)

if __name__ == "__main__":
    main()