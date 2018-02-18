def complementary_pairs(modulus):
    return [(0, 0)] + [(x, modulus - x) for x in xrange(1, modulus / 2 + 1)]

def elements_congruent_to(arr, residue, modulus):
    return sum(1 for x in arr if x % modulus == residue)

def maximal_elements_from_pair(arr, pair, modulus):
    if pair[0] == pair[1]:
        return min(1, elements_congruent_to(arr, pair[0], modulus))
    else:
        return max(elements_congruent_to(arr, pair[0], modulus),
                   elements_congruent_to(arr, pair[1], modulus))

def maximal_non_divisible_subset_size(arr, modulus):
    return sum(maximal_elements_from_pair(arr, pair, modulus) for pair in complementary_pairs(modulus))

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    _, modulus = read_space_separated_integers()
    arr = read_space_separated_integers()
    print maximal_non_divisible_subset_size(arr, modulus)

if __name__ == "__main__":
    main()