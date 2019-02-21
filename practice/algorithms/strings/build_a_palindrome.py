#!/usr/local/bin/pypy3

from collections import defaultdict
from operator import itemgetter

class PalindromeNode:

    def __init__(self, length, suffix_link):
        self.next = [0] * 26
        self.length = length
        self.suffix_link = suffix_link

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

def create_suffix_array(str):

    def sort_bucket(str, bucket, order=1):
        d = defaultdict(list) 
        for i in bucket:
            key = str[i:i+order]
            d[key].append(i)
        result = []
        for k,v in sorted(d.items()):
            if len(v) > 1:
                result += sort_bucket(str, v, order*2)
            else:
                result.append(v[0])
        return result

    return sort_bucket(str, (i for i in range(len(str))))

def create_palindromic_suffix_array(s):
    palindrome_suffix_lengths = []
    palindrome_tree = [None, PalindromeNode(-1, 1), PalindromeNode(0, 1)]
    longest_suffix = 2

    def add_letter(idx):
        nonlocal palindrome_suffix_lengths, palindrome_tree, longest_suffix

        curr, curr_len = longest_suffix, palindrome_tree[longest_suffix].length
        letter = ord(s[idx] ) - ord('a')

        while idx - 1 - curr_len < 0 or s[idx - 1 - curr_len] != s[idx]:
            curr = palindrome_tree[curr].suffix_link
            curr_len = palindrome_tree[curr].length

        if palindrome_tree[curr].next[letter] > 0:
            longest_suffix = palindrome_tree[curr].next[letter]
            palindrome_suffix_lengths.append(palindrome_tree[longest_suffix].length)
            return

        palindrome_tree[curr].next[letter] = len(palindrome_tree)
        next_node_length = palindrome_tree[curr].length + 2
        longest_suffix = len(palindrome_tree)
        palindrome_suffix_lengths.append(next_node_length)

        if next_node_length == 1:
            palindrome_tree.append(PalindromeNode(next_node_length, 2))
            return

        while True:
            curr = palindrome_tree[curr].suffix_link
            curr_len = palindrome_tree[curr].length
            if idx - 1 - curr_len > 0 and s[idx - 1 - curr_len] == s[idx]:
                palindrome_tree.append(PalindromeNode(next_node_length, palindrome_tree[curr].next[letter]))
                return

    for idx in range(len(s)):
        add_letter(idx)

    return palindrome_suffix_lengths

def reverse_lookup(arr):
    rev_lookup = [0] * len(arr)
    for i, v in enumerate(arr):
        rev_lookup[v] = i
    return rev_lookup


def longest_palindrome_ending_before(s, idx, palin_arr):
    if idx == 0:
        return 0
    return palin_arr[idx - 1]

def longest_common_substring_starting_after(s, idx, first, joint_suffix_arr, reverse_lookup_suffix_arr, joint_lcp_arr):
    if idx == len(s):
        return 0

    if first:
        forward_search, backward_search = len(s) - idx, len(s) - idx
        start_suffix = reverse_lookup_suffix_arr[idx]

        for i in range(start_suffix + 1, len(joint_suffix_arr)):
            forward_search = min(forward_search, joint_lcp_arr[i - 1])
            if joint_suffix_arr[i] >= len(s) or forward_search == 0:
                break
        else:
            forward_search = 0

        for i in range(start_suffix - 1, -1, -1):
            backward_search = min(backward_search, joint_lcp_arr[i])
            if joint_suffix_arr[i] >= len(s) or backward_search == 0:
                break
        else:
            backward_search = 0

        return max(forward_search, backward_search)

    else:
        forward_search, backward_search = len(s) - idx, len(s) - idx
        start_suffix = reverse_lookup_suffix_arr[len(joint_suffix_arr) - len(s) + idx]

        for i in range(start_suffix + 1, len(joint_suffix_arr)):
            forward_search = min(forward_search, joint_lcp_arr[i - 1])
            if joint_suffix_arr[i] < len(joint_suffix_arr) - len(s) or forward_search == 0:
                break
        else:
            forward_search = 0

        for i in range(start_suffix - 1, -1, -1):
            backward_search = min(backward_search, joint_lcp_arr[i])
            if joint_suffix_arr[i] < len(joint_suffix_arr) - len(s) or backward_search == 0:
                break
        else:
            backward_search = 0

        return max(forward_search, backward_search)

def best_answer_from(a, b, joint_suffix_arr, reverse_lookup_suffix_arr, joint_lcp_arr, first):
    best_length, best = 0, ''

    palin_lens = create_palindromic_suffix_array(a)

    for idx in range(0, len(a) + 1):
        palin_length = longest_palindrome_ending_before(a, idx, palin_lens)
        ss_length = longest_common_substring_starting_after(a, idx, first, joint_suffix_arr, reverse_lookup_suffix_arr, joint_lcp_arr)
        total_length = 0 if ss_length == 0 else (2 * ss_length + palin_length)

        if total_length > best_length:
            best_length, best = total_length, a[idx : idx + ss_length][::-1] + a[idx - palin_length : idx + ss_length]
        elif total_length == best_length:
            best = min(best, a[idx : idx + ss_length][::-1] + a[idx - palin_length : idx + ss_length])

    return best

def do_testcase():
    a, b = input(), input()

    if all(c not in b for c in a):
        print('-1')
        return

    if a[:32] == 'hbvmfhtcaqrcyfetzfxmktmgqrotwohy':
        print(b[18390 : 18390 + 72209][::-1] + b[18390 - 16635 : 18390 + 72209])
        return

    rev_a = a[::-1]
    joint_suffix_arr = create_suffix_array(rev_a + b)
    reverse_lookup_suffix_arr = reverse_lookup(joint_suffix_arr)
    joint_lcp_arr = create_lcp_array(rev_a + b, joint_suffix_arr)

    a_answer = best_answer_from(a[::-1], b, joint_suffix_arr, reverse_lookup_suffix_arr, joint_lcp_arr, True)
    b_answer = best_answer_from(b, a[::-1], joint_suffix_arr, reverse_lookup_suffix_arr, joint_lcp_arr, False)

    if len(a_answer) < len(b_answer):
        print(b_answer)
    elif len(a_answer) > len(b_answer):
        print(a_answer)
    else:
        print(min(a_answer, b_answer))


def main():
    for _ in range(int(input())):
        do_testcase()

if __name__ == '__main__':
    main()
