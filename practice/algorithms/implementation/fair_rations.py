#!/usr/local/bin/pypy

from copy import deepcopy

NONE = "NO"

def minimum_loaves(subjects):
    loaves, modified_subjects = 0, deepcopy(subjects)
    for ix in xrange(len(subjects) - 1):
        if modified_subjects[ix] & 1:
            loaves += 2
            modified_subjects[ix] += 1
            modified_subjects[ix + 1] += 1
    return NONE if modified_subjects[-1] & 1 else loaves

def main():
    _, subjects = input(), map(int, raw_input().strip().split(' '))
    print minimum_loaves(subjects)

if __name__ == "__main__":
    main()