#!/usr/local/bin/pypy3

def have_common_substring(s1, s2):
    return bool(set(s1) & set(s2))

def main():
    for _ in range(int(input())):
        print('YES' if have_common_substring(input(), input()) else 'NO')

if __name__ == "__main__":
    main()