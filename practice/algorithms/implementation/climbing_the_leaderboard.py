#!/usr/local/bin/pypy

def uniq(arr):
    seen, unique = set(), []
    for x in arr:
        if x not in seen:
            unique.append(x)
            seen.add(x)
    return unique

def index(x, scores):
    lo, hi = 0, len(scores)
    while lo != hi:
        mid = (lo + hi) / 2
        if scores[mid] == x:
            return mid
        elif scores[mid] < x:
            hi = mid
        else:
            lo = mid + 1
    return lo

def rank(x, scores):
    return index(x, scores) + 1

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    _, scores = input(), uniq(read_space_separated_integers())
    _, alice_scores = input(), read_space_separated_integers()

    for alice_score in alice_scores:
        print rank(alice_score, scores)

if __name__ == "__main__":
    main()