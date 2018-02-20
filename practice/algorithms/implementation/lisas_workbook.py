#!/usr/local/bin/pypy

def special_problems(chapters, per_page):
    current_chapter, current_problem, current_page = 0, 1, 1
    special_problems = 0

    while True:
        highest_problem_on_page = min(current_problem + per_page - 1, chapters[current_chapter])
        if current_problem <= current_page <= highest_problem_on_page:
            special_problems += 1

        current_page += 1
        if highest_problem_on_page == chapters[current_chapter]:
            current_problem, current_chapter = 1, current_chapter + 1
        else:
            current_problem = highest_problem_on_page + 1
        if current_chapter == len(chapters):
            break

    return special_problems

def read_space_separated_integers():
    return map(int, raw_input().strip().split(' '))

def main():
    _, per_page = read_space_separated_integers()
    chapters = read_space_separated_integers()
    print special_problems(chapters, per_page)

if __name__ == "__main__":
    main()