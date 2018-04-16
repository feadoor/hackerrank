#!/usr/local/bin/pypy3

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def surface_area(toy):
    w, h = len(toy), len(toy[0])

    def ud_area(i, j):
        return 2

    def rl_area(i, j):
        return (
            (toy[i][j] if i == 0 else max(0, toy[i][j] - toy[i - 1][j])) +
            (toy[i][j] if i == w - 1 else max(0, toy[i][j] - toy[i + 1][j]))
        )

    def fb_area(i, j):
        return (
            (toy[i][j] if j == 0 else max(0, toy[i][j] - toy[i][j - 1])) +
            (toy[i][j] if j == h - 1 else max(0, toy[i][j] - toy[i][j + 1]))
        )

    return sum(
        ud_area(i, j) + rl_area(i, j) + fb_area(i, j)
        for i in range(w) for j in range(h)
    )

def main():
    h, w = read_space_separated_integers()
    toy = [read_space_separated_integers() for _ in range(h)]
    print(surface_area(toy))

if __name__ == "__main__":
    main()