from copy import deepcopy

BASE_MAGIC_SQUARE = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

def rotate_90(square):
    return [[square[y][2 - x] for y in xrange(3)] for x in xrange(3)]

def reflect(square):
    return [[square[x][2 - y] for y in xrange(3)] for x in xrange(3)]

def all_magic_squares():
    all_squares = []
    worker = BASE_MAGIC_SQUARE

    for _ in xrange(4):
        for _ in xrange(2):
            all_squares.append(worker)
            worker = reflect(worker)
        worker = rotate_90(worker)

    return all_squares

def get_distance(from_square, to_square):
    return sum(abs(from_square[x][y] - to_square[x][y]) for x in xrange(3) for y in xrange(3))

def get_minimum_distance(square):
    return min(get_distance(square, magic_square) for magic_square in all_magic_squares())

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    square = [read_space_separated_integers() for _ in xrange(3)]
    print get_minimum_distance(square)

if __name__ == "__main__":
    main()