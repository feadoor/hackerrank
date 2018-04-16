#!/usr/local/bin/pypy3

def characters_in_all_of(strings):
    return set.intersection(*map(set, strings))

def number_of_gemstones(strings):
    return len(characters_in_all_of(strings))

def main():
    n_strings = int(input())
    strings = [input() for _ in range(n_strings)]
    print(number_of_gemstones(strings))

if __name__ == "__main__":
    main()