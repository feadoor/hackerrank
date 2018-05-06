#!/usr/local/bin/pypy3

from copy import copy

def swaps_required(arr, target):

    worker, lookup = [], {}
    for idx, val in enumerate(arr):
        worker.append(val)
        lookup[val] = idx

    swap_count = 0
    for idx in range(len(worker)):
        if worker[idx] != target[idx]:
            swap = lookup[target[idx]]
            worker[idx], worker[swap] = worker[swap], worker[idx]
            lookup[worker[swap]] = swap
            swap_count += 1

    return swap_count

def main():
    _, arr = input(), [int(x) for x in input().strip().split(' ')]
    print(min(
        swaps_required(arr, sorted(arr)),
        swaps_required(arr, sorted(arr, reverse=True))
    ))

if __name__ == '__main__':
    main()
