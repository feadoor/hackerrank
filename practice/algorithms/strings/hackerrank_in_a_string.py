#!/usr/local/bin/pypy3

def contains(s_to_find, s_to_check):
    it = iter(s_to_check)
    return all(c in it for c in s_to_find)

def main():
    cases = int(input())
    for case in range(cases):
        print('YES' if contains('hackerrank', input()) else 'NO')

if __name__ == "__main__":
    main()