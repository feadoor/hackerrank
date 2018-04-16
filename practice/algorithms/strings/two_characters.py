#!/usr/local/bin/pypy3

from itertools import combinations, starmap

def alternation_length(s):
    def inner(c1, c2):
        modified_s = ''.join(c for c in s if c == c1 or c == c2)
        valid_alternation = not any(
            modified_s[i] == modified_s[i + 1]
            for i in range(len(modified_s) - 1)
        )
        return len(modified_s) if valid_alternation else 0
    return inner

def longest_alternation(s):
    chars_in_s = set(s)
    alternations = starmap(alternation_length(s), combinations(chars_in_s, 2))
    return max(alternations, default=0)

def main():
    _, letters = input(), input()
    print(longest_alternation(letters))

if __name__ == "__main__":
    main()