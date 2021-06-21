import pandas as pd
from jugaad_trader import Zerodha
from datetime import datetime, timedelta

from pandas import DataFrame
from csv import writer
from jugaad_trader import Zerodha
from talib import RSI, WMA, EMA
from _thread import start_new_thread
import talib
import numpy as np
import pandas as pd
import pytz
from datetime import datetime, timedelta
from dateutil.tz import tzoffset
import csv

import logging


from datetime import datetime
from dateutil.tz import tzoffset


def get_timestamp():
    return datetime.now(tzoffset(None, 19800)).isoformat(' ', 'seconds')


def get_ltp(instrument_token):
    return kite.ltp(instrument_token)[str(instrument_token)]['last_price']

# Source for tech indicator : https://github.com/arkochhar/Technical-Indicators/blob/master/indicator/indicators.py


def ExponentialMovingAverage(df, base, target, period, alpha=False):
    """
    Function to compute Exponential Moving Average (EMA)
    Args :
        df : Pandas DataFrame which contains ['date', 'open', 'high', 'low', 'close', 'volume'] columns
        base : String indicating the column name from which the EMA needs to be computed from
        target : String indicates the column name to which the computed data needs to be stored
        period : Integer indicates the period of computation in terms of number of candles
        alpha : Boolean if True indicates to use the formula for computing EMA using alpha (default is False)
    Returns :
        df : Pandas DataFrame with new column added with name 'target'
    """

    con = pd.concat([df[:period][base].rolling(
        window=period).mean(), df[period:][base]])

    if (alpha == True):
        # (1 - alpha) * previous_val + alpha * current_val where alpha = 1 / period
        df[target] = con.ewm(alpha=1 / period, adjust=False).mean()
    else:
        # ((current_val - previous_val) * coeff) + previous_val where coeff = 2 / (period + 1)
        df[target] = con.ewm(span=period, adjust=False).mean()

    df[target].fillna(0, inplace=True)
    return df


def ATR(df, period, ohlc=['open', 'high', 'low', 'close']):
    """
    Function to compute Average True Range (ATR)
    Args :
        df : Pandas DataFrame which contains ['date', 'open', 'high', 'low', 'close', 'volume'] columns
        period : Integer indicates the period of computation in terms of number of candles
        ohlc: List defining OHLC Column names (default ['Open', 'High', 'Low', 'Close'])
    Returns :
        df : Pandas DataFrame with new columns added for
            True Range (TR)
            ATR (ATR_$period)
    """
    atr = 'ATR_' + str(period)

    # Compute true range only if it is not computed and stored earlier in the df
    if not 'TR' in df.columns:
        df['h-l'] = df[ohlc[1]] - df[ohlc[2]]
        df['h-yc'] = abs(df[ohlc[1]] - df[ohlc[3]].shift())
        df['l-yc'] = abs(df[ohlc[2]] - df[ohlc[3]].shift())

        df['TR'] = df[['h-l', 'h-yc', 'l-yc']].max(axis=1)

        df.drop(['h-l', 'h-yc', 'l-yc'], inplace=True, axis=1)

    # Compute ExponentialMovingAverage of true range using ATR formula after ignoring first row
    ExponentialMovingAverage(df, 'TR', atr, period, alpha=True)

    return df


supertrend_period = 21
supertrend_multiplier = 3


def SUPERTREND(df, period=supertrend_period, multiplier=supertrend_multiplier, ohlc=['open', 'high', 'low', 'close']):
    """
    Function to compute SUPERTREND
    Args :
        df : Pandas DataFrame which contains ['date', 'open', 'high', 'low', 'close', 'volume'] columns
        period : Integer indicates the period of computation in terms of number of candles
        multiplier : Integer indicates value to multiply the ATR
        ohlc: List defining OHLC Column names (default ['Open', 'High', 'Low', 'Close'])
    Returns :
        df : Pandas DataFrame with new columns added for
            True Range (TR), ATR (ATR_$period)
            SUPERTREND (ST_$period_$multiplier)
            SUPERTREND Direction (STX_$period_$multiplier)
    """

    ATR(df, period, ohlc=ohlc)
    atr = 'ATR_' + str(period)
    st = 'ST_' + str(period)  # + '_' + str(multiplier)
    stx = 'STX_' + str(period)  # + '_' + str(multiplier)

    """
    SUPERTREND Algorithm :
        BASIC UPPERBAND = (HIGH + LOW) / 2 + Multiplier * ATR
        BASIC LOWERBAND = (HIGH + LOW) / 2 - Multiplier * ATR
        FINAL UPPERBAND = IF( (Current BASICUPPERBAND < Previous FINAL UPPERBAND) or (Previous Close > Previous FINAL UPPERBAND))
                            THEN (Current BASIC UPPERBAND) ELSE Previous FINALUPPERBAND)
        FINAL LOWERBAND = IF( (Current BASIC LOWERBAND > Previous FINAL LOWERBAND) or (Previous Close < Previous FINAL LOWERBAND))
                            THEN (Current BASIC LOWERBAND) ELSE Previous FINAL LOWERBAND)
        SUPERTREND = IF((Previous SUPERTREND = Previous FINAL UPPERBAND) and (Current Close <= Current FINAL UPPERBAND)) THEN
                        Current FINAL UPPERBAND
                    ELSE
                        IF((Previous SUPERTREND = Previous FINAL UPPERBAND) and (Current Close > Current FINAL UPPERBAND)) THEN
                            Current FINAL LOWERBAND
                        ELSE
                            IF((Previous SUPERTREND = Previous FINAL LOWERBAND) and (Current Close >= Current FINAL LOWERBAND)) THEN
                                Current FINAL LOWERBAND
                            ELSE
                                IF((Previous SUPERTREND = Previous FINAL LOWERBAND) and (Current Close < Current FINAL LOWERBAND)) THEN
                                    Current FINAL UPPERBAND
    """

    # Compute basic upper and lower bands
    df['basic_ub'] = (df[ohlc[1]] + df[ohlc[2]]) / 2 + multiplier * df[atr]
    df['basic_lb'] = (df[ohlc[1]] + df[ohlc[2]]) / 2 - multiplier * df[atr]

    # Compute final upper and lower bands
    df['final_ub'] = 0.00
    df['final_lb'] = 0.00
    for i in range(period, len(df)):
        df['final_ub'].iat[i] = df['basic_ub'].iat[i] if df['basic_ub'].iat[i] < df['final_ub'].iat[i - 1] or \
            df[ohlc[3]].iat[i - 1] > df['final_ub'].iat[i - 1] else \
            df['final_ub'].iat[i - 1]
        df['final_lb'].iat[i] = df['basic_lb'].iat[i] if df['basic_lb'].iat[i] > df['final_lb'].iat[i - 1] or \
            df[ohlc[3]].iat[i - 1] < df['final_lb'].iat[i - 1] else \
            df['final_lb'].iat[i - 1]

    # Set the SUPERTREND value
    df[st] = 0.00
    for i in range(period, len(df)):
        df[st].iat[i] = df['final_ub'].iat[i] if df[st].iat[i - 1] == df['final_ub'].iat[i - 1] and df[ohlc[3]].iat[
            i] <= df['final_ub'].iat[i] else \
            df['final_lb'].iat[i] if df[st].iat[i - 1] == df['final_ub'].iat[i - 1] and df[ohlc[3]].iat[i] > \
            df['final_ub'].iat[i] else \
            df['final_lb'].iat[i] if df[st].iat[i - 1] == df['final_lb'].iat[i - 1] and df[ohlc[3]].iat[i] >= \
            df['final_lb'].iat[i] else \
            df['final_ub'].iat[i] if df[st].iat[i - 1] == df['final_lb'].iat[i - 1] and df[ohlc[3]].iat[i] < \
            df['final_lb'].iat[i] else 0.00

        # Mark the trend direction up/down
    df[stx] = np.where((df[st] > 0.00), np.where(
        (df[ohlc[3]] < df[st]), False, True), np.NaN)

    # Remove basic and final bands from the columns
    df.drop(['basic_ub', 'basic_lb', 'final_ub',
            'final_lb'], inplace=True, axis=1)

    df.fillna(0, inplace=True)
    return df


# kite = Zerodha()


# # Set access token loads the stored session.
# # Name chosen to keep it compatible with kiteconnect.
# kite.set_access_token()

# today = datetime.today()


# banknifty_instrument_token = 260105

# previous_session_ohlc = kite.historical_data(
#     banknifty_instrument_token, today - timedelta(days=21), today, "day")[-1]

# previous_session_date = previous_session_ohlc['date']


# banknifty_high = round(previous_session_ohlc['high'])
# banknifty_high = banknifty_high - (banknifty_high % 100)
# banknifty_low = round(previous_session_ohlc['low'])
# banknifty_low = banknifty_low - (banknifty_low % 100)

# nfo_instruments = pd.DataFrame(kite.instruments("NFO"))

# banknifty_instruments = nfo_instruments.loc[(
#     nfo_instruments.name == 'BANKNIFTY')]

# call_option = banknifty_instruments.loc[(banknifty_instruments.strike == banknifty_low) & (banknifty_instruments.instrument_type == 'CE')]
# print(call_option)


kite = Zerodha()


# Set access token loads the stored session.
# Name chosen to keep it compatible with kiteconnect.
kite.set_access_token()

today = datetime.today()
banknifty_instrument_token = 260105

historical = kite.historical_data(
    banknifty_instrument_token, today - timedelta(days=314), today, "day")
historical_data = DataFrame(historical)

print(historical_data.tail())

historical_data["ema210"] = EMA(historical_data.close, timeperiod=210)
historical_data["ema21"] = EMA(historical_data.close, timeperiod=21)

previous_session_ohlc = historical[-2]



previous_day_candle = historical_data.iloc[-2]

previous_session_date = previous_session_ohlc['date'].date()
banknifty_close = int(round(previous_day_candle['close'], -2))

if banknifty_close >= previous_day_candle.ema210:
    print("Long Term Trend: Positive")
else:
    print("Long Term Trend: Negative")

if banknifty_close >= previous_day_candle.ema21:
    print("Short Term Trend: Positive")
else:
    print("Short Term Trend: Negative")

banknifty_high = int(round(previous_session_ohlc['high'], -2))
banknifty_low = int(round(previous_session_ohlc['low'], -2))

nfo_instruments = pd.DataFrame(kite.instruments("NFO"))

banknifty_instruments = nfo_instruments.loc[(
    nfo_instruments.name == 'BANKNIFTY')]

tickertape = {}
strikes = []

monthly_options = banknifty_instruments.loc[banknifty_instruments.strike == banknifty_close, [
    'instrument_token', 'tradingsymbol']].head(2)
call_instrument_token, call_tradingsymbol = monthly_options.values[0]
put_instrument_token, put_tradingsymbol = monthly_options.values[1]
tickertape[call_instrument_token] = call_tradingsymbol
tickertape[put_instrument_token] = put_tradingsymbol
watchlist = (call_instrument_token, put_instrument_token)
