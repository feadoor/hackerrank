def get_absolute_permutation(length, difference):
    if difference == 0:
        for x in xrange(1, length + 1):
            yield x
    elif length % (2 * difference) == 0:
        block_size, start, mid = 2 * difference, difference, 0
        for block in xrange(length / (2 * difference)):
            for ix in xrange(1, difference + 1):
                yield start + ix
            for ix in xrange(1, difference + 1):
                yield mid + ix
            start, mid = start + block_size, mid + block_size
    else:
        yield -1

def do_test_case():
    length, difference = map(int, raw_input().strip().split(' '))
    absolute_permutation = get_absolute_permutation(length, difference)
    print ' '.join(map(str, absolute_permutation)) if absolute_permutation else NONE

def main():
    for _ in xrange(input()):
        do_test_case()

if __name__ == "__main__":
    main()