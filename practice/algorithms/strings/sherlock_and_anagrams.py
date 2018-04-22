#!/usr/local/bin/pypy3

from collections import defaultdict

def substring_frequencies(s):
    frequencies = defaultdict(int)
    for start in range(len(s)):
        for end in range(start, len(s)):
            frequencies[''.join(sorted(s[start : end + 1]))] += 1
    return frequencies

def anagram_substring_pairs(s):
    return sum(x * (x - 1) // 2 for x in substring_frequencies(s).values())

def main():
    for _ in range(int(input())):
        print(anagram_substring_pairs(input()))

if __name__ == "__main__":
    main()