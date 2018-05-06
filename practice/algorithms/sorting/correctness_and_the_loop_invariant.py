#!/usr/local/bin/pypy3

def main():
    _, values = input(), [int(x) for x in input().strip().split(' ')]
    print(' '.join(map(str, sorted(values))))

if __name__ == '__main__':
    main()