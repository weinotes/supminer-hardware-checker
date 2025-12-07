#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SupMiner 硬件检测工具 - 主流版本
自动检测硬件配置并推荐主流挖矿项目
支持的主流项目：BTC, LTC, DOGE, ETC, RVN, KAS, ERG, XMR
"""

import platform
import json
import subprocess
import sys
from datetime import datetime

try:
    import psutil
except ImportError:
    print("错误: 缺少 psutil 库")
    print("\n请先安装依赖:")
    print("  pip install psutil")
    print("或:")
    print("  pip3 install psutil")
    sys.exit(1)

class HardwareDetector:
    def __init__(self):
        self.system_info = {
            "detection_time": datetime.now().isoformat(),
            "os": {},
            "cpu": {},
            "memory": {},
            "gpu": [],
            "recommended_projects": []
        }
    
    def detect_os(self):
        """检测操作系统信息"""
        self.system_info["os"] = {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }
    
    def detect_cpu(self):
        """检测CPU信息"""
        self.system_info["cpu"] = {
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
            "max_frequency": psutil.cpu_freq().max if psutil.cpu_freq() else 0,
            "current_frequency": psutil.cpu_freq().current if psutil.cpu_freq() else 0,
            "cpu_usage": psutil.cpu_percent(interval=1),
            "model": platform.processor()
        }
    
    def detect_memory(self):
        """检测内存信息"""
        memory = psutil.virtual_memory()
        self.system_info["memory"] = {
            "total_gb": round(memory.total / (1024**3), 2),
            "available_gb": round(memory.available / (1024**3), 2),
            "used_gb": round(memory.used / (1024**3), 2),
            "percent": memory.percent
        }
    
    def detect_gpu_nvidia(self):
        """检测NVIDIA显卡"""
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=name,memory.total,driver_version', '--format=csv,noheader'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n'):
                    if line:
                        parts = [p.strip() for p in line.split(',')]
                        if len(parts) >= 3:
                            self.system_info["gpu"].append({
                                "vendor": "NVIDIA",
                                "model": parts[0],
                                "memory": parts[1],
                                "driver": parts[2]
                            })
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
    
    def detect_gpu_amd(self):
        """检测AMD显卡"""
        try:
            if platform.system() == "Linux":
                result = subprocess.run(
                    ['lspci'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                if result.returncode == 0:
                    for line in result.stdout.split('\n'):
                        if 'VGA' in line or 'Display' in line:
                            if 'AMD' in line or 'ATI' in line or 'Radeon' in line:
                                self.system_info["gpu"].append({
                                    "vendor": "AMD",
                                    "model": line.split(':')[-1].strip(),
                                    "memory": "Unknown",
                                    "driver": "Unknown"
                                })
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
    
    def detect_gpu(self):
        """检测GPU信息"""
        self.detect_gpu_nvidia()
        self.detect_gpu_amd()
        
        if not self.system_info["gpu"]:
            self.system_info["gpu"].append({
                "vendor": "Unknown",
                "model": "No dedicated GPU detected",
                "memory": "N/A",
                "driver": "N/A"
            })
    
    def recommend_projects(self):
        """
        根据硬件配置推荐主流挖矿项目
        
        主流项目分类:
        - ASIC专用: BTC, LTC, DOGE, BCH (需要专业矿机)
        - GPU挖矿: ETC, RVN, KAS, ERG (显卡挖矿)
        - CPU挖矿: XMR (处理器挖矿)
        """
        recommendations = []
        
        # GPU 推荐
        has_gpu = any(gpu["vendor"] in ["NVIDIA", "AMD"] for gpu in self.system_info["gpu"])
        
        if has_gpu:
            recommendations.append({
                "category": "GPU Mining (显卡挖矿)",
                "priority": "⭐⭐⭐⭐⭐",
                "projects": [
                    {
                        "name": "ETC (Ethereum Classic 以太坊经典)",
                        "algorithm": "Etchash",
                        "description": "市值40亿美元，最主流的GPU挖矿币种",
                        "pools": ["F2Pool", "AntPool", "ViaBTC", "币安矿池"],
                        "exchanges": ["Binance", "OKX", "Coinbase", "Huobi"],
                        "hardware": "推荐: NVIDIA RTX 3060/3070/3080 或 AMD RX 5700/6700"
                    },
                    {
                        "name": "RVN (Ravencoin 乌鸦币)",
                        "algorithm": "KawPow",
                        "description": "抗ASIC设计，GPU友好，专注数字资产",
                        "pools": ["F2Pool", "2Miners", "Ravenminer"],
                        "exchanges": ["Binance", "OKX", "KuCoin"],
                        "hardware": "推荐: 中高端显卡，内存>4GB"
                    },
                    {
                        "name": "KAS (Kaspa)",
                        "algorithm": "kHeavyHash",
                        "description": "2025年快速增长项目，高TPS区块链",
                        "pools": ["F2Pool", "Hashpool", "Woolypooly"],
                        "exchanges": ["Binance", "OKX", "KuCoin", "MEXC"],
                        "hardware": "推荐: 现代GPU，支持高算力"
                    },
                    {
                        "name": "ERG (Ergo)",
                        "algorithm": "Autolykos v2",
                        "description": "学术背景深厚，能效比优秀",
                        "pools": ["F2Pool", "Herominers", "2Miners"],
                        "exchanges": ["Binance", "KuCoin", "Gate.io"],
                        "hardware": "推荐: 中端GPU即可，内存>4GB"
                    }
                ]
            })
        
        # CPU 推荐
        cpu_cores = self.system_info["cpu"]["physical_cores"]
        if cpu_cores and cpu_cores >= 4:
            recommendations.append({
                "category": "CPU Mining (处理器挖矿)",
                "priority": "⭐⭐⭐",
                "projects": [
                    {
                        "name": "XMR (Monero 门罗币)",
                        "algorithm": "RandomX",
                        "description": "最主流的CPU挖矿币，隐私币龙头",
                        "pools": ["F2Pool", "SupportXMR", "MoneroOcean"],
                        "exchanges": ["Binance", "Kraken", "Poloniex"],
                        "hardware": f"当前CPU: {cpu_cores}核心，推荐: AMD Ryzen 9/Threadripper"
                    }
                ]
            })
        
        # ASIC 矿机提示（如果没有高端GPU）
        if not has_gpu or self.system_info["gpu"][0]["vendor"] == "Unknown":
            recommendations.append({
                "category": "ASIC Mining (专业矿机挖矿)",
                "priority": "⭐⭐⭐⭐⭐",
                "note": "需要购买专业ASIC矿机，收益最高但投资较大",
                "projects": [
                    {
                        "name": "BTC (Bitcoin 比特币)",
                        "algorithm": "SHA-256",
                        "description": "全球市值第一，最成熟的挖矿生态",
                        "pools": ["F2Pool", "AntPool", "币安矿池", "Foundry USA", "ViaBTC"],
                        "exchanges": ["所有主流交易所"],
                        "hardware": "需要ASIC矿机: 蚂蚁S19系列、神马M50系列"
                    },
                    {
                        "name": "LTC (Litecoin 莱特币)",
                        "algorithm": "Scrypt",
                        "description": "比特金莱特银，可与DOGE合并挖矿",
                        "pools": ["F2Pool", "AntPool", "ViaBTC", "Poolin"],
                        "exchanges": ["Binance", "Coinbase", "OKX", "Huobi"],
                        "hardware": "需要Scrypt ASIC: 蚂蚁L7、金贝KD6"
                    },
                    {
                        "name": "DOGE (Dogecoin 狗狗币)",
                        "algorithm": "Scrypt",
                        "description": "马斯克支持，与LTC合并挖矿",
                        "pools": ["F2Pool", "AntPool", "Prohashing"],
                        "exchanges": ["Binance", "Coinbase", "OKX", "Robinhood"],
                        "hardware": "使用LTC矿机即可同时挖DOGE"
                    }
                ]
            })
        
        # 添加重要提示
        recommendations.append({
            "category": "⚠️ 重要提示",
            "priority": "必读",
            "warnings": [
                "所有推荐币种均已上线主流交易所（Binance、OKX、Coinbase等）",
                "所有项目均被F2Pool、AntPool等大型矿池支持",
                "挖矿收益取决于：电费成本、设备性能、币价波动、网络难度",
                "投资有风险，建议先用挖矿收益计算器评估ROI",
                "CPU挖矿收益较低，主要用于学习，不建议大规模投入",
                "GPU挖矿需要考虑显卡折旧和电费成本",
                "ASIC挖矿需要大量初始投资，适合专业矿场",
                "理性投资，谨防诈骗"
            ]
        })
        
        self.system_info["recommended_projects"] = recommendations
    
    def generate_report(self):
        """生成检测报告"""
        print("\n" + "="*70)
        print("SupMiner 硬件检测报告 - 主流挖矿项目版本")
        print("="*70)
        
        # 操作系统
        print(f"\n【操作系统】")
        print(f"  系统: {self.system_info['os']['system']} {self.system_info['os']['release']}")
        print(f"  架构: {self.system_info['os']['machine']}")
        
        # CPU
        print(f"\n【处理器 CPU】")
        print(f"  型号: {self.system_info['cpu']['model']}")
        print(f"  物理核心: {self.system_info['cpu']['physical_cores']}")
        print(f"  逻辑核心: {self.system_info['cpu']['logical_cores']}")
        if self.system_info['cpu']['max_frequency']:
            print(f"  最大频率: {self.system_info['cpu']['max_frequency']:.2f} MHz")
        
        # 内存
        print(f"\n【内存 RAM】")
        print(f"  总容量: {self.system_info['memory']['total_gb']} GB")
        print(f"  已使用: {self.system_info['memory']['used_gb']} GB ({self.system_info['memory']['percent']}%)")
        print(f"  可用: {self.system_info['memory']['available_gb']} GB")
        
        # GPU
        print(f"\n【显卡 GPU】")
        for i, gpu in enumerate(self.system_info['gpu'], 1):
            print(f"  显卡 {i}:")
            print(f"    厂商: {gpu['vendor']}")
            print(f"    型号: {gpu['model']}")
            print(f"    显存: {gpu['memory']}")
            if gpu['driver'] != "N/A":
                print(f"    驱动: {gpu['driver']}")
        
        # 推荐项目
        print(f"\n{'='*70}")
        print("【推荐的主流挖矿项目】")
        print(f"{'='*70}")
        
        for rec in self.system_info['recommended_projects']:
            if "warnings" in rec:
                # 警告信息
                print(f"\n{rec['category']}")
                print("-" * 70)
                for warning in rec['warnings']:
                    print(f"  ⚠️  {warning}")
            else:
                # 项目推荐
                print(f"\n{rec['category']} - 优先级: {rec['priority']}")
                if "note" in rec:
                    print(f"  💡 {rec['note']}")
                print("-" * 70)
                
                for project in rec['projects']:
                    print(f"\n  🪙 {project['name']}")
                    print(f"     算法: {project['algorithm']}")
                    print(f"     简介: {project['description']}")
                    print(f"     矿池: {', '.join(project['pools'])}")
                    print(f"     交易所: {', '.join(project['exchanges'])}")
                    print(f"     硬件: {project['hardware']}")
        
        print(f"\n{'='*70}")
        print("详细的JSON报告已保存到: hardware_report.json")
        print(f"{'='*70}\n")
    
    def save_json_report(self, filename="hardware_report.json"):
        """保存JSON格式报告"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.system_info, f, indent=2, ensure_ascii=False)
    
    def run(self):
        """运行完整检测流程"""
        print("正在检测硬件配置...")
        self.detect_os()
        self.detect_cpu()
        self.detect_memory()
        self.detect_gpu()
        
        print("正在分析并推荐主流挖矿项目...")
        self.recommend_projects()
        
        self.generate_report()
        self.save_json_report()

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          SupMiner 硬件检测工具 - 主流项目版本                ║
║                                                              ║
║          推荐的都是上交易所的主流币种                         ║
║          支持蚂蚁矿池、F2Pool、币安矿池等                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    detector = HardwareDetector()
    detector.run()
    
    print("\n✅ 检测完成！")
    print("📧 如需专业挖矿部署服务，请联系:")
    print("   - 网站: https://supminer.net")
    print("   - 邮箱: support@supminer.net")
    print("   - Telegram: @supminer")
    print("\n💡 提示: 所有推荐项目均为主流币种，流动性有保障")
    print("⚠️  理性投资，谨防诈骗！\n")

if __name__ == "__main__":
    main()
