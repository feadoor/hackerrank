#!/usr/local/bin/pypy3

def minimum_loss(arr):
    reverse_lookup = {val: idx for idx, val in enumerate(arr)}
    arr.sort()
    return min(
        arr[idx + 1] - arr[idx]
        for idx in range(len(arr) - 1)
        if reverse_lookup[arr[idx + 1]] < reverse_lookup[arr[idx]]
    )

def main():
    _, arr = input(), [int(x) for x in input().strip().split(' ')]
    print(minimum_loss(arr))

if __name__ == '__main__':
    main()
