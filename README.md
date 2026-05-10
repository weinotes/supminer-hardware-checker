# SupMiner Hardware Checker · 硬件检测工具

🔍 Auto-detect hardware and recommend mainstream mineable cryptocurrencies.
🔍 自动检测硬件配置，推荐主流挖矿项目

**Author:** Davey Wong <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

---

## Quick Start · 快速开始

### 1. Install · 安装

```bash
git clone https://github.com/weinotes/supminer-hardware-checker.git
cd supminer-hardware-checker
pip install -e .
# Optional: pip install -e .[rich]  for pretty CLI output
```

### 2. Run · 运行

```bash
python -m supminer_hardware_checker
# or: supminer-check
# or: make run
```

---

## What It Detects · 检测内容

| Category | What's checked | Description |
|----------|---------------|-------------|
| 💻 **OS** | System type, version, arch | Windows / macOS / Linux |
| 🧠 **CPU** | Model, cores, frequency, usage | Physical + logical cores |
| 💾 **RAM** | Total, available | Displayed in GB |
| 🎮 **GPU** | Vendor, model, VRAM, driver | NVIDIA (nvidia-smi) / AMD (lspci) |

---

## Recommended Coins · 推荐项目

### GPU Mining · 显卡挖矿

| Coin | Algorithm | Exchanges | Pools |
|------|-----------|-----------|-------|
| **ETC** Ethereum Classic | Etchash | Binance, OKX, Coinbase | F2Pool, AntPool |
| **RVN** Ravencoin | KawPow | Binance, OKX, KuCoin | F2Pool, 2Miners |
| **KAS** Kaspa | kHeavyHash | Binance, OKX, KuCoin | F2Pool, Hashpool |
| **ERG** Ergo | Autolykos v2 | Binance, KuCoin, Gate.io | F2Pool, Herominers |

### CPU Mining · 处理器挖矿

| Coin | Algorithm | Exchanges | Pools |
|------|-----------|-----------|-------|
| **XMR** Monero | RandomX | Binance, Kraken | F2Pool, SupportXMR |

### ASIC Mining · 专业矿机

| Coin | Algorithm | Recommended Miners |
|------|-----------|-------------------|
| **BTC** Bitcoin | SHA-256 | Antminer S21, Whatsminer M60 |
| **LTC** Litecoin | Scrypt | Antminer L7, Goldshell KD6 |
| **DOGE** Dogecoin | Scrypt | Merge mine with LTC |

---

## Project Structure · 项目结构

```
supminer-hardware-checker/
├── src/supminer_hardware_checker/
│   ├── __init__.py      # Package metadata · 包元数据
│   ├── __main__.py      # Entry: python -m
│   ├── detector.py      # Core detection logic · 核心逻辑
│   └── data.py          # Mining project data · 挖矿数据
├── pyproject.toml       # Build config · 构建配置
├── Makefile             # Common tasks · 常用命令
└── ...docs & license
```

---

## Development · 开发

```bash
pip install -e .[rich]
make test     # 测试导入
make lint     # 语法检查
make clean    # 清理
```

---

## Criteria · 项目标准

This tool only recommends coins that are:
本工具只推荐符合以下条件的币种：

1. **Listed on major exchanges** — Binance, OKX, Coinbase, etc. · 已上线主流交易所
2. **Supported by major pools** — F2Pool, AntPool, etc. · 大型矿池支持
3. **Top market cap** — sufficient liquidity · 市值排名靠前
4. **Long-term stable** — mature projects with active communities · 长期稳定运营

---

## Disclaimer · 免责声明

Mining profitability depends on electricity costs, hardware performance, coin price volatility, and network difficulty. Cryptocurrency investment carries risk. Please comply with local laws and regulations.
挖矿收益受市场、硬件、电费等因素影响。加密货币投资有风险，请充分评估后决策。请遵守当地法律法规。

---

## License

MIT License — see [LICENSE](LICENSE)

---

**Davey Wong** <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)
