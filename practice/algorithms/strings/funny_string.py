#!/usr/local/bin/pypy3

def steps(s):
    return [abs(ord(s[i + 1]) - ord(s[i])) for i in range(len(s) - 1)]

def is_reversible(arr):
    return arr == arr[::-1]

def is_funny(s):
    return is_reversible(steps(s))

def main():
    for _ in range(int(input())):
        print('Funny' if is_funny(input()) else 'Not Funny')

if __name__ == "__main__":
    main()