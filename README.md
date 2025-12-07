# SupMiner Hardware Checker

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

**智能硬件检测工具 - 为您推荐最适合的挖矿方案**

[English](#english) | [中文](#中文)

</div>

---

## 中文

### 📋 项目简介

SupMiner Hardware Checker 是一款专业的硬件检测工具，专为 [supminer.net](https://supminer.net) 用户设计。它能够：

- 🔍 **智能检测** CPU、GPU、内存等硬件信息
- 💡 **专业建议** 根据硬件配置推荐适合的挖矿项目
- 📊 **详细报告** 生成完整的硬件检测报告（JSON格式）
- 🖥️ **跨平台** 支持 Windows、Linux、macOS

### ✨ 功能特点

#### 硬件检测
- ✅ CPU型号、核心数、频率
- ✅ NVIDIA/AMD GPU检测
- ✅ 显存容量和驱动版本
- ✅ 系统内存信息
- ✅ 操作系统详情

#### 智能推荐
- 🎯 GPU挖矿项目推荐（Qubic、Nexa、Nexus等）
- 🎯 CPU挖矿项目推荐（Ore、Gauntlet等）
- ⚠️ 硬件不足警告
- 📈 性能优化建议

### 🚀 快速开始

#### 方法一：直接运行（推荐）

```bash
# 1. 下载脚本
curl -O https://raw.githubusercontent.com/weinotes/supminer-hardware-checker/main/hardware_checker.py

# 2. 运行检测（基础功能）
python3 hardware_checker.py

# 3. 安装完整依赖（可选，获取更详细信息）
pip install psutil
python3 hardware_checker.py
```

#### 方法二：克隆仓库

```bash
# 1. 克隆项目
git clone https://github.com/weinotes/supminer-hardware-checker.git
cd supminer-hardware-checker

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行检测
python hardware_checker.py
```

### 📦 依赖要求

- Python 3.6+
- psutil (可选，用于获取详细硬件信息)

#### 安装 psutil

**macOS / Windows:**
```bash
pip install psutil
# 或
pip3 install psutil
```

**Ubuntu/Debian 22.04+ (推荐方法):**
```bash
# 方法 1: 使用系统包管理器（最简单）
sudo apt update
sudo apt install python3-psutil

# 方法 2: 安装到用户目录
pip3 install --user psutil

# 方法 3: 使用虚拟环境
python3 -m venv venv
source venv/bin/activate
pip install psutil
```

**其他 Linux 发行版:**
```bash
pip3 install psutil
# 如果遇到 externally-managed-environment 错误，使用:
pip3 install --user psutil
```

### 💻 使用示例

#### Windows用户

```powershell
# 使用PowerShell或CMD
python hardware_checker.py
```

#### Linux/Mac用户

```bash
# 使用终端
python3 hardware_checker.py
```

#### 输出示例

```
============================================================
SupMiner.net 硬件检测报告
============================================================

检测时间: 2024-12-07 15:30:00

【系统信息】
操作系统: Linux
系统版本: #1 SMP PREEMPT_DYNAMIC
架构: x86_64

【CPU信息】
型号: AMD Ryzen 9 5900X 12-Core Processor
物理核心: 12
逻辑核心: 24
最大频率: 4950.00 MHz

【GPU信息】
GPU 1:
  类型: NVIDIA
  型号: NVIDIA GeForce RTX 3080
  显存: 10240 MiB
  驱动: 535.129.03

【内存信息】
总内存: 32.00 GB
可用内存: 24.50 GB
使用率: 23.4%

============================================================
【挖矿建议】
============================================================

推荐类型: GPU挖矿（优先推荐）

原因分析:
  ✅ 检测到NVIDIA显卡，适合GPU挖矿
  ✅ CPU拥有12个物理核心，可同时进行CPU挖矿
  ✅ 系统内存充足 (32.00 GB)

适合的项目:
  • Qubic (GPU) - 推荐
  • Nexa (GPU)
  • Nexus (GPU)
  • Gauntlet (GPU)
  • Qubic (CPU)
  • Ore
  • Nexus (CPU)
  • Gauntlet (CPU)

============================================================
访问 https://supminer.net 获取详细安装教程
联系我们获取专业的挖矿咨询服务
============================================================
```

### 📊 支持的挖矿项目

#### GPU挖矿项目
- **Qubic (GPU)** - NVIDIA GPU优化，高效能
- **Nexa** - 支持NVIDIA显卡
- **Nexus (GPU)** - GPU加速版本
- **Gauntlet (GPU)** - 图形计算优化

#### CPU挖矿项目
- **Qubic (CPU)** - 多核心CPU优化
- **Ore** - 轻量级CPU挖矿
- **Nexus (CPU)** - CPU友好型
- **Gauntlet (CPU)** - 通用CPU版本

### 🔧 高级用法

#### 生成JSON报告

脚本会自动生成 `hardware_report.json` 文件，包含完整的硬件信息：

```json
{
  "timestamp": "2024-12-07 15:30:00",
  "system": {...},
  "cpu": {...},
  "gpu": [...],
  "memory": {...},
  "recommendation": {...}
}
```

#### 自定义检测

您可以修改脚本以适应特定需求：

```python
checker = HardwareChecker()
checker.get_cpu_info()
checker.get_gpu_info()
# 自定义分析逻辑
```

### 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 📝 更新日志

#### v1.0.0 (2024-12-07)
- 🎉 首次发布
- ✅ 支持CPU/GPU/内存检测
- ✅ 智能推荐挖矿项目
- ✅ 跨平台支持
- ✅ JSON报告导出

### 📞 联系我们

- 🌐 官网: [supminer.net](https://supminer.net)
- 📧 邮箱: support@supminer.net
- 💬 Telegram: [加入我们的社群]

### 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

### ⚠️ 免责声明

本工具仅用于硬件检测和项目推荐，不包含任何挖矿程序。实际挖矿收益取决于多种因素，请理性投资。

---

## English

### 📋 Project Overview

SupMiner Hardware Checker is a professional hardware detection tool designed for [supminer.net](https://supminer.net) users. It can:

- 🔍 **Smart Detection** - CPU, GPU, memory and other hardware information
- 💡 **Professional Advice** - Recommend suitable mining projects based on hardware configuration
- 📊 **Detailed Reports** - Generate complete hardware detection reports (JSON format)
- 🖥️ **Cross-platform** - Support Windows, Linux, macOS

### 🚀 Quick Start

```bash
# Download and run
curl -O https://raw.githubusercontent.com/weinotes/supminer-hardware-checker/main/hardware_checker.py
python3 hardware_checker.py

# For detailed information, install dependencies
pip install psutil
```

### 💻 Usage

```bash
python hardware_checker.py
```

### 📊 Supported Mining Projects

**GPU Mining:**
- Qubic (GPU), Nexa, Nexus (GPU), Gauntlet (GPU)

**CPU Mining:**
- Qubic (CPU), Ore, Nexus (CPU), Gauntlet (CPU)

### 📞 Contact

- 🌐 Website: [supminer.net](https://supminer.net)
- 📧 Email: support@supminer.net

### 📄 License

MIT License - See [LICENSE](LICENSE) file

---

<div align="center">

**Made with ❤️ by SupMiner Team**

⭐ 如果这个项目对你有帮助，请给我们一个 Star！

</div>
