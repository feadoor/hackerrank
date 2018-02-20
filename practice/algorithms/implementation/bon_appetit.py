#!/usr/local/bin/pypy

def calculate_actual_bill(items, skipped_idx):
    return (sum(items) - items[skipped_idx]) / 2

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    n, skipped_idx = read_space_separated_integers()
    items = read_space_separated_integers()
    charged_bill = input()

    actual_bill = calculate_actual_bill(items, skipped_idx)
    print 'Bon Appetit' if actual_bill == charged_bill else charged_bill - actual_bill

if __name__ == "__main__":
    main()