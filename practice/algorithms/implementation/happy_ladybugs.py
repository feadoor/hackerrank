from collections import Counter

YES = "YES"
NO = "NO"

def is_board_happy(board_str):
    length = len(board_str)
    for ix, c in enumerate(board_str):
        if c != '_' and (ix == 0 or board_str[ix - 1] != c) and (ix == length - 1 or board_str[ix + 1] != c):
            return False
    return True

def is_board_solvable(board_str):
    if is_board_happy(board_str):
        return True
    else:
        counts = Counter(board_str)
        return counts['_'] != 0 and all(k == '_' or v > 1 for k, v in counts.iteritems())

def do_test_case():
    _, board_str = input(), raw_input()
    print YES if is_board_solvable(board_str) else NO

def main():
    for _ in xrange(input()):
        do_test_case()

if __name__ == "__main__":
    main()