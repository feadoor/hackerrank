#!/usr/local/bin/pypy3

def main():
    val, _ = int(input()), input()
    items = [int(x) for x in input().strip().split(' ')]
    print(items.index(val))

if __name__ == '__main__':
    main()
