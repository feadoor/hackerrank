def digits(n):
    return map(int, str(n))

def divisible_digits(n):
    return sum(1 for d in digits(n) if d != 0 and n % d == 0)

def main():
    test_cases = input()
    for _ in xrange(test_cases):
        print divisible_digits(input())

if __name__ == "__main__":
    main()