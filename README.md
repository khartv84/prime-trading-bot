# Prime Spot DCA Trading Bot

An open-source demo framework for building automated **DCA (Dollar-Cost Averaging)** trading bots on **Binance Spot**.

This repository contains example code structure, configuration, and documentation to help developers understand how DCA logic can be implemented safely.

> Learn more about the full version of this bot at [PrimeTradingBot.com](https://primetradingbot.com)  
> or read the product overview: [Prime Spot DCA Trading Bot](https://primetradingbot.com/spotdca.html)

---

## Features (Example)

- DCA buying logic with safety orders  
- Technical indicators (RSI, MA, MACD, ADX, Bollinger Bands, and Volume)  
- Configurable take-profit and trailing profit logic  
- Logging and state persistence  
- GUI-ready structure

---

## Example Setup (Demo Only)

### 1. Clone repository
```bash
git clone https://github.com/yourusername/prime-trading-bot.git
cd prime-trading-bot

### 2. Create virtual environment
python -m venv venv

Activate venv
- Windows PowerShell:
.\venv\Scripts\Activate.ps1

- Linux/macOS:
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run example
python bot/main.py