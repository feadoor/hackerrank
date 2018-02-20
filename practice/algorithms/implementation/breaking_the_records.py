#!/usr/local/bin/pypy

def is_high_score(prev, curr):
    return curr > prev

def is_low_score(prev, curr):
    return curr < prev

def broken_record_count(scores, predicate):
    record, broken_count = scores[0], 0

    for score in scores:
        if predicate(record, score):
            record = score
            broken_count += 1

    return broken_count

def broken_high_score_count(scores):
    return broken_record_count(scores, is_high_score)

def broken_low_score_count(scores):
    return broken_record_count(scores, is_low_score)

def main():
    n = input()
    scores = map(int, raw_input().strip().split(' '))
    print broken_high_score_count(scores), broken_low_score_count(scores)

if __name__ == "__main__":
    main()