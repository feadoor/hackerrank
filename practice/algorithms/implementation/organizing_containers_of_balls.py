POSSIBLE = "Possible"
IMPOSSIBLE = "Impossible"

def row_sums(matrix, size):
    return [sum(matrix[x][y] for y in xrange(size)) for x in xrange(size)]

def column_sums(matrix, size):
    return [sum(matrix[x][y] for x in xrange(size)) for y in xrange(size)]

def possible(matrix, size):
    return sorted(row_sums(matrix, size)) == sorted(column_sums(matrix, size))

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def read_matrix(size):
    return [read_space_separated_integers() for _ in xrange(size)]

def do_test_case():
    size = input()
    matrix = read_matrix(size)
    print POSSIBLE if possible(matrix, size) else IMPOSSIBLE

def main():
    test_cases = input()
    for _ in xrange(test_cases):
        do_test_case()

if __name__ == "__main__":
    main()