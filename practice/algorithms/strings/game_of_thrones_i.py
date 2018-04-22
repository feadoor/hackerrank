#!/usr/local/bin/pypy3

from collections import Counter

def is_palindrome_anagram(s):
    counts = Counter(s)
    return sum(v % 2 for v in counts.values()) == len(s) % 2

def main():
    print('YES' if is_palindrome_anagram(input()) else 'NO')

if __name__ == "__main__":
    main()