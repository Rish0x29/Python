def generate_signal(row):
    # Trend filter
    if row['close'] > row['ema200']:
        bias = "LONG"
    elif row['close'] < row['ema200']:
        bias = "SHORT"
    else:
        return None

    # Volatility filter
    if row['atr'] < 20:
        return None

    # Momentum filter
    if bias == "LONG":
        if not (row['macd'] > row['macd_signal'] and row['macd'] < 0):
            return None
    else:
        if not (row['macd'] < row['macd_signal'] and row['macd'] > 0):
            return None

    return bias
