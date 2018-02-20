#!/usr/local/bin/pypy

def beautiful_triplets(arr, d):
    numbers = set(arr)
    return sum(1 for x in arr if x + d in numbers and x + 2 * d in numbers)

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    _, d = read_space_separated_integers()
    arr = read_space_separated_integers()
    print beautiful_triplets(arr, d)

if __name__ == "__main__":
    main()