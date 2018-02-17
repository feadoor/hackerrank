def reversed(n):
    return int(str(n)[::-1])

def is_beautiful(n, factor):
    return (n - reversed(n)) % factor == 0

def beautiful_days(lo, hi, factor):
    return sum(1 for n in xrange(lo, hi + 1) if is_beautiful(n, factor))

def main():
    lo, hi, factor = map(int, raw_input().strip().split(' '))
    print beautiful_days(lo, hi, factor)

if __name__ == "__main__":
    main()