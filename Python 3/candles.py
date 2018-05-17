# When a candle finishes burning it leaves a leftover. makeNew leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.
# You have candlesNumber candles in your possession. What's the total number of candles you can burn, assuming that you create new candles as soon as you have enough leftovers?


def candles(candlesNumber, makeNew):
    burned = 0
    leftovers = 0
    while candlesNumber > 0:
        burned += candlesNumber
        leftovers += candlesNumber
        candlesNumber = leftovers // makeNew
        leftovers %= makeNew
    return burned
