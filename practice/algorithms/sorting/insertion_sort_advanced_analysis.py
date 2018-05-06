#!/usr/local/bin/pypy3

class FenwickTree:

    def __init__(self, size):
        self._size = size
        self._arr = [0] * self._size

    def insert(self, ix):
        while (ix < self._size):
            self._arr[ix] += 1
            ix |= (ix + 1)

    def sum(self, ix):
        ans = 0
        while ix > 0:
            ans += self._arr[ix - 1]
            ix &= ix & (ix - 1)
        return ans

def count_inversions(arr):
    total, fenwick = 0, FenwickTree(max(arr) + 1)
    for cnt, entry in enumerate(arr):
        total += cnt - fenwick.sum(entry + 1)
        fenwick.insert(entry)
    return total

def main():
    for _ in range(int(input())):
        _, arr = input(), [int(x) for x in input().strip().split(' ')]
        print(count_inversions(arr))

if __name__ == '__main__':
    main()
