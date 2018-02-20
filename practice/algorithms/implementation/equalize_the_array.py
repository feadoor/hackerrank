#!/usr/local/bin/pypy

from collections import Counter

def required_deletions(arr):
    counts = Counter(arr)
    return len(arr) - counts.most_common(1)[0][1]

def main():
    _, arr = input(), map(int, raw_input().strip().split(' '))
    print required_deletions(arr)

if __name__ == "__main__":
    main()