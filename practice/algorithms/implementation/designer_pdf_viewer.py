from string import ascii_lowercase

def get_selected_area(word, letter_heights):
    return len(word) * max(letter_heights[c] for c in word)

def read_letter_heights():
    heights = map(int, raw_input().strip().split(' '))
    return {c: heights[ord(c) - ord('a')] for c in ascii_lowercase}

def main():
    letter_heights = read_letter_heights()
    word = raw_input()
    print get_selected_area(word, letter_heights)

if __name__ == "__main__":
    main()