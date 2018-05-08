#!/usr/local/bin/pypy3

from collections import Counter

def read_arr():
    input()
    return [int(x) for x in input().strip().split(' ')]

def main():
    small, large = read_arr(), read_arr()
    missing_counts = Counter(large) - Counter(small)
    print(' '.join(map(str, sorted(missing_counts.keys()))))

if __name__ == '__main__':
    main()
