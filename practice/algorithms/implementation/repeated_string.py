#!/usr/local/bin/pypy

def appearances_of_a(s, length):
    whole_copies, leftovers = divmod(length, len(s))
    return whole_copies * s.count('a') + s[:leftovers].count('a')

def main():
    s, length = raw_input(), input()
    print appearances_of_a(s, length)

if __name__ == "__main__":
    main()