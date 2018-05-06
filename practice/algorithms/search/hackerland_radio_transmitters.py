#!/usr/local/bin/pypy3

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def count_transmitters(sorted_houses, transmitter_distance):
    transmitters, idx = 0, 0
    while idx < len(sorted_houses):
        threshold = sorted_houses[idx] + transmitter_distance
        while idx < len(sorted_houses) and sorted_houses[idx] <= threshold:
            idx += 1
        reach = sorted_houses[idx - 1] + transmitter_distance
        while idx < len(sorted_houses) and sorted_houses[idx] <= reach:
            idx += 1
        transmitters += 1
    return transmitters

def main():
    _, k = read_space_separated_integers()
    houses = sorted(read_space_separated_integers())
    print(count_transmitters(houses, k))

if __name__ == '__main__':
    main()
