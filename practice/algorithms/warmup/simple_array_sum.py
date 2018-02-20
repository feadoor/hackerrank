#!/usr/local/bin/pypy

def main():
    size = input()
    array = map(int, raw_input().strip().split(' '))
    print sum(array)

if __name__ == "__main__":
    main()