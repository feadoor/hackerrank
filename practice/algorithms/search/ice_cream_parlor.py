#!/usr/local/bin/pypy3

from collections import defaultdict

def read_integer():
    return int(input())

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def do_test_case():
    money, _ = read_integer(), read_integer()
    ice_creams = read_space_separated_integers()
    reverse_lookup = defaultdict(set)
    for idx, val in enumerate(ice_creams):
        reverse_lookup[val].add(idx + 1)

    for val in reverse_lookup.keys():
        if money - val in reverse_lookup:
            amts = reverse_lookup[val] | reverse_lookup[money - val]
            if len(amts) == 2:
                print(' '.join(map(str, sorted(amts))))
                return

def main():
    for _ in range(read_integer()):
        do_test_case()

if __name__ == '__main__':
    main()
