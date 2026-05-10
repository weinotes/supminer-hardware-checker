# SupMiner 硬件检测工具 - v3.0

🔍 自动检测硬件配置，推荐 **主流的、上交易所的、大型矿池支持** 的挖矿项目

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/badge/pypi-v3.0.0-blue)](https://pypi.org/project/supminer-hardware-checker/)

---

## 🚀 快速开始（3步）

### 第 1 步：下载

```bash
# Git 方式
git clone https://github.com/weinotes/supminer-hardware-checker.git
cd supminer-hardware-checker

# 或下载 ZIP：https://github.com/weinotes/supminer-hardware-checker/archive/refs/heads/main.zip
```

### 第 2 步：安装依赖

```bash
# 标准安装（推荐）
pip install -e .

# 含美化输出（可选）
pip install -e .[rich]

# 或直接 pip install psutil
```

### 第 3 步：运行

```bash
# 方法一：模块运行
python -m supminer_hardware_checker

# 方法二：命令行（安装后可用）
supminer-check

# 方法三：使用 Make
make run
```

---

## 📊 检测内容

| 类别 | 检测项 | 说明 |
|------|--------|------|
| 💻 **操作系统** | 系统类型、版本、架构 | Windows / macOS / Linux |
| 🧠 **CPU** | 型号、核心数、频率、使用率 | 物理核心+逻辑核心 |
| 💾 **内存** | 总容量、可用容量 | 以 GB 显示 |
| 🎮 **GPU** | 厂商、型号、显存、驱动 | NVIDIA (nvidia-smi) / AMD (lspci) |

## 🪙 推荐项目

### GPU 挖矿

| 币种 | 算法 | 交易所 | 矿池 |
|------|------|--------|------|
| **ETC** 以太坊经典 | Etchash | Binance, OKX, Coinbase | F2Pool, AntPool |
| **RVN** 乌鸦币 | KawPow | Binance, OKX, KuCoin | F2Pool, 2Miners |
| **KAS** Kaspa | kHeavyHash | Binance, OKX, KuCoin | F2Pool, Hashpool |
| **ERG** Ergo | Autolykos v2 | Binance, KuCoin, Gate.io | F2Pool, Herominers |

### CPU 挖矿

| 币种 | 算法 | 交易所 | 矿池 |
|------|------|--------|------|
| **XMR** 门罗币 | RandomX | Binance, Kraken | F2Pool, SupportXMR |

### ASIC 挖矿（专业矿机）

| 币种 | 算法 | 推荐矿机 |
|------|------|---------|
| **BTC** 比特币 | SHA-256 | 蚂蚁S21, 神马M60 |
| **LTC** 莱特币 | Scrypt | 蚂蚁L7, 金贝KD6 |
| **DOGE** 狗狗币 | Scrypt | 与LTC合并挖矿 |

---

## 📦 项目结构

```
supminer-hardware-checker/
├── src/
│   └── supminer_hardware_checker/
│       ├── __init__.py    # 包元数据
│       ├── __main__.py    # python -m 入口
│       ├── detector.py    # 硬件检测核心逻辑
│       └── data.py        # 挖矿项目数据库
├── pyproject.toml          # 项目元数据 & 构建配置
├── Makefile                # 常用命令
├── README.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE                 # MIT
└── requirements.txt
```

---

## 🔧 开发

```bash
# 安装开发模式
pip install -e .[rich]

# 测试导入
make test

# 语法检查
make lint

# 清理
make clean
```

---

## ✅ 关于项目标准

本工具只推荐：

1. **已上线主流交易所** — Binance、OKX、Coinbase 等
2. **大型矿池支持** — F2Pool、AntPool、币安矿池等
3. **市值排名靠前** — 流动性充足，容易变现
4. **长期稳定运营** — 项目成熟，社区活跃

我们不推荐小众/山寨币、未上主流交易所或流动性差的项目。

---

## 📞 专业服务

| 服务 | 价格 | 说明 |
|------|------|------|
| 🔧 远程挖矿部署 | ¥800起 | 单台设备，包7天支持 |
| 💡 技术咨询 | ¥300/小时 | 一对一在线咨询 |
| 🏢 托管服务 | ¥300/台/月 | 日常监控维护 |

- 🌐 **官网**: https://supminer.net
- 📧 **邮箱**: support@supminer.net
- 💬 **Telegram**: @supminer

---

## ⚠️ 免责声明

挖矿收益受市场、硬件、电费等因素影响。加密货币投资有风险，请充分评估后决策。请遵守当地法律法规。

---

## 📄 许可证

MIT License — 详见 [LICENSE](LICENSE)
