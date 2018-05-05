#!/usr/local/bin/pypy3

from operator import itemgetter

def create_lcp_array(s, suffix_array):
    n, lcp, k = len(s), [0] * len(s), 0

    reverse_lookup = [0] * n
    for i, v in enumerate(suffix_array):
        reverse_lookup[v] = i

    for i in range(n):
        if reverse_lookup[i] == n - 1:
            k = 0
        else:
            j = suffix_array[reverse_lookup[i] + 1]
            while i + k < n and j + k < n and s[i + k] == s[j + k]:
                k += 1
            lcp[reverse_lookup[i]] = k
        if k > 0:
            k -= 1
    return lcp

def create_suffix_array_and_lcp(s):
    suffixes = [[idx, -1, ord(c)] for (idx, c) in enumerate(s)]
    suffixes.sort(key=itemgetter(1, 2))

    n, k, indexes = len(s), 1, [0] * len(s)
    while k < n:

        cmp_rank = suffixes[0][1]
        rank = suffixes[0][1] = 0
        indexes[suffixes[0][0]] = 0

        for idx in range(1, n):
            indexes[suffixes[idx][0]] = idx
            if suffixes[idx][1] == cmp_rank and suffixes[idx][2] == suffixes[idx - 1][2]:
                suffixes[idx][1] = rank
            else:
                rank += 1
                cmp_rank, suffixes[idx][1] = suffixes[idx][1], rank

        for idx in range(n):
            next_idx = suffixes[idx][0] + k
            suffixes[idx][2] = suffixes[indexes[next_idx]][1] if next_idx < n else -1

        suffixes.sort(key=itemgetter(1, 2))
        k *= 2

    suffix_array = [s[0] for s in suffixes]
    return suffix_array, create_lcp_array(s, suffix_array)

def maximum_value(s):
    sa, lcp = create_suffix_array_and_lcp(s)
    n, best_result = len(s), len(s)

    for i in range(n):
        count = 2
        for j in range(i + 1, n):
            if lcp[j] >= lcp[i]: count += 1
            else: break
        for j in range(i - 1, -1, -1):
            if lcp[j] >= lcp[i]: count += 1
            else: break
        best_result = max(best_result, count * lcp[i])

    return best_result

def main():
    print(maximum_value(input()))

if __name__ == '__main__':
    main()
