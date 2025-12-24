import pandas as pd
import ta

def add_indicators(df):
    df['ema200'] = ta.trend.EMAIndicator(df['close'], 200).ema_indicator()
    df['ema50'] = ta.trend.EMAIndicator(df['close'], 50).ema_indicator()

    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    df['macd_hist'] = macd.macd_diff()

    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['atr'] = ta.volatility.AverageTrueRange(
        df['high'], df['low'], df['close']
    ).average_true_range()

    return df
