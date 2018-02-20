#!/usr/local/bin/pypy

def effective_cost(actual, other, conversion):
    return min(actual, other + conversion)

def cost_of_gifts(black_cost, white_cost, conversion_cost, black_amount, white_amount):
    effective_black_cost = effective_cost(black_cost, white_cost, conversion_cost)
    effective_white_cost = effective_cost(white_cost, black_cost, conversion_cost)
    return black_amount * effective_black_cost + white_amount * effective_white_cost

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def do_test_case():
    black_amount, white_amount = read_space_separated_integers()
    black_cost, white_cost, conversion_cost = read_space_separated_integers()
    print cost_of_gifts(black_cost, white_cost, conversion_cost, black_amount, white_amount)

def main():
    test_cases = input()
    for _ in xrange(test_cases):
        do_test_case()

if __name__ == "__main__":
    main()