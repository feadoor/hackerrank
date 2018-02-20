#!/usr/local/bin/pypy

CAT_A = "Cat A"
CAT_B = "Cat B"
MOUSE = "Mouse C"

def get_distance(cat, mouse):
    return abs(cat - mouse)

def get_winner(cat_a, cat_b, mouse):
    a_distance = get_distance(cat_a, mouse)
    b_distance = get_distance(cat_b, mouse)

    if a_distance < b_distance:
        return CAT_A
    elif b_distance < a_distance:
        return CAT_B
    else:
        return MOUSE

def main():
    queries = input()
    for _ in xrange(queries):
        cat_a, cat_b, mouse = map(int, raw_input().strip().split(' '))
        print get_winner(cat_a, cat_b, mouse)

if __name__ == "__main__":
    main()