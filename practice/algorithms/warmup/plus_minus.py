#!/usr/local/bin/pypy

from __future__ import division

def array_statistics(arr):
    positive_count, negative_count, zero_count = 0, 0, 0
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    return positive_count, negative_count, zero_count

def main():
    size = input()
    array = map(int, raw_input().strip().split(' '))

    positive, negative, zero = array_statistics(array)
    print positive / size
    print negative / size
    print zero / size

if __name__ == "__main__":
    main()