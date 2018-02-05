def comparison_points(score_a, score_b):
    return sum(x > y for x, y in zip(score_a, score_b))

def read_triplet():
    return map(int, raw_input().strip().split(' '))

def main():
    a, b = read_triplet(), read_triplet()
    print comparison_points(a, b), comparison_points(b, a)

if __name__ == "__main__":
    main()