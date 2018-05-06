#!/usr/local/bin/pypy3

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def print_space_separated_integers(values):
    print(' '.join(map(str, values)))

def main():
    length, values = int(input()), read_space_separated_integers()
    curr = values[length - 1]
    for idx in range(length - 2, -1, -1):
        if values[idx] > curr:
            values[idx + 1] = values[idx]
            print_space_separated_integers(values)
        else:
            values[idx + 1] = curr
            break
    else:
        values[0] = curr
    print_space_separated_integers(values)

if __name__ == '__main__':
    main()
