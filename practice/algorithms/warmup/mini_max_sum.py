def minimum_sum(arr):
    return sum(arr) - max(arr)

def maximum_sum(arr):
    return sum(arr) - min(arr)

def main():
    array = map(int, raw_input().strip().split(' '))
    print minimum_sum(array), maximum_sum(array)

if __name__ == "__main__":
    main()