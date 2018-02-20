#!/usr/local/bin/pypy

YES = "Yes"
NO = "No"

def prefix_match_len(str_a, str_b):
    best = 0
    while best < len(str_a) and best < len(str_b) and str_a[best] == str_b[best]:
        best += 1
    return best

def minimum_distance(from_str, to_str):
    return len(from_str) + len(to_str) - 2 * prefix_match_len(from_str, to_str)

def distance_is_achievable(from_str, to_str, distance):
    if distance >= len(from_str) + len(to_str):
        return True
    else:
        minimum_dist = minimum_distance(from_str, to_str)
        return distance >= minimum_dist and (distance - minimum_dist) % 2 == 0

def main():
    from_str, to_str = raw_input(), raw_input()
    distance = input()
    print YES if distance_is_achievable(from_str, to_str, distance) else NO

if __name__ == "__main__":
    main()