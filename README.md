# SupMiner Hardware Checker

🔍 Auto-detect hardware and recommend mainstream mineable cryptocurrencies.

**Author:** Davey Wong <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

---

## Quick Start

```bash
git clone https://github.com/weinotes/supminer-hardware-checker.git
cd supminer-hardware-checker
pip install -e .
# Optional: pip install -e .[rich]  for pretty CLI output
python -m supminer_hardware_checker
```

---

## What It Detects

| Category | Description |
|----------|-------------|
| 💻 **OS** | System type, version, architecture |
| 🧠 **CPU** | Model, physical/logical cores, frequency, usage |
| 💾 **RAM** | Total and available capacity in GB |
| 🎮 **GPU** | Vendor, model, VRAM, driver version |

---

## Recommended Coins

### GPU Mining

| Coin | Algorithm | Exchanges | Pools |
|------|-----------|-----------|-------|
| **ETC** Ethereum Classic | Etchash | Binance, OKX, Coinbase | F2Pool, AntPool |
| **RVN** Ravencoin | KawPow | Binance, OKX, KuCoin | F2Pool, 2Miners |
| **KAS** Kaspa | kHeavyHash | Binance, OKX, KuCoin | F2Pool, Hashpool |
| **ERG** Ergo | Autolykos v2 | Binance, KuCoin, Gate.io | F2Pool, Herominers |

### CPU Mining

| Coin | Algorithm | Exchanges | Pools |
|------|-----------|-----------|-------|
| **XMR** Monero | RandomX | Binance, Kraken | F2Pool, SupportXMR |

### ASIC Mining

| Coin | Algorithm | Recommended Miners |
|------|-----------|-------------------|
| **BTC** Bitcoin | SHA-256 | Antminer S21, Whatsminer M60 |
| **LTC** Litecoin | Scrypt | Antminer L7, Goldshell KD6 |
| **DOGE** Dogecoin | Scrypt | Merge mine with LTC |

---

## Project Structure

```
supminer-hardware-checker/
├── src/supminer_hardware_checker/
│   ├── __init__.py
│   ├── __main__.py
│   ├── detector.py
│   └── data.py
├── pyproject.toml
├── Makefile
└── ...
```

---

## Selection Criteria

This tool only recommends coins that are:

1. **Listed on major exchanges** — Binance, OKX, Coinbase, etc.
2. **Supported by major pools** — F2Pool, AntPool, etc.
3. **Top market cap** — sufficient liquidity
4. **Long-term stable** — mature, active communities

---

## Disclaimer

Mining profitability depends on electricity costs, hardware performance, coin price volatility, and network difficulty. Cryptocurrency investment carries risk. Please comply with local laws.

---

## License

MIT License — see [LICENSE](LICENSE)

---

**Davey Wong** <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)
