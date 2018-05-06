#!/usr/local/bin/pypy3

def partition(values):
    pivot = values[0]
    left, equal, right = [], [], []
    for value in values:
        if value < pivot: left.append(value)
        elif value > pivot: right.append(value)
        else: equal.append(pivot)
    return left + equal + right

def main():
    n, values = int(input()), [int(x) for x in input().strip().split(' ')]
    print(' '.join(map(str, partition(values))))

if __name__ == '__main__':
    main()
