#!/usr/local/bin/pypy3

from collections import deque

class CountsWithMedian:

    def __init__(self, max_value, queue_length):
        self.counts = [0] * (max_value + 1)
        self.queue = deque()
        self.queue_length = queue_length

    def add_next(self, value):
        if len(self.queue) == self.queue_length:
            self.counts[self.queue.popleft()] -= 1
        self.queue.append(value)
        self.counts[value] += 1

    def get_median(self):
        curr, lo, hi = -1, -1, -1
        target1, target2 = (len(self.queue) - 1) // 2, len(self.queue) // 2
        while curr < target1:
            lo, hi = lo + 1, hi + 1
            curr += self.counts[lo]
        while curr < target2:
            hi += 1
            curr += self.counts[hi]
        return (lo + hi) / 2


def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def main():
    n_days, queue_length = read_space_separated_integers()
    counter, hits = CountsWithMedian(200, queue_length), 0
    for amt in read_space_separated_integers():
        if len(counter.queue) >= queue_length and 2 * counter.get_median() <= amt:
            hits += 1
        counter.add_next(amt)
    print(hits)

if __name__ == '__main__':
    main()
