#!/usr/local/bin/pypy3

from collections import Counter

def is_valid(s):
    counts = Counter(s)
    meta_counts = Counter(counts.values())
    return (
        len(meta_counts) == 1 or
        len(meta_counts) == 2 and meta_counts[1] == 1 or
        len(meta_counts) == 2 and meta_counts[min(meta_counts.keys()) + 1] == 1
    )

def main():
    print('YES' if is_valid(input()) else 'NO')

if __name__ == "__main__":
    main()