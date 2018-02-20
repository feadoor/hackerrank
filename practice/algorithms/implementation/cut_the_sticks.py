#!/usr/local/bin/pypy

def perform_cut(arr):
    cut_length = min(arr)
    return [x - cut_length for x in arr if x > cut_length]

def main():
    _, arr = input(), map(int, raw_input().strip().split(' '))
    while arr:
        print len(arr)
        arr = perform_cut(arr)

if __name__ == "__main__":
    main()