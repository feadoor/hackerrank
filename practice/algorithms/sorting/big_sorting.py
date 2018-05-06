#!/usr/local/bin/pypy3

def main():
    items = [input() for _ in range(int(input()))]
    print('\n'.join(sorted(items, key=lambda s: (len(s), s))))

if __name__ == '__main__':
    main()
