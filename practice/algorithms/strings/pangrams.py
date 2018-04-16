#!/usr/local/bin/pypy3

from string import ascii_lowercase

def is_pangram(s):
    return all(x in set(s.lower()) for x in ascii_lowercase)

def main():
    print('pangram' if is_pangram(input()) else 'not pangram')

if __name__ == "__main__":
    main()