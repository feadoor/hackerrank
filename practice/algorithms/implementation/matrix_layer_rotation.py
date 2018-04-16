#!/usr/local/bin/pypy3

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def read_matrix(rows):
    return [read_space_separated_integers() for _ in range(rows)]

def get_circles(m, n):

    def get_circle(circle_idx):
        circle, i, j = [], circle_idx, circle_idx
        while j < n - circle_idx - 1:
            circle.append((i, j))
            j += 1
        while i < m - circle_idx - 1:
            circle.append((i, j))
            i += 1
        while j > circle_idx:
            circle.append((i, j))
            j -= 1
        while i > circle_idx:
            circle.append((i, j))
            i -= 1
        return circle

    return [get_circle(idx) for idx in range(min(m, n) // 2)]

def spin_matrix(mat, rotations):
    m, n = len(mat), len(mat[0])
    circles = get_circles(m, n)

    result = [[0 for _ in range(n)] for _ in range(m)]
    for circle in circles:
        for idx, (i, j) in enumerate(circle):
            new_i, new_j = circle[(idx + rotations) % len(circle)]
            result[i][j] = mat[new_i][new_j]

    return result

def main():
    m, n, rotations = read_space_separated_integers()
    matrix = read_matrix(m)
    for row in spin_matrix(matrix, rotations):
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()