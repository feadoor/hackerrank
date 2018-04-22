#!/usr/local/bin/pypy3

from collections import defaultdict

def shortest_substring_to_replace(s):
    target, counts = len(s) // 4, defaultdict(int)
    left, right = -1, len(s)

    while left < len(s) - 1 and counts[s[left + 1]] < target:
        left += 1
        counts[s[left]] += 1

    best_remainder = right - left - 1
    while left >= 0:
        counts[s[left]] -= 1
        left -= 1
        while right > left + 1 and counts[s[right - 1]] < target:
            right -= 1
            counts[s[right]] += 1
        best_remainder = min(best_remainder, right - left - 1)

    return best_remainder

def main():
    _, s = input(), input()
    print(shortest_substring_to_replace(s))

if __name__ == "__main__":
    main()