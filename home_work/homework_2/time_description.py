def time_description(hour, minute):
    time_to_str = {0: "o' clock", 1: 'one minute', 2: 'two minutes',
                   3: 'three minutes', 4: 'four minutes', 5: 'five minutes',
                   6: 'six minutes', 7: 'seven minutes', 8: 'eight minutes',
                   9: 'nine minutes', 10: 'ten minutes',
                   11: 'eleven minutes', 12: 'twelve minutes',
                   13: 'thirteen minutes', 14: 'fourteen minutes',
                   15: 'quarter', 16: 'sixteen minutes',
                   17: 'seventeen minutes', 18: 'eighteen minutes',
                   19: 'nineteen minutes', 20: 'twenty minutes',
                   21: 'twenty one minutes', 22: 'twenty two minutes',
                   23: 'twenty three minutes', 24: 'twenty four minutes',
                   25: 'twenty five minutes', 26: 'twenty six minutes',
                   27: 'twenty seven minutes', 28: 'twenty eight minutes',
                   29: 'twenty nine minutes', 30: 'half'}
    if hour not in range(1, 13) or minute not in range(0, 60):
        return "Incorrect input data!"
    elif minute == 0:
        return f'{time_to_str[hour].split()[0]} {time_to_str[minute]}'
    elif hour == 12 and minute > 30:
        return f'{time_to_str[60 - minute]} to one'
    elif minute <= 30:
        return f'{time_to_str[minute]} past {time_to_str[hour].split()[0]}'
    else:
        return f'{time_to_str[60-minute]} to {time_to_str[hour+1].split()[0]}'
