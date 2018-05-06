#!/usr/local/bin/pypy3

def get_counts(values, n_poss=100):
    counts = [0] * n_poss
    for value in values:
        counts[value] += 1
    return counts

def main():
    _, values = input(), [int(x) for x in input().strip().split(' ')]
    print(' '.join(map(str, get_counts(values))))

if __name__ == '__main__':
    main()
