from collections import namedtuple
from itertools import takewhile

Point = namedtuple('Point', ['x', 'y'])
DELTAS = [Point(*x) for x in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]]

def in_bounds(position, board_size):
    return 1 <= position.x <= board_size and 1 <= position.y <= board_size

def add(position, delta):
    return Point(position.x + delta.x, position.y + delta.y)

def get_beam(start, delta, board_size):
    position = add(start, delta)
    while in_bounds(position, board_size):
        yield position
        position = add(position, delta)

def attackable_squares_in_beam(beam, obstacles):
    return sum(1 for _ in takewhile(lambda x: x not in obstacles, beam))

def attackable_squares(position, obstacles, board_size):
    beams = (get_beam(position, delta, board_size) for delta in DELTAS)
    return sum(attackable_squares_in_beam(beam, obstacles) for beam in beams)

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def read_point():
    return Point(*read_space_separated_integers())

def main():
    board_size, n_obstacles = read_space_separated_integers()
    position = read_point()
    obstacles = set(read_point() for _ in xrange(n_obstacles))
    print attackable_squares(position, obstacles, board_size)

if __name__ == "__main__":
    main()