def count_subsequences_of_length_summing_to(arr, length, target):
    def sum_of_subsequence_at(ix):
        return sum(arr[ix:ix + length])
    return sum(sum_of_subsequence_at(ix) == target for ix in xrange(len(arr) - length + 1))

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    chocolate_size = input()
    chocolate = read_space_separated_integers()
    target, length = read_space_separated_integers()
    print count_subsequences_of_length_summing_to(chocolate, length, target)

if __name__ == "__main__":
    main()