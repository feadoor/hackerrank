def height_after_cycles(n_cycles):
    full_cycles = n_cycles / 2
    summer_height = (1 << (full_cycles + 1)) - 1
    return 2 * summer_height if n_cycles & 1 else summer_height

def main():
    tests = input()
    for _ in xrange(tests):
        print height_after_cycles(input())

if __name__ =="__main__":
    main()