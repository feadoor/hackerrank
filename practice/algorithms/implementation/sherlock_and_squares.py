from math import sqrt, floor

def integer_sqrt(n):
    return int(floor(sqrt(n)))

def squares_between(lo, hi):
    hi_sqrt = integer_sqrt(hi)
    lo_sqrt = integer_sqrt(lo)
    lo_is_square = lo_sqrt * lo_sqrt == lo
    return hi_sqrt - lo_sqrt + int(lo_is_square)

def main():
    test_cases = input()
    for _ in xrange(test_cases):
        lo, hi = map(int, raw_input().strip().split(' '))
        print squares_between(lo, hi)

if __name__ == "__main__":
    main()