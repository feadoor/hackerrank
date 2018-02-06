from collections import Counter

def matching_pairs(socks):
    counts = Counter(socks)
    return sum(x / 2 for x in counts.itervalues())

def main():
    n = input()
    socks = map(int, raw_input().strip().split(' '))
    print matching_pairs(socks)

if __name__ == "__main__":
    main()