#!/usr/local/bin/pypy3

from itertools import repeat, chain, combinations

GOOD = 'G'
BAD = 'B'

def cross_edges(i, j, width, height):
    return chain(
        (((i, j),),),
        zip(
            zip(range(i + 1, width), repeat(j)),
            zip(reversed(range(0, i)), repeat(j)),
            zip(repeat(i), range(j + 1, height)),
            zip(repeat(i), reversed(range(0, j)))
        )
    )

def valid_crosses(i, j, grid):
    width, height = len(grid), len(grid[0])
    coords = set()
    for edge in cross_edges(i, j, width, height):
        if all(grid[i][j] for i, j in edge):
            coords.update(edge)
            yield frozenset(coords)
        else:
            return

def all_valid_crosses(grid):
    width, height = len(grid), len(grid[0])
    return chain.from_iterable(
        valid_crosses(i, j, grid)
        for i in range(width) for j in range(height)
    )

def max_cross_product(grid):
    return max(
        len(p1) * len(p2)
        for p1, p2 in combinations(all_valid_crosses(grid), 2)
        if not p1 & p2
    )

def main():
    width, height = [int(x) for x in input().strip().split(' ')]
    grid = [[x == GOOD for x in input().strip()] for _ in range(width)]
    print(max_cross_product(grid))

if __name__ == "__main__":
    main()