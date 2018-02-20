#!/usr/local/bin/pypy

def total_likes(days):
    total, liked_on_day = 0, 2
    for _ in xrange(days):
        total += liked_on_day
        liked_on_day = (3 * liked_on_day) / 2
    return total

def main():
    days = input()
    print total_likes(days)

if __name__ == "__main__":
    main()