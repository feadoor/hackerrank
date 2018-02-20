#!/usr/local/bin/pypy

def rounded_grade(grade):
    if grade < 38 or grade % 5 < 3:
        return grade
    else:
        return grade + 5 - grade % 5

def main():
    num_grades = input()
    for _ in xrange(num_grades):
        print rounded_grade(input())

if __name__ == "__main__":
    main()