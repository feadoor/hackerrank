def dead_prisoner(prisoners, sweets, starting_idx):
    prisoner_idx = (starting_idx + sweets - 1) % prisoners
    return prisoner_idx if prisoner_idx > 0 else prisoners

def do_test_case():
    prisoners, sweets, starting_idx = map(int, raw_input().strip().split(' '))
    print dead_prisoner(prisoners, sweets, starting_idx)

def main():
    test_cases = input()
    for _ in xrange(test_cases):
        do_test_case()

if __name__ == "__main__":
    main()