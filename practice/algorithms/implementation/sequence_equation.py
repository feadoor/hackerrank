def read_reverse_permutation(size):
    reverse_perm = {n : 0 for n in xrange(1, size + 1)}
    for ix, val in enumerate(map(int, raw_input().strip().split(' '))):
        reverse_perm[val] = ix + 1
    return reverse_perm

def main():
    size = input()
    reverse_perm = read_reverse_permutation(size)
    for n in xrange(1, size + 1):
        print reverse_perm[reverse_perm[n]]

if __name__ == "__main__":
    main()