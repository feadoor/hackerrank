def is_within_house(house, tree_position, fruit_delta):
    return house[0] <= tree_position + fruit_delta <= house[1]

def count_within_house(house, tree_position, fruit_deltas):
    return sum(is_within_house(house, tree_position, fruit_delta) for fruit_delta in fruit_deltas)

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    house = read_space_separated_integers()
    apple_tree_pos, orange_tree_pos = read_space_separated_integers()
    num_apples, num_oranges = read_space_separated_integers()

    apple_deltas = read_space_separated_integers()
    orange_deltas = read_space_separated_integers()

    print count_within_house(house, apple_tree_pos, apple_deltas)
    print count_within_house(house, orange_tree_pos, orange_deltas)

if __name__ == "__main__":
    main()