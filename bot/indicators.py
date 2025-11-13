def calculate_rsi(prices):
    gains = [prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]>prices[i]]
    losses = [prices[i]-prices[i+1] for i in range(len(prices)-1) if prices[i+1]<prices[i]]
    avg_gain = sum(gains)/len(gains) if gains else 0
    avg_loss = sum(losses)/len(losses) if losses else 1
    rs = avg_gain/avg_loss
    return 100 - (100/(1+rs))

def calculate_ma(prices):
    return sum(prices)/len(prices)
