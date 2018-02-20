#!/usr/local/bin/pypy

def all_final_stones(stones, a, b):
    a, b = min(a, b), max(a, b)
    if a == b:
        yield (stones - 1) * a
    else:
        value, difference = (stones - 1) * a, b - a
        for _ in xrange(stones):
            yield value
            value += difference

def do_test_case():
    stones, a, b = (input() for _ in xrange(3))
    for stone in all_final_stones(stones, a, b):
        print stone,
    print

def main():
    for _ in xrange(input()):
        do_test_case()

if __name__ == "__main__":
    main()