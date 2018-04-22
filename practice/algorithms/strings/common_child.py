#!/usr/local/bin/pypy3

def longest_common_subsequence_length(s1, s2):
    lcs_lengths = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                lcs_lengths[i][j] = lcs_lengths[i - 1][j - 1] + 1
            else:
                lcs_lengths[i][j] = max(lcs_lengths[i - 1][j], lcs_lengths[i][j - 1])
    return lcs_lengths[len(s1)][len(s2)]

def main():
    print(longest_common_subsequence_length(input(), input()))

if __name__ == "__main__":
    main()