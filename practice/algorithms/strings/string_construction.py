#!/usr/local/bin/pypy3

def cost(s):
    return len(set(s))

def main():
    for _ in range(int(input())):
        print(cost(input()))

if __name__ == "__main__":
    main()