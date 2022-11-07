def time_description(hour, minute):
    time_to_str = {0: "o' clock", 1: 'one', 2: 'two', 3: 'three',
                   4: 'four', 5: 'five',
                   6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                   11: 'eleven', 12: 'twelve',
                   13: 'thirteen', 14: 'fourteen', 15: 'quarter',
                   16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                   19: 'nineteen', 20: 'twenty', 21: 'twenty one',
                   22: 'twenty two', 23: 'twenty three', 24: 'twenty four',
                   25: 'twenty five', 26: 'twenty six', 27: 'twenty seven',
                   28: 'twenty eight', 29: 'twenty nine', 30: 'half'}
    if hour > 12 or minute >= 60 or hour <= 0 or minute < 0:
        return "Incorrect input data!"
    if minute == 0:
        return f'{time_to_str[hour]} {time_to_str[0]}'
    if minute == 1:
        return f'{time_to_str[minute]} minute past {time_to_str[hour]}'
    elif minute == 15:
        return f'{time_to_str[minute]} past {time_to_str[hour]} '
    elif minute < 30:
        return f'{time_to_str[minute]} minutes past {time_to_str[hour]} '
    elif minute == 30:
        return f'{time_to_str[minute]} past {time_to_str[hour]} '
    elif minute == 59:
        return f'{time_to_str[60-minute]} minute to {time_to_str[hour+1]}'
    elif minute == 45:
        return f'{time_to_str[60-minute]} to {time_to_str[hour+1]} '
    elif minute > 30:
        return f'{time_to_str[60-minute]} minutes to {time_to_str[hour+1]}'
