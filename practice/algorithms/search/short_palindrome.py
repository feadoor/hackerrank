#!/usr/local/bin/pypy3

MODULUS = 1000000007

def count_short_palindromes(s):
    ans, counts = 0, [[0] * 26] + [[[0] * 26 for _ in range(26)]] + [[[0] * 26 for _ in range(26)]]
    for char in s:
        char_v = ord(char) - ord('a')
        for other_v in range(26):
            ans += counts[2][char_v][other_v]
            counts[2][other_v][char_v] += counts[1][other_v][char_v]
            counts[1][other_v][char_v] += counts[0][other_v]
        counts[0][char_v] += 1
    return ans % MODULUS

def main():
    print(count_short_palindromes(input()))

if __name__ == '__main__':
    main()
