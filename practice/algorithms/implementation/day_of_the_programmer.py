def is_leap_year_julian(year):
    return year % 4 == 0

def is_leap_year_gregorian(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_russian_leap_year(year):
    return is_leap_year_julian(year) if year < 1918 else is_leap_year_gregorian(year)

def programmer_day(year):
    if year == 1918:
        return '26.09.1918'
    else:
        return '12.09.{}'.format(year) if is_russian_leap_year(year) else '13.09.{}'.format(year)

def main():
    year = input()
    print programmer_day(year)

if __name__ == "__main__":
    main()