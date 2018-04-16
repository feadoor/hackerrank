#!/usr/local/bin/pypy3

YES = 'yes'
SWAP = 'swap'
REVERSE = 'reverse'
NO = 'no'

def read_space_separated_integers():
    return [int(x) for x in input().strip().split(' ')]

def extreme_elements(arr):
    for i in (x for x in range(len(arr) - 1) if arr[x] > arr[x + 1]):
        break
    for j in (x for x in reversed(range(1, len(arr))) if arr[x] < arr[x - 1]):
        break
    return i, j

def is_sorted(arr):
    return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))

def can_swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    ret = is_sorted(arr)
    arr[i], arr[j] = arr[j], arr[i]
    return ret

def can_reverse(arr, i, j):
    arr[i : j + 1] = reversed(arr[i : j + 1])
    ret = is_sorted(arr)
    arr[i : j + 1] = reversed(arr[i : j + 1])
    return ret

def main():
    _, arr = input(), read_space_separated_integers()
    i, j = extreme_elements(arr)

    if is_sorted(arr):
        print(YES)
    elif can_swap(arr, i, j):
        print(YES)
        print(SWAP, i + 1, j + 1)
    elif can_reverse(arr, i, j):
        print(YES)
        print(REVERSE, i + 1, j + 1)
    else:
        print(NO)

if __name__ == "__main__":
    main()