def adjusted_value(arr, rotations, query_index):
    adjusted_index = (query_index - rotations) % len(arr)
    return arr[adjusted_index]

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    _, rotations, test_cases = read_space_separated_integers()
    arr = read_space_separated_integers()
    for _ in xrange(test_cases):
        query_index = input()
        print adjusted_value(arr, rotations, query_index)

if __name__ == "__main__":
    main()