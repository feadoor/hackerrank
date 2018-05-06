#!/usr/local/bin/pypy3

def get_median(arr):
    return sorted(arr)[len(arr) // 2]

def main():
    _, arr = input(), [int(x) for x in input().strip().split(' ')]
    print(get_median(arr))

if __name__ == '__main__':
    main()
