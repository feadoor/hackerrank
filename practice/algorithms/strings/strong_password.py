#!/usr/local/bin/pypy3

import string

UPPERS = string.ascii_uppercase
LOWERS = string.ascii_lowercase
NUMBERS = string.digits
SPECIALS = '!@#$%^&*()-+'

def contains(charset):
    return lambda s: any(c in charset for c in s)

def characters_to_add(password):
    missing_length = 6 - len(password)
    missing_chars = sum(
        0 if match(password) else 1
        for match in map(contains, [UPPERS, LOWERS, NUMBERS, SPECIALS])
    )
    return max(missing_length, missing_chars)

def main():
    _, password = input(), input()
    print(characters_to_add(password))

if __name__ == "__main__":
    main()