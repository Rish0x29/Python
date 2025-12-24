def calculate_sl_tp(row, direction):
    if row['atr'] < 100:
        stop_dist = 20
    else:
        stop_dist = 50

    if direction == "LONG":
        sl = row['close'] - stop_dist
        tp = row['close'] + stop_dist * 2
    else:
        sl = row['close'] + stop_dist
        tp = row['close'] - stop_dist * 2

    return sl, tp
