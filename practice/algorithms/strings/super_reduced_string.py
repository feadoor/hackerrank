#!/usr/local/bin/pypy3

from itertools import groupby
from operator import itemgetter

def groups(s):
    return map(''.join, map(itemgetter(1), groupby(s)))

def reduce_once(s):
    return ''.join(group[0] for group in groups(s) if len(group) % 2)

def reduce(s):
    prev_s = None
    while prev_s != s:
        prev_s, s = s, reduce_once(s)
    return s

def main():
    answer = reduce(input())
    print(answer if len(answer) else 'Empty String')

if __name__ == "__main__":
    main()