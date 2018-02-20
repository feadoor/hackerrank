#!/usr/local/bin/pypy

def in_bounds(size, row, col):
    return 0 <= row < size and 0 <= col < size

def neighbours(row, col):
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

def is_cavity(matrix, row, col):
    size = len(matrix)
    for neighbour_row, neighbour_col in neighbours(row, col):
        if not in_bounds(size, neighbour_row, neighbour_col):
            return False
        if matrix[neighbour_row][neighbour_col] >= matrix[row][col]:
            return False
    return True

def print_map(matrix):
    for row in xrange(len(matrix)):
        for col in xrange(len(matrix)):
            if is_cavity(matrix, row, col):
                matrix[row][col] = 'X'

    for line in matrix:
        print ''.join(map(str, line))

def main():
    size = input()
    matrix = [map(int, list(raw_input())) for _ in xrange(size)]
    print_map(matrix)

if __name__ == "__main__":
    main()