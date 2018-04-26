#!/usr/local/bin/python3

from collections import defaultdict, namedtuple

Offset = namedtuple('Offset', ['pos1', 'pos2'])

def diff(offset):
    return offset.pos1 - offset.pos2

def incr1(offset):
    return Offset(offset.pos1 + 1, offset.pos2)

def incr2(offset):
    return Offset(offset.pos1, offset.pos2 + 1)

def minimal_string(s1, s2):
    s1, s2 = s1 + '~', s2 + '~'
    skips = defaultdict(lambda: Offset(-1, -1))
    current_offset = Offset(0, 0)
    result = ''

    while current_offset != Offset(len(s1) - 1, len(s2) - 1):

        if current_offset.pos1 <= skips[diff(current_offset)].pos1:
            diff_offset = skips[diff(current_offset)]
        else:
            x, y = current_offset.pos1, current_offset.pos2
            while x < len(s1) - 1 and y < len(s2) - 1 and s1[x] == s2[y]:
                x, y = x + 1, y + 1
            diff_offset = skips[diff(current_offset)] = Offset(x, y)

        if s1[diff_offset.pos1] <= s2[diff_offset.pos2]:
            result += s1[current_offset.pos1]
            current_offset = incr1(current_offset)
        else:
            result += s2[current_offset.pos2]
            current_offset = incr2(current_offset)

    return result

def main():
    for _ in range(int(input())):
        print(minimal_string(input(), input()))

if __name__ == "__main__":
    main()