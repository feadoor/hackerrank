#!/usr/local/bin/pypy3

from itertools import groupby
from operator import itemgetter

def groups(s):
    return map(''.join, map(itemgetter(1), groupby(s)))

def deletions(s):
    return sum(len(x) - 1 for x in groups(s))

def main():
    for _ in range(int(input())):
        print(deletions(input()))

if __name__ == "__main__":
    main()