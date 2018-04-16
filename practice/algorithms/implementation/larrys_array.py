#!/usr/local/bin/pypy3

YES = 'YES'
NO = 'NO'

def read_integer():
    return int(input())

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def inversions(perm):
    return sum(
        1 if perm[i] > perm[j] else 0
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )

def is_even(perm):
    return inversions(perm) % 2 == 0

def main():
    test_cases = read_integer()
    for _ in range(test_cases):
        _, permutation = read_integer(), read_space_separated_integers()
        print(YES if is_even(permutation) else NO)

if __name__ == "__main__":
    main()