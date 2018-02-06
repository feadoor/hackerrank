UP = 'U'
DOWN = 'D'

def count_valleys(steps):
    level, valleys = 0, 0

    for step in steps:
        next_level = level + 1 if step == UP else level - 1
        if next_level == 0 and level < 0:
            valleys += 1
        level = next_level

    return valleys

def main():
    n = input()
    steps = raw_input().strip()
    print count_valleys(steps)

if __name__ == "__main__":
    main()
