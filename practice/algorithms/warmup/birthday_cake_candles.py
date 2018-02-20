#!/usr/local/bin/pypy

def candles_blown_out(candle_heights):
    return candle_heights.count(max(candle_heights))

def main():
    size = input()
    heights = map(int, raw_input().strip().split(' '))
    print candles_blown_out(heights)

if __name__ == "__main__":
    main()