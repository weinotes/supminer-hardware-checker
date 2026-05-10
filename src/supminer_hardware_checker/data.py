"""
Mining project data — update this file to refresh coin/pool/exchange info.

Author: Davey Wong <wgwcko@gmail.com> (https://www.guangweiblog.com)
Licensed under MIT.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class MiningProject:
    """A single mineable cryptocurrency project."""
    name: str
    algorithm: str
    description: str
    pools: List[str]
    exchanges: List[str]
    hardware: str


@dataclass
class MiningCategory:
    """A category of mining projects (GPU / CPU / ASIC)."""
    category: str
    priority: str
    projects: List[MiningProject] = field(default_factory=list)
    note: str = ""


# ---------------------------------------------------------------------------
# GPU Mining
# ---------------------------------------------------------------------------
gpu_projects = [
    MiningProject(
        name="ETC (Ethereum Classic 以太坊经典)",
        algorithm="Etchash",
        description="市值40亿美元，最主流的GPU挖矿币种，2025年生态持续发展",
        pools=["F2Pool", "AntPool", "ViaBTC", "币安矿池"],
        exchanges=["Binance", "OKX", "Coinbase", "Huobi", "Kraken"],
        hardware="推荐: NVIDIA RTX 3060/3070/3080/4060 或 AMD RX 5700/6700/7700",
    ),
    MiningProject(
        name="RVN (Ravencoin 乌鸦币)",
        algorithm="KawPow",
        description="抗ASIC设计，GPU友好，专注数字资产发行",
        pools=["F2Pool", "2Miners", "Ravenminer"],
        exchanges=["Binance", "OKX", "KuCoin", "MEXC"],
        hardware="推荐: 中高端显卡，显存>4GB",
    ),
    MiningProject(
        name="KAS (Kaspa)",
        algorithm="kHeavyHash",
        description="2024-2025年快速增长项目，高TPS DAG区块链",
        pools=["F2Pool", "Hashpool", "Woolypooly"],
        exchanges=["Binance", "OKX", "KuCoin", "MEXC", "Gate.io"],
        hardware="推荐: 现代GPU，支持高算力，NVIDIA 30/40系列表现优异",
    ),
    MiningProject(
        name="ERG (Ergo)",
        algorithm="Autolykos v2",
        description="学术背景深厚，能效比优秀，持续开发中",
        pools=["F2Pool", "Herominers", "2Miners"],
        exchanges=["Binance", "KuCoin", "Gate.io"],
        hardware="推荐: 中端GPU即可，显存>4GB",
    ),
]

# ---------------------------------------------------------------------------
# CPU Mining
# ---------------------------------------------------------------------------
cpu_projects = [
    MiningProject(
        name="XMR (Monero 门罗币)",
        algorithm="RandomX",
        description="最主流的CPU挖矿币，隐私币龙头，2025年社区活跃",
        pools=["F2Pool", "SupportXMR", "MoneroOcean"],
        exchanges=["Binance", "Kraken", "Poloniex", "KuCoin"],
        hardware="推荐: AMD Ryzen 9/Threadripper 或 Intel Core i9 (多核心优势明显)",
    ),
]

# ---------------------------------------------------------------------------
# ASIC Mining
# ---------------------------------------------------------------------------
asic_projects = [
    MiningProject(
        name="BTC (Bitcoin 比特币)",
        algorithm="SHA-256",
        description="全球市值第一，最成熟的挖矿生态，2025年减半后手续费收入占比提升",
        pools=["F2Pool", "AntPool", "币安矿池", "Foundry USA", "ViaBTC"],
        exchanges=["所有主流交易所"],
        hardware="需要ASIC矿机: 蚂蚁S21系列、神马M60系列、Whatsminer M50",
    ),
    MiningProject(
        name="LTC (Litecoin 莱特币)",
        algorithm="Scrypt",
        description="比特金莱特银，可与DOGE合并挖矿，Scrypt生态核心",
        pools=["F2Pool", "AntPool", "ViaBTC", "Poolin"],
        exchanges=["Binance", "Coinbase", "OKX", "Huobi", "Kraken"],
        hardware="需要Scrypt ASIC: 蚂蚁L7、金贝KD6、Elphapex DG1",
    ),
    MiningProject(
        name="DOGE (Dogecoin 狗狗币)",
        algorithm="Scrypt",
        description="马斯克支持，社区强大，与LTC合并挖矿",
        pools=["F2Pool", "AntPool", "Prohashing", "ViaBTC"],
        exchanges=["Binance", "Coinbase", "OKX", "Robinhood", "Kraken"],
        hardware="使用LTC矿机即可同时挖DOGE (合并挖矿)",
    ),
]

gpu_category = MiningCategory(
    category="GPU Mining (显卡挖矿)",
    priority="⭐⭐⭐⭐⭐",
    projects=gpu_projects,
)

cpu_category = MiningCategory(
    category="CPU Mining (处理器挖矿)",
    priority="⭐⭐⭐",
    projects=cpu_projects,
)

asic_category = MiningCategory(
    category="ASIC Mining (专业矿机挖矿)",
    priority="⭐⭐⭐⭐⭐",
    note="需要购买专业ASIC矿机，收益最高但投资较大",
    projects=asic_projects,
)

WARNINGS = [
    "所有推荐币种均已上线主流交易所（Binance、OKX、Coinbase等）",
    "所有项目均被F2Pool、AntPool等大型矿池支持",
    "挖矿收益取决于：电费成本、设备性能、币价波动、网络难度",
    "投资有风险，建议先用挖矿收益计算器评估ROI",
    "CPU挖矿收益较低，主要用于学习，不建议大规模投入",
    "GPU挖矿需要考虑显卡折旧和电费成本",
    "ASIC挖矿需要大量初始投资，适合专业矿场",
    "理性投资，谨防诈骗",
]
