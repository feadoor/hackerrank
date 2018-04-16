#!/usr/local/bin/pypy3

from itertools import chain, groupby
from operator import itemgetter

def groups(s):
    return map(''.join, map(itemgetter(1), groupby(s)))

def weights(group):
    score = ord(group[0]) - ord('a') + 1
    return range(score, score * (len(group) + 1), score)

def all_weights(s):
    return set(chain.from_iterable(map(weights, groups(s))))

def main():
    weight_set = all_weights(input())
    for _ in range(int(input())):
        print('Yes' if int(input()) in weight_set else 'No')

if __name__ == "__main__":
    main()