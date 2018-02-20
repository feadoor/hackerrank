#!/usr/local/bin/pypy

NONE = "no answer"

def next_permutation(string):
    i = len(string) - 2
    while i >= 0 and string[i] >= string[i + 1]:
        i -= 1
    if i < 0: return None

    j = len(string) - 1
    while string[j] <= string[i]:
        j -= 1

    swapped = string[:i] + string[j] + string[i + 1:j] + string[i] + string[j + 1:]
    return swapped[:i + 1] + swapped[i + 1:][::-1]

def main():
    for _ in xrange(input()):
        next_perm = next_permutation(raw_input())
        print next_perm if next_perm else NONE

if __name__ == "__main__":
    main()