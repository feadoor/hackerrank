#!/usr/local/bin/pypy

from collections import Counter

def size_of_best_pick(arr):
    counts = Counter(arr)
    return max(counts[i] + counts[i + 1] for i in counts.iterkeys())

def main():
    n = input()
    arr = map(int, raw_input().strip().split(' '))
    print size_of_best_pick(arr)

if __name__ == "__main__":
    main()