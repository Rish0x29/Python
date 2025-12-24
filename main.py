import pandas as pd
from indicators import add_indicators
from strategy import generate_signal
from risk import calculate_sl_tp

df = pd.read_csv("data/sample.csv")
df = add_indicators(df)

signals = []

for i in range(len(df)):
    signal = generate_signal(df.iloc[i])
    if signal:
        sl, tp = calculate_sl_tp(df.iloc[i], signal)
        signals.append({
            "time": df.iloc[i]['time'],
            "signal": signal,
            "entry": df.iloc[i]['close'],
            "sl": sl,
            "tp": tp
        })

print(signals[:5])
