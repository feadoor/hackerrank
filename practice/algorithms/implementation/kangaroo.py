#!/usr/local/bin/pypy

YES = 'YES'
NO = 'NO'

def meets(position_1, speed_1, position_2, speed_2):
    position_delta, speed_delta = position_2 - position_1, speed_2 - speed_1

    if speed_delta == 0:
        return position_delta == 0
    elif speed_delta > 0:
        return position_delta < 0 and position_delta % speed_delta == 0
    else:
        return position_delta > 0 and position_delta % speed_delta == 0

def main():
    pos_1, speed_1, pos_2, speed_2 = map(int, raw_input().strip().split(' '))
    print YES if meets(pos_1, speed_1, pos_2, speed_2) else NO

if __name__ == "__main__":
    main()