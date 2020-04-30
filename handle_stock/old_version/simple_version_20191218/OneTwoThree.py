
def one_two_three(code, open_value, close, high, one_rate=1, two_rate=1, three_rate=1):
    one_day = ''
    two_days = ''
    three_days = ''
    two_days_high = ''

    # open_value = history['open']
    # close = history['close']
    # high = history['high']

    if close[0] / close[1] >= one_rate and close[0] >= open_value[0]:
        one_day = code
        if close[1] / close[2] >= two_rate and close[1] >= open_value[1]:
            two_days = code
            if close[2] / close[3] >= three_rate and close[2] >= open_value[2]:
                three_days = code
            if close[0] >= high[1]:
                two_days_high = code

    return one_day, two_days, three_days, two_days_high

