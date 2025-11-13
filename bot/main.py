import time
from indicators import calculate_rsi, calculate_ma

def main():
    print("Starting Prime Spot DCA Trading Bot (Demo Mode)...")
    prices = [100, 98, 97, 99, 101, 102]
    rsi = calculate_rsi(prices)
    ma = calculate_ma(prices)
    print(f"RSI: {rsi:.2f}, MA: {ma:.2f}")
    print("Simulated DCA logic running...")
    time.sleep(1)
    print("Demo complete. Visit https://primetradingbot.com for full features.")

if __name__ == "__main__":
    main()
