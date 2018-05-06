#!/usr/local/bin/pypy3

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def do_step(values, curr_idx):
    curr = values[curr_idx]
    for idx in range(curr_idx - 1, -1, -1):
        if values[idx] > curr:
            values[idx + 1] = values[idx]
        else:
            values[idx + 1] = curr
            return curr_idx - idx - 1
    else:
        values[0] = curr
        return curr_idx

def insertion_sort_shifts(values):
    return sum(do_step(values, idx) for idx in range(1, len(values)))

def main():
    _, values = input(), read_space_separated_integers()
    print(insertion_sort_shifts(values))

if __name__ == '__main__':
    main()
