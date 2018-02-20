#!/usr/local/bin/pypy

INVALID = "INVALID RANGE"

def split(n):
    string = str(n)
    split_point = len(string) / 2
    return int(string[:split_point] or '0'), int(string[split_point:] or '0')

def is_kaprekar(n):
    return sum(split(n * n)) == n

def kaprekars_in_range(lo, hi):
    return [n for n in xrange(lo, hi + 1) if is_kaprekar(n)]

def main():
    lo, hi = input(), input()
    kaprekars = kaprekars_in_range(lo, hi)
    for n in kaprekars: print n,
    if not kaprekars: print INVALID

if __name__ == "__main__":
    main()