def forward_diagonal_sum(matrix):
    return sum(matrix[ix][ix] for ix in xrange(len(matrix)))

def backward_diagonal_sum(matrix):
    size = len(matrix)
    return sum(matrix[ix][size - ix - 1] for ix in xrange(size))

def diagonal_difference(matrix):
    return abs(forward_diagonal_sum(matrix) - backward_diagonal_sum(matrix))

def main():
    size = input()
    matrix = [map(int, raw_input().strip().split(' ')) for _ in xrange(size)]
    print diagonal_difference(matrix)

if __name__ == "__main__":
    main()