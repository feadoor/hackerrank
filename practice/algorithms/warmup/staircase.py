#!/usr/local/bin/pypy

def main():
    size = input()
    for steps in xrange(1, size + 1):
        print ' ' * (size - steps) + '#' * steps

if __name__ == "__main__":
    main()