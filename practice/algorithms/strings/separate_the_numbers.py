#!/usr/local/bin/pypy3

def build_string(start, target_length):
    result, next_int = '', int(start)
    while len(result) < target_length:
        result += str(next_int)
        next_int += 1
    return result

def starting_integers(s):
    return map(lambda x: s[:x], range(1, len(s)))

def is_beautiful(s):
    for x in starting_integers(s):
        if build_string(x, len(s)) == s:
            return x
    return None

def main():
    for _ in range(int(input())):
        beautiful = is_beautiful(input())
        print('YES {0}'.format(beautiful) if beautiful else 'NO')

if __name__ == "__main__":
    main()