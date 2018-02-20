#!/usr/local/bin/pypy

START_ENERGY = 100

def final_energy(clouds, jump_size):
    energy, position = START_ENERGY, 0
    while True:
        position = (position + jump_size) % len(clouds)
        energy -= 3 if clouds[position] else 1
        if position == 0:
            break
    return energy

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    _, jump_size = read_space_separated_integers()
    clouds = map(bool, read_space_separated_integers())
    print final_energy(clouds, jump_size)

if __name__ == "__main__":
    main()