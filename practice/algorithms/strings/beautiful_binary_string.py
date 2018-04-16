#!/usr/local/bin/pypy3

def changes_required(arr):
    changes = 0
    for i in range(len(arr) - 2):
        if arr[i : i + 3] == [0, 1, 0]:
            arr[i + 2] = 1
            changes += 1
    return changes

def main():
    _, arr = input(), [int(x) for x in input()]
    print(changes_required(arr))

if __name__ == "__main__":
    main()