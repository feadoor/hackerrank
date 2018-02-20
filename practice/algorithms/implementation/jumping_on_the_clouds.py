#!/usr/local/bin/pypy

def is_safe(position, clouds):
    return position < len(clouds) and not clouds[position]

def jumps_required(clouds):
    position, jumps = 0, 0
    while position != len(clouds) - 1:
        position = position + 2 if is_safe(position + 2, clouds) else position + 1
        jumps += 1
    return jumps

def main():
    _, clouds = input(), map(int, raw_input().strip().split(' '))
    print jumps_required(clouds)

if __name__ == "__main__":
    main()