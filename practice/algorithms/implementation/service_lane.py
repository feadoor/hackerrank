def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def do_test_case(arr):
    lo, hi = read_space_separated_integers()
    print min(arr[lo:hi + 1])

def main():
    _, test_cases = read_space_separated_integers()
    arr = read_space_separated_integers()
    for _ in xrange(test_cases):
        do_test_case(arr)

if __name__ == "__main__":
    main()