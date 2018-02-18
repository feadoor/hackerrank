NUMBERS = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one',
    'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six',
    'twenty seven', 'twenty eight', 'twenty nine', 'thirty'
]
OCLOCK = 'o\' clock'
QUARTER_PAST = 'quarter past'
HALF_PAST = 'half past'
QUARTER_TO = 'quarter to'
MINUTE_PAST = 'minute past'
MINUTE_TO = 'minute to'
MINUTES_PAST = 'minutes past'
MINUTES_TO = 'minutes to'

def time_in_words(hour, minute):
    next_hour = hour + 1 if hour < 12 else 1
    if minute == 0:
        return NUMBERS[hour] + ' ' + OCLOCK
    elif minute == 15:
        return QUARTER_PAST + ' ' + NUMBERS[hour]
    elif minute == 30:
        return HALF_PAST + ' ' + NUMBERS[hour]
    elif minute == 45:
        next_hour
        return QUARTER_TO + ' ' + NUMBERS[next_hour]
    elif minute == 1:
        return NUMBERS[minute] + ' ' + MINUTE_PAST + ' ' + NUMBERS[hour]
    elif minute == 59:
        return NUMBERS[60 - minute] + ' ' + MINUTE_TO + ' ' + NUMBERS[hour]
    elif minute < 30:
        return NUMBERS[minute] + ' ' + MINUTES_PAST + ' ' + NUMBERS[hour]
    else:
        return NUMBERS[60 - minute] + ' ' + MINUTES_TO + ' ' + NUMBERS[next_hour]

def main():
    hour, minute = input(), input()
    print time_in_words(hour, minute)

if __name__ == "__main__":
    main()