#!/usr/local/bin/pypy3

from collections import Counter
from itertools import chain

def intersection_count(counter1, counter2):
    keys = set(chain(counter1.keys(), counter2.keys()))
    return sum(min(counter1[k], counter2[k]) for k in keys)

def anagram_deletions(s1, s2):
    common_letters = intersection_count(Counter(s1), Counter(s2))
    return len(s1) + len(s2) - 2 * common_letters

def main():
    print(anagram_deletions(input(), input()))

if __name__ == "__main__":
    main()