#!/usr/local/bin/pypy

from collections import Counter

def most_common(arr):
    counter = Counter(arr)
    return max(arr, key=lambda x: (counter[x], -x))

def main():
    n = input()
    arr = map(int, raw_input().strip().split(' '))
    print most_common(arr)

if __name__ == "__main__":
    main()