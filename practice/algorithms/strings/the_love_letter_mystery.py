#!/usr/local/bin/pypy3

def distance(s1, s2):
    return sum(abs(ord(x) - ord(y)) for x, y in zip(s1, s2))

def reductions(s):
    return distance(s, s[::-1]) // 2

def main():
    for _ in range(int(input())):
        print(reductions(input()))

if __name__ == "__main__":
    main()