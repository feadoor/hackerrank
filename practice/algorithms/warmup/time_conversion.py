AM = 'AM'
PM = 'PM'

def get_constituent_parts(time_str):
    hours, minutes, seconds_and_ampm = time_str.split(':')
    return int(hours), int(minutes), int(seconds_and_ampm[:2]), seconds_and_ampm[2:]

def write_as_military_time(hours, minutes, seconds, ampm):
    if ampm == PM and hours != 12:
        hours += 12
    elif ampm == AM and hours == 12:
        hours = 0
    return "{0:02}:{1:02}:{2:02}".format(hours, minutes, seconds)

def convert(time_str):
    return write_as_military_time(*get_constituent_parts(time_str))

def main():
    time = raw_input().strip()
    print convert(time)

if __name__ == "__main__":
    main()