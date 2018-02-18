from math import floor, sqrt

def integer_sqrt(n):
    return int(floor(sqrt(n)))

def get_grid_size(length):
    rows = integer_sqrt(length)
    if rows * rows >= length:
        return (rows, rows)
    elif rows * (rows + 1) >= length:
        return (rows, rows + 1)
    else:
        return (rows + 1, rows + 1)

def write_in_grid(s, rows, columns):
    get_char = lambda ix: s[ix] if ix < len(s) else ''
    return [[get_char(r * columns + c) for c in xrange(columns)] for r in xrange(rows)]

def read_from_grid(grid, rows, columns):
    return ' '.join(''.join(grid[r][c] for r in xrange(rows)) for c in xrange(columns))

def encrypt(s):
    no_spaces = s.replace(' ', '')
    rows, columns = get_grid_size(len(no_spaces))
    grid = write_in_grid(no_spaces, rows, columns)
    return read_from_grid(grid, rows, columns)

def main():
    print encrypt(raw_input())

if __name__ == "__main__":
    main()