#!/usr/local/bin/pypy3

def is_palindrome(s):
    return all(x == y for x, y in zip(s, reversed(s)))

def possible_indices_to_remove(s):
    for idx, (x, y) in enumerate(zip(s, reversed(s))):
        if x != y:
            return idx, len(s) - idx - 1
    return ()

def index_to_remove(s):
    for idx in possible_indices_to_remove(s):
        if is_palindrome(s[:idx] + s[idx + 1:]):
            return idx
    return -1

def main():
    for _ in range(int(input())):
        print(index_to_remove(input()))

if __name__ == "__main__":
    main()