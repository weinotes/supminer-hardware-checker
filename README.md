# SupMiner 硬件检测工具 - 主流版本

🔍 自动检测硬件配置，推荐**主流的、上交易所的、大型矿池支持**的挖矿项目

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

---

## ✨ 特点

- ✅ **主流币种推荐** - 只推荐上线 Binance、OKX、Coinbase 等交易所的币种
- ✅ **大型矿池支持** - 所有推荐项目均被 F2Pool、AntPool、币安矿池等支持
- ✅ **智能硬件检测** - 自动识别 CPU、GPU、内存配置
- ✅ **分类推荐** - 根据硬件类型推荐最适合的挖矿项目
- ✅ **跨平台支持** - Windows、Linux、macOS 全支持
- ✅ **详细报告** - 生成 JSON 格式的完整硬件报告

---

## 🪙 支持的主流项目

### GPU 挖矿（显卡）

| 币种 | 算法 | 市值排名 | 主要矿池 | 交易所 |
|------|------|---------|---------|--------|
| **ETC** 以太坊经典 | Etchash | Top 30 | F2Pool, AntPool, ViaBTC | Binance, OKX, Coinbase |
| **RVN** 乌鸦币 | KawPow | Top 100 | F2Pool, 2Miners | Binance, OKX, KuCoin |
| **KAS** Kaspa | kHeavyHash | Top 50 | F2Pool, Hashpool | Binance, OKX, MEXC |
| **ERG** Ergo | Autolykos v2 | Top 150 | F2Pool, Herominers | Binance, KuCoin, Gate.io |

### CPU 挖矿（处理器）

| 币种 | 算法 | 市值排名 | 主要矿池 | 交易所 |
|------|------|---------|---------|--------|
| **XMR** 门罗币 | RandomX | Top 50 | F2Pool, SupportXMR | Binance, Kraken, Poloniex |

### ASIC 挖矿（专业矿机）

| 币种 | 算法 | 市值排名 | 主要矿池 | 推荐矿机 |
|------|------|---------|---------|---------|
| **BTC** 比特币 | SHA-256 | 第1名 | F2Pool, AntPool, 币安矿池 | 蚂蚁S19, 神马M50 |
| **LTC** 莱特币 | Scrypt | Top 20 | F2Pool, AntPool, ViaBTC | 蚂蚁L7, 金贝KD6 |
| **DOGE** 狗狗币 | Scrypt | Top 10 | F2Pool, AntPool | 与LTC合并挖矿 |

---

## 🚀 快速开始

### 安装依赖

#### Linux / macOS

```bash
# 推荐方式（确保使用正确的Python环境）
python3 -m pip install psutil

# 或使用系统包管理器（Ubuntu/Debian）
sudo apt install python3-psutil

# 或使用用户目录安装
pip3 install --user psutil
```

#### Windows

```powershell
pip install psutil
```

### 运行检测

```bash
# Linux / macOS
python3 hardware_checker_v2.py

# Windows
python hardware_checker_v2.py
```

---

## 📊 输出示例

```
╔══════════════════════════════════════════════════════════════╗
║          SupMiner 硬件检测工具 - 主流项目版本                ║
║          推荐的都是上交易所的主流币种                         ║
║          支持蚂蚁矿池、F2Pool、币安矿池等                     ║
╚══════════════════════════════════════════════════════════════╝

======================================================================
SupMiner 硬件检测报告 - 主流挖矿项目版本
======================================================================

【操作系统】
  系统: Linux 5.15.0
  架构: x86_64

【处理器 CPU】
  型号: AMD Ryzen 9 5900X
  物理核心: 12
  逻辑核心: 24
  最大频率: 3700.00 MHz

【显卡 GPU】
  显卡 1:
    厂商: NVIDIA
    型号: NVIDIA GeForce RTX 3080
    显存: 10240 MiB
    驱动: 525.85.05

======================================================================
【推荐的主流挖矿项目】
======================================================================

GPU Mining (显卡挖矿) - 优先级: ⭐⭐⭐⭐⭐
----------------------------------------------------------------------

  🪙 ETC (Ethereum Classic 以太坊经典)
     算法: Etchash
     简介: 市值40亿美元，最主流的GPU挖矿币种
     矿池: F2Pool, AntPool, ViaBTC, 币安矿池
     交易所: Binance, OKX, Coinbase, Huobi
     硬件: 推荐: NVIDIA RTX 3060/3070/3080 或 AMD RX 5700/6700

  🪙 RVN (Ravencoin 乌鸦币)
     算法: KawPow
     简介: 抗ASIC设计，GPU友好，专注数字资产
     矿池: F2Pool, 2Miners, Ravenminer
     交易所: Binance, OKX, KuCoin
     硬件: 推荐: 中高端显卡，内存>4GB

...

⚠️ 重要提示 - 优先级: 必读
----------------------------------------------------------------------
  ⚠️  所有推荐币种均已上线主流交易所（Binance、OKX、Coinbase等）
  ⚠️  所有项目均被F2Pool、AntPool等大型矿池支持
  ⚠️  挖矿收益取决于：电费成本、设备性能、币价波动、网络难度
  ⚠️  理性投资，谨防诈骗
```

---

## 📋 生成的报告文件

运行后会生成 `hardware_report.json`，包含：
- 完整的硬件信息
- 详细的项目推荐
- 矿池和交易所列表
- 硬件配置建议

---

## 🔧 故障排除

### 问题 1: `psutil` 模块未找到

**macOS 解决方法:**
```bash
# 方法1: 使用python3 -m pip
python3 -m pip install psutil

# 方法2: 检查Python路径
which python3
/usr/bin/python3 -m pip install --user psutil

# 方法3: 验证安装
python3 -c "import psutil; print(psutil.__version__)"
```

**Ubuntu 22.04+ 解决方法:**
```bash
# 方法1: 使用系统包管理器（推荐）
sudo apt install python3-psutil

# 方法2: 用户目录安装
pip3 install --user psutil

# 方法3: 虚拟环境
python3 -m venv venv
source venv/bin/activate
pip install psutil
```

### 问题 2: GPU 检测不到

**解决方法:**
- NVIDIA 显卡：安装 [NVIDIA 驱动](https://www.nvidia.com/Download/index.aspx)
- AMD 显卡：确保系统识别显卡（Linux: `lspci | grep VGA`）

### 问题 3: 权限问题

```bash
# 给脚本添加执行权限
chmod +x hardware_checker_v2.py

# 使用 sudo（如果需要）
sudo python3 hardware_checker_v2.py
```

---

## 🌐 关于主流项目的说明

### 为什么只推荐这些项目？

1. **交易所上线** - 所有推荐币种都在 Binance、OKX、Coinbase 等主流交易所交易
2. **矿池支持** - 被 F2Pool、AntPool、币安矿池等大型矿池支持
3. **流动性保障** - 市值排名靠前，交易量大，容易变现
4. **长期稳定** - 项目运行多年，社区活跃，不是短期炒作

### 不推荐小众项目的原因

❌ **流动性差** - 难以在交易所卖出  
❌ **矿池少** - 挖矿不稳定，收益波动大  
❌ **风险高** - 项目可能跑路或归零  
❌ **不适合新手** - 需要专业知识判断

---

## 💼 专业服务

需要专业的挖矿部署服务？

- 🌐 **官网**: https://supminer.net
- 📧 **邮箱**: support@supminer.net
- 💬 **Telegram**: @supminer

### 服务价格

- 🔧 远程挖矿部署: ¥800起
- 💡 技术咨询: ¥300/小时
- 🏢 托管服务: ¥300/台/月起
- 📚 技术培训: ¥500/课时

---

## 📜 免责声明

- ⚠️ 本工具仅用于硬件检测和信息展示
- ⚠️ 挖矿收益因市场、硬件、电费等因素波动
- ⚠️ 投资有风险，建议充分评估后决策
- ⚠️ 遵守当地法律法规进行挖矿活动

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📞 联系我们

- **网站**: https://supminer.net
- **邮箱**: support@supminer.net
- **GitHub**: https://github.com/weinotes/supminer-hardware-checker

---

**理性投资，谨防诈骗！** 💎

---

## 更新日志

### v2.0 - 2024-12-07
- ✅ 更新为主流挖矿项目推荐
- ✅ 只推荐上线主流交易所的币种
- ✅ 只推荐主流矿池支持的项目
- ✅ 移除小众项目（Qubic, Nexa, Nexus, Ore, Gauntlet）
- ✅ 新增主流项目（BTC, LTC, DOGE, ETC, RVN, KAS, ERG, XMR）
- ✅ 添加详细的矿池和交易所信息

### v1.0 - 2024-12-06
- 初始版本
