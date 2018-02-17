from itertools import product

def get_best_spend(keyboards, usbs, max_spend):
    all_spends = map(sum, product(keyboards, usbs))
    allowed_spends = filter(lambda x: x <= max_spend, all_spends)
    return max(allowed_spends) if allowed_spends else -1

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    max_spend, _, _ = read_space_separated_integers()
    keyboards = read_space_separated_integers()
    usbs = read_space_separated_integers()
    print get_best_spend(keyboards, usbs, max_spend)

if __name__ == "__main__":
    main()