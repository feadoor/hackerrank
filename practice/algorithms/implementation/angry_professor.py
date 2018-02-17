CANCELLED = "YES"
NOT_CANCELLED = "NO"

def meets_threshold(threshold, arrival_times):
    return sum(1 for x in arrival_times if x <= 0) >= threshold

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def do_test_case():
    _, threshold = read_space_separated_integers()
    arrival_times = read_space_separated_integers()
    print NOT_CANCELLED if meets_threshold(threshold, arrival_times) else CANCELLED

def main():
    tests = input()
    for _ in xrange(tests):
        do_test_case()

if __name__ == "__main__":
    main()