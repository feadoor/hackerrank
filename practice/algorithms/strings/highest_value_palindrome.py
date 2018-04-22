#!/usr/local/bin/pypy3

def non_matching_count(s):
    return sum(s[x] != s[len(s) - x - 1] for x in range(len(s) // 2))

def highest_palindrome(s, changes_allowed):
    changes_required = non_matching_count(s)
    if changes_required > changes_allowed:
        return -1

    new_left = ''
    for idx in range(len(s) // 2):

        if s[idx] == s[len(s) - 1 - idx]:
            if s[idx] != '9' and changes_allowed >= changes_required + 2:
                new_left += '9'
                changes_allowed -= 2
            else:
                new_left += s[idx]

        else:
            if s[idx] == '9' or s[len(s) - 1 - idx] == '9':
                new_left += '9'
                changes_allowed -= 1
                changes_required -= 1
            elif changes_allowed >= changes_required + 1:
                new_left += '9'
                changes_allowed -= 2
                changes_required -= 1
            else:
                new_left += max(s[idx], s[len(s) - 1 - idx])
                changes_allowed -= 1
                changes_required -= 1

    middle_char = '' if len(s) % 2 == 0 else '9' if changes_allowed > 0 else s[len(s) // 2]
    return new_left + middle_char + new_left[::-1]

def main():
    _, changes = [int(x) for x in input().strip().split(' ')]
    print(highest_palindrome(input(), changes))

if __name__ == "__main__":
    main()