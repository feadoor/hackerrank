#!/usr/local/bin/pypy3

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def main():
    _, diff = read_space_separated_integers()
    values = set(read_space_separated_integers())
    print(sum(val + diff in values for val in values))

if __name__ == '__main__':
    main()
