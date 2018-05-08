#!/usr/local/bin/pypy3

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def maximum_subarray_sum(arr, mod):
    prefix_sums, best_sum = [0], 0
    for val in arr:
        prefix_sums.append((prefix_sums[-1] + val) % mod)
        best_sum = max(best_sum, prefix_sums[-1])

    leftmost, rightmost = {}, {}
    for idx, val in enumerate(prefix_sums):
        rightmost[val] = idx
    for idx in range(len(prefix_sums) - 1, -1, -1):
        leftmost[prefix_sums[idx]] = idx

    prefix_sums = sorted(set(prefix_sums))
    for idx, p_sum in enumerate(prefix_sums):
        if idx < len(prefix_sums) - 1:
            if leftmost[prefix_sums[idx + 1]] < rightmost[p_sum]:
                best_sum = max(best_sum, (p_sum - prefix_sums[idx + 1]) % mod)

    return best_sum

def do_test_case():
    _, mod = read_space_separated_integers()
    arr = read_space_separated_integers()
    print(maximum_subarray_sum(arr, mod))

def main():
    for _ in range(int(input())):
        do_test_case()

if __name__ == '__main__':
    main()
