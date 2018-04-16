#!/usr/local/bin/pypy3

def caesar(rot):
    def inner(c):
        if c.isalpha() and c.islower():
            return chr(ord('a') + (ord(c) - ord('a') + rot) % 26)
        elif c.isalpha() and c.isupper():
            return chr(ord('A') + (ord(c) - ord('A') + rot) % 26)
        else:
            return c
    return inner

def encrypt(s, rot):
    return ''.join(map(caesar(rot), s))

def main():
    _, plaintext = input(), input()
    rot = int(input())
    print(encrypt(plaintext, rot))

if __name__ == "__main__":
    main()