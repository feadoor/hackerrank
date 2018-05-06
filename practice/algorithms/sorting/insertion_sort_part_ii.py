#!/usr/local/bin/pypy3

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def print_space_separated_integers(values):
    print(' '.join(map(str, values)))

def do_step(values, curr_idx):
    curr = values[curr_idx]
    for idx in range(curr_idx - 1, -1, -1):
        if values[idx] > curr:
            values[idx + 1] = values[idx]
        else:
            values[idx + 1] = curr
            break
    else:
        values[0] = curr

def insertion_sort(values):
    for idx in range(1, len(values)):
        do_step(values, idx)
        print_space_separated_integers(values)

def main():
    _, values = input(), read_space_separated_integers()
    insertion_sort(values)

if __name__ == '__main__':
    main()
