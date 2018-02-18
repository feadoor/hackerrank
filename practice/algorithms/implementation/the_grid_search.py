YES = "YES"
NO = "NO"

def get_dimensions(grid):
    return len(grid[0]), len(grid)

def is_subgrid(grid, pattern):
    grid_width, grid_height = get_dimensions(grid)
    pattern_width, pattern_height = get_dimensions(pattern)

    def subgrid_matches(row, col):
        return all(
            grid[row + r][col + c] == pattern[r][c]
            for r in xrange(pattern_height)
            for c in xrange(pattern_width)
        )

    for row in xrange(grid_height - pattern_height + 1):
        for col in xrange(grid_width - pattern_width + 1):
            if subgrid_matches(row, col):
                return True

    return False

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def read_row():
    return map(int, raw_input())

def read_grid():
    rows, _ = read_space_separated_integers()
    return [read_row() for _ in xrange(rows)]

def do_test_case():
    grid, pattern = read_grid(), read_grid()
    print YES if is_subgrid(grid, pattern) else NO

def main():
    for _ in xrange(input()):
        do_test_case()

if __name__ == "__main__":
    main()