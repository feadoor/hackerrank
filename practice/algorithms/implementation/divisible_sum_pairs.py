from collections import defaultdict

def divisible_sum_pairs(arr, divisor):
    remainder_counts = defaultdict(int)
    for num in arr:
        remainder_counts[num % divisor] += 1

    def complementary_remainder(r):
        return divisor - r if r > 0 else 0

    def pairs_with_remainders(r1, r2):
        if r1 == r2:
            return remainder_counts[r1] * (remainder_counts[r2] - 1) / 2
        else:
            return remainder_counts[r1] * remainder_counts[r2]

    return sum(pairs_with_remainders(r, complementary_remainder(r)) for r in xrange(divisor / 2 + 1))

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    n, k = read_space_separated_integers()
    arr = read_space_separated_integers()
    print divisible_sum_pairs(arr, k)

if __name__ == "__main__":
    main()