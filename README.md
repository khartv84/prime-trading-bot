# Prime Spot DCA Trading Bot
Welcome to the **Prime Spot DCA Trading Bot** – the ultimate automated trading solution for Binance. Built for both stability and aggressive growth, v4.0 introduces a robust Client-Server architecture and lightning-fast asynchronous market data processing.

> Learn more about the full version of this bot at [PrimeTradingBot.com](https://primetradingbot.com)  
> or read the product overview: [Prime Spot DCA Trading Bot](https://primetradingbot.com/spotdca.html)

# Prime Spot DCA Trading Bot v4.0 🚀
## 🌟 What's New in v4.0?
* **Client-Server WebSocket Architecture:** Run the server securely on your VPS while monitoring and controlling your bot locally via the lightweight UI Client.
* **Asynchronous Engine:** Upgraded to `ccxt.async_support` for sub-second market data fetching across 1400+ pairs.
* **Smart Isolate & Dust Sweeping:** Manually isolate specific pairs for targeted take-profit. The bot now automatically detects and sweeps "dust" (assets < $2) to prevent order clutter.
* **Zero-Setup Executables:** Fully compiled with Nuitka. No need to install Python, pip, or complex dependencies (if using the provided standalone binaries).
* **Enhanced Testnet Stability:** Fully bypasses strict WAF and network restrictions for seamless Sandbox testing.

## ⚡ Core Features
- **DCA (Dollar Cost Averaging):** Configurable safety orders, volume scaling, and step percentages.
- **Dynamic & Trailing Take Profit:** Lock in profits as the market surges using ATR multipliers and trailing percentages.
- **Advanced Technical Indicators:** RSI, MACD, ADX, Bollinger Bands, and Volume filters built-in.
- **Auto-Capital Allocation:** Smart capital division based on user-defined limits.

## 🛠️ Installation & Usage
Please refer to our detailed documentation or use the automated installation script for Linux VPS:
```bash
curl -sO [https://raw.githubusercontent.com/khartv84/prime-trading-bot/main/install.sh](https://raw.githubusercontent.com/khartv84/prime-trading-bot/main/install.sh) && bash install.sh

![Prime Bot GUI](/assets/images/screenshot.png)
---
