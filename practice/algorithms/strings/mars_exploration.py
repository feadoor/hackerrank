#!/usr/local/bin/pypy3

from itertools import cycle

def distance(s1, s2):
    return sum(x != y for x, y in zip(s1, s2))

def sos_corruptions(s):
    return distance(s, cycle('SOS'))

def main():
    print(sos_corruptions(input()))

if __name__ == "__main__":
    main()