#!/usr/local/bin/pypy

def number_of_beverages_needed(max_height, hurdles):
    highest_hurdle = max(hurdles)
    return highest_hurdle - max_height if highest_hurdle > max_height else 0

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    n, max_height = read_space_separated_integers()
    hurdles = read_space_separated_integers()
    print number_of_beverages_needed(max_height, hurdles)

if __name__ == "__main__":
    main()