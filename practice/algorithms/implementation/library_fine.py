from collections import namedtuple

Date = namedtuple('Date', ['day', 'month', 'year'])

def fine(due_date, returned_date):
    YEAR_FINE, MONTH_FINE, DAY_FINE = 10000, 500, 15
    if returned_date.year > due_date.year:
        return YEAR_FINE
    elif returned_date.year == due_date.year and returned_date.month > due_date.month:
        return MONTH_FINE * (returned_date.month - due_date.month)
    elif returned_date.year == due_date.year and returned_date.month == due_date.month and returned_date.day > due_date.day:
        return DAY_FINE * (returned_date.day - due_date.day)
    else:
        return 0

def read_date():
    return Date(*map(int, raw_input().strip().split(' ')))

def main():
    returned_date, due_date = read_date(), read_date()
    print fine(due_date, returned_date)

if __name__ == "__main__":
    main()