#!/usr/local/bin/pypy

from collections import defaultdict

def minimum_difference(indices):
    if len(indices) > 1:
        sorted_indices = sorted(indices)
        return min(sorted_indices[i + 1] - sorted_indices[i] for i in xrange(len(indices) - 1))
    else:
        return float("inf")

def minimum_distance(arr):
    index_map = defaultdict(list)
    for i, x in enumerate(arr):
        index_map[x].append(i)
    answer = min(minimum_difference(indices) for indices in index_map.itervalues())
    return answer if answer != float("inf") else -1

def main():
    _, arr = input(), map(int, raw_input().strip().split(' '))
    print minimum_distance(arr)

if __name__ == "__main__":
    main()