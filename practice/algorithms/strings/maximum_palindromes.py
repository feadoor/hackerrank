#!/usr/local/bin/pypy3

MODULUS = 1000000007

def initialise(s):
    initialise_factorials(s)
    initialise_inverses()
    initialise_counts(s)

def initialise_factorials(s):
    global FACTORIALS
    FACTORIALS = [1]
    for n in range(1, len(s) // 2 + 1):
        FACTORIALS.append((FACTORIALS[-1] * n) % MODULUS)

def initialise_inverses():
    global INVERSES
    INVERSES = {v : inverse(v, MODULUS) for v in FACTORIALS}

def initialise_counts(s):
    global COUNTS
    COUNTS = [{}]
    for _, c in enumerate(s):
        COUNTS.append(dict(COUNTS[-1]))
        COUNTS[-1][c] = COUNTS[-1].get(c, 0) + 1

def inverse(a, p):
    u1, u3 = 1, a
    v1, v3 = 0, p

    while v3 != 0:
        q = u3 // v3
        u1, v1 = v1, u1 - q * v1
        u3, v3 = v3, u3 - q * v3;

    return u1 if u1 >= 0 else u1 + p

def maximum_palindromes(start, end):
    counts = {k: COUNTS[end][k] - COUNTS[start - 1].get(k, 0) for k in COUNTS[end].keys()}
    double_counts = [x // 2 for x in counts.values() if x >= 2]
    leftovers = sum(x % 2 for x in counts.values())

    total_palindromes = FACTORIALS[sum(double_counts)]
    for x in double_counts:
        total_palindromes *= INVERSES[FACTORIALS[x]]
    if leftovers:
        total_palindromes *= leftovers
    return total_palindromes % MODULUS

def main():
    s = input()
    initialise(s)
    for _ in range(int(input())):
        start, end = [int(x) for x in input().strip().split(' ')]
        print(maximum_palindromes(start, end))

if __name__ == "__main__":
    main()