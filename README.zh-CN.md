# SupMiner 硬件检测工具

🔍 自动检测硬件配置，推荐主流挖矿项目

**作者：** Davey Wong <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

---

## 快速开始

```bash
git clone https://github.com/weinotes/supminer-hardware-checker.git
cd supminer-hardware-checker
pip install -e .
# 可选安装 rich 美化输出：pip install -e .[rich]
python -m supminer_hardware_checker
```

---

## 检测内容

| 类别 | 说明 |
|------|------|
| 💻 **操作系统** | 类型、版本、架构 |
| 🧠 **CPU** | 型号、物理/逻辑核心数、频率、使用率 |
| 💾 **内存** | 总容量和可用容量（GB） |
| 🎮 **GPU** | 厂商、型号、显存、驱动版本 |

---

## 推荐项目

### GPU 挖矿（显卡）

| 币种 | 算法 | 交易所 | 矿池 |
|------|------|--------|------|
| **ETC** 以太坊经典 | Etchash | Binance, OKX, Coinbase | F2Pool, AntPool |
| **RVN** 乌鸦币 | KawPow | Binance, OKX, KuCoin | F2Pool, 2Miners |
| **KAS** Kaspa | kHeavyHash | Binance, OKX, KuCoin | F2Pool, Hashpool |
| **ERG** Ergo | Autolykos v2 | Binance, KuCoin, Gate.io | F2Pool, Herominers |

### CPU 挖矿（处理器）

| 币种 | 算法 | 交易所 | 矿池 |
|------|------|--------|------|
| **XMR** 门罗币 | RandomX | Binance, Kraken | F2Pool, SupportXMR |

### ASIC 挖矿（专业矿机）

| 币种 | 算法 | 推荐矿机 |
|------|------|---------|
| **BTC** 比特币 | SHA-256 | 蚂蚁S21、神马M60 |
| **LTC** 莱特币 | Scrypt | 蚂蚁L7、金贝KD6 |
| **DOGE** 狗狗币 | Scrypt | 与LTC合并挖矿 |

---

## 项目结构

```
supminer-hardware-checker/
├── src/supminer_hardware_checker/
│   ├── __init__.py      # 包元数据
│   ├── __main__.py      # python -m 入口
│   ├── detector.py      # 硬件检测核心逻辑
│   └── data.py          # 挖矿项目数据
├── pyproject.toml       # 构建配置
├── Makefile             # 常用命令
└── ...
```

---

## 项目标准

本工具只推荐符合以下条件的币种：

1. **已上线主流交易所** — Binance、OKX、Coinbase 等
2. **大型矿池支持** — F2Pool、AntPool 等
3. **市值排名靠前** — 流动性充足
4. **长期稳定运营** — 项目成熟、社区活跃

---

## 免责声明

挖矿收益受电费、硬件性能、币价波动和网络难度影响。加密货币投资有风险，请充分评估后决策。请遵守当地法律法规。

---

## 许可证

MIT License — 详见 [LICENSE](LICENSE)

---

**Davey Wong** <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)
