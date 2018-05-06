#!/usr/local/bin/pypy3

def get_pairs_with_smallest_abs(arr):
    arr.sort()
    best_abs, best_pairs = float('inf'), []
    for ix in range(len(arr) - 1):
        if abs(arr[ix] - arr[ix + 1]) < best_abs:
            best_abs = abs(arr[ix] - arr[ix + 1])
            best_pairs = []
        if abs(arr[ix] - arr[ix + 1]) == best_abs:
            best_pairs.extend([arr[ix], arr[ix + 1]])
    return best_pairs

def main():
    _, arr = input(), [int(x) for x in input().strip().split(' ')]
    print(' '.join(map(str, get_pairs_with_smallest_abs(arr))))

if __name__ == '__main__':
    main()
