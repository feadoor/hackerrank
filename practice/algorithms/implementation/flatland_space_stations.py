#!/usr/local/bin/pypy

def maximum_distance_to_station(stations, city_size):
    sorted_stations = sorted(stations)
    if len(stations) > 1:
        maximum_internal_distance = max((sorted_stations[i + 1] - sorted_stations[i]) / 2 for i in xrange(len(stations) - 1))
    else:
        maximum_internal_distance = 0
    return max(maximum_internal_distance, sorted_stations[0], city_size - sorted_stations[-1] - 1)

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    city_size, _ = read_space_separated_integers()
    stations = read_space_separated_integers()
    print maximum_distance_to_station(stations, city_size)

if __name__ == "__main__":
    main()