#!/usr/local/bin/pypy

def get_counter(t):
    block = 3
    while block < t:
        block = 2 * block + 3
    return block - t + 1

def main():
    print get_counter(input())

if __name__ == "__main__":
    main()