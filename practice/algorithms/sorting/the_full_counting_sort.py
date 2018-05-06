#!/usr/local/bin/python3

from operator import itemgetter

def read_items(n_items):
    items = []
    for _ in range(n_items // 2):
        x, _ = input().strip().split(' ')
        items.append((int(x), '-'))
    for _ in range(n_items // 2):
        x, s = input().strip().split(' ')
        items.append((int(x), s))
    return items

def main():
    n_items = int(input())
    items = read_items(n_items)
    items.sort(key=itemgetter(0))
    print(' '.join(map(itemgetter(1), items)))

if __name__ == '__main__':
    main()
