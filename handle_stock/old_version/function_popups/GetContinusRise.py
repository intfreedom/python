import tushare as ts

def continuous(ticket, growthRate = 0.01, opentVSclosey = 0.98):
    # dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
    # Notice: the value of two function is not same, get_hist_data, get_realtime_quotes
    Point80 = ''
    Point90 = ''
    Point95 = ''

    history = ts.get_hist_data(ticket)
    op = history['open']
    close = history['close']
    low = history['low']
    thisYesterday = ts.get_hist_data(ticket)
    closeYesterday = thisYesterday['close'][0]
    openYesterday = thisYesterday['open'][0]
    highYesterday = thisYesterday['high'][0]
    closeBeforeY = thisYesterday['close'][1]
    openBeforeY = thisYesterday['open'][1]
    print(thisYesterday, closeYesterday, openYesterday)

    thisToday = ts.get_realtime_quotes(ticket)
    openToday = thisToday['open'][0]
    priceToday = thisToday['price'][0]
    lowToday = thisToday['low'][0]
    openTodayValue = float(openToday)
    priceTodayValue = float(priceToday)
    lowTodayValue = float(lowToday)
    print(openTodayValue, priceTodayValue, lowTodayValue)
    # I think this one, can be, (close[0]>close[1] or open[0]>close[1] or hi>close[1]) and close[0]>op[0]
    # (close[0] - op[0]) / op[0] >= 1% and close[0] > close[1] the final
    if (close[0] - op[0]) / op[0] >= growthRate and (close[0] > close[1]):
        if lowTodayValue >= openYesterday and priceTodayValue > openTodayValue:
            # if lowTodayValue >= openYesterday and (priceTodayValue - openTodayValue)/openTodayValue>=0.01:
            Point80 = ticket
            if priceTodayValue >= 1.01 * closeYesterday and openTodayValue >= closeYesterday:
                Point90 = ticket
            # if lowTodayValue >= closeYesterday and (closeBeforeY - openBeforeY) / openBeforeY >= 0.01:
            #     Point90 = ticket
            #     if lowTodayValue > highYesterday:
            #         Point95 = ticket
    return Point80, Point90, Point95
