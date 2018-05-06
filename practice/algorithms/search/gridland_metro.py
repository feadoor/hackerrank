#!/usr/local/bin/pypy3

from collections import defaultdict

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def merge_intervals(intervals, new_interval):

    for insertion_point, endpoints in enumerate(intervals):
        if endpoints[0] > new_interval[0]:
            intervals.insert(insertion_point, new_interval)
            break
    else:
        intervals.append(new_interval)

    merged, prev_interval = [], intervals[0]
    for interval in intervals:
        if interval[0] <= prev_interval[1] + 1:
            if interval[1] > prev_interval[1]:
                prev_interval[1] = interval[1]
        else:
            merged.append(prev_interval)
            prev_interval = interval
    merged.append(prev_interval)

    return merged

def get_uncovered_squares(n, m, k):
    covered = defaultdict(list)
    for _ in range(k):
        row, lo, hi = read_space_separated_integers()
        covered[row] = merge_intervals(covered[row], [lo, hi])
    return n * m - sum(sum(hi - lo + 1 for lo, hi in intervals) for intervals in covered.values())

def main():
    n, m, k = read_space_separated_integers()
    print(get_uncovered_squares(n, m, k))

if __name__ == '__main__':
    main()
