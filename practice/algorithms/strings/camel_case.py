#!/usr/local/bin/pypy3

def count_uppers(s):
    return sum(1 if c.isupper() else 0 for c in s)

def main():
    print(count_uppers(input()) + 1)

if __name__ == "__main__":
    main()