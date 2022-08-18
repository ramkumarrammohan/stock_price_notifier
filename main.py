from yahoo_finance.Ticker import LiveTicker

if __name__ == '__main__':
    print('!!! app started !!!')

    ticker = LiveTicker()
    ticker.add_symbol('INFY.NS')
    ticker.add_symbol('TATASTEEL.NS')
    err, price_list = ticker.get_current_price()
    if err == False:
        print(price_list)
    else:
        print('Err: get_current_price')