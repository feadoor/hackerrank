#!/usr/local/bin/pypy3

from collections import Counter
from itertools import chain

def anagram_distance(s1, s2):
    counter1, counter2 = Counter(s1), Counter(s2)
    keys = set(chain(counter1.keys(), counter2.keys()))
    return sum(abs(counter1[k] - counter2[k]) for k in keys) // 2

def split(s):
    return s[:len(s) // 2], s[len(s) // 2:]

def main():
    for _ in range(int(input())):
        s = input()
        print(-1 if len(s) % 2 != 0 else anagram_distance(*split(s)))

if __name__ == "__main__":
    main()