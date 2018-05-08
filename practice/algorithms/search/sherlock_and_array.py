#!/usr/local/bin/pypy3

def exists_partition_element(arr):
    curr_sum, total = 0, sum(arr)
    for value in arr:
        if 2 * curr_sum == total - value:
            return True
        curr_sum += value
    return False

def do_test_case():
    _, arr = input(), [int(x) for x in input().strip().split(' ')]
    print('YES' if exists_partition_element(arr) else 'NO')

def main():
    for _ in range(int(input())):
        do_test_case()

if __name__ == '__main__':
    main()
