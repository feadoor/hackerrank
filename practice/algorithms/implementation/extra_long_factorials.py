def factorial(n):
    return reduce(lambda x, y: x * y, xrange(1, n + 1))

def main():
    print factorial(input())

if __name__ == "__main__":
    main()