#!/usr/local/bin/pypy

def page_turns_from_front(target_page):
    return target_page / 2

def page_turns_from_back(target_page, total_pages):
    if total_pages % 2 == 0:
        return (total_pages - target_page + 1) / 2
    else:
        return (total_pages - target_page) / 2

def minimum_turns(target_page, total_pages):
    return min(page_turns_from_front(target_page), page_turns_from_back(target_page, total_pages))

def main():
    total_pages = input()
    target_page = input()
    print minimum_turns(target_page, total_pages)

if __name__ == "__main__":
    main()
