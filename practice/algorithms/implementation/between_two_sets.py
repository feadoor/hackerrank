def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

def lcm(x, y):
    return (x * y) / gcd(x, y)

def count_divisors(n):
    return sum(n % k == 0 for k in xrange(1, n + 1))

def count_of_numbers_between(a_set, b_set):
    a_lcm = reduce(lcm, a_set)
    b_gcd = reduce(gcd, b_set)

    return count_divisors(b_gcd / a_lcm) if b_gcd % a_lcm == 0 else 0

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    a_size, b_size = read_space_separated_integers()
    a_set = read_space_separated_integers()
    b_set = read_space_separated_integers()
    print count_of_numbers_between(a_set, b_set)

if __name__ == "__main__":
    main()