#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SupMiner Hardware Checker — detector module.

Detects OS, CPU, memory, and GPU, then recommends mainstream
mineable cryptocurrency projects based on detected hardware.

Author: Davey Wong <wgwcko@gmail.com> (https://www.guangweiblog.com)
Licensed under MIT.
"""

from __future__ import annotations

import json
import platform
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import psutil
except ImportError:
    print("错误: 缺少 psutil 库")
    print("\n请先安装依赖:")
    print("  pip install psutil")
    print("或:")
    print("  pip3 install psutil")
    sys.exit(1)

from supminer_hardware_checker.data import (
    WARNINGS,
    MiningCategory,
    asic_category,
    cpu_category,
    gpu_category,
)

# ---------------------------------------------------------------------------
# Rich output (optional)
# ---------------------------------------------------------------------------
try:
    from rich.console import Console
    from rich.panel import Panel

    RICH_AVAILABLE = True
    console = Console()
except ImportError:
    RICH_AVAILABLE = False


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

class SystemInfo:
    """Aggregated hardware and recommendation data."""

    def __init__(self) -> None:
        self.detection_time: str = datetime.now().isoformat()
        self.os: Dict[str, str] = {}
        self.cpu: Dict[str, Any] = {}
        self.memory: Dict[str, Any] = {}
        self.gpu: List[Dict[str, str]] = []
        self.recommended_projects: List[Dict[str, Any]] = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "detection_time": self.detection_time,
            "os": self.os,
            "cpu": self.cpu,
            "memory": self.memory,
            "gpu": self.gpu,
            "recommended_projects": self.recommended_projects,
        }


# ---------------------------------------------------------------------------
# Detector
# ---------------------------------------------------------------------------

class HardwareDetector:
    """Detect system hardware and recommend mining projects."""

    def __init__(self) -> None:
        self.system_info = SystemInfo()

    # -- OS -----------------------------------------------------------------

    def detect_os(self) -> None:
        self.system_info.os = {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        }

    # -- CPU ----------------------------------------------------------------

    def detect_cpu(self) -> None:
        freq = psutil.cpu_freq()
        self.system_info.cpu = {
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
            "max_frequency_mhz": round(freq.max, 2) if freq else 0.0,
            "current_frequency_mhz": round(freq.current, 2) if freq else 0.0,
            "cpu_usage_percent": psutil.cpu_percent(interval=1),
            "model": platform.processor(),
        }

    # -- Memory -------------------------------------------------------------

    def detect_memory(self) -> None:
        mem = psutil.virtual_memory()
        self.system_info.memory = {
            "total_gb": round(mem.total / (1024**3), 2),
            "available_gb": round(mem.available / (1024**3), 2),
            "used_gb": round(mem.used / (1024**3), 2),
            "percent": mem.percent,
        }

    # -- GPU ----------------------------------------------------------------

    def _run_cmd(self, cmd: List[str], timeout: int = 5) -> Optional[str]:
        """Run a command and return stdout, or None on failure."""
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=timeout
            )
            return result.stdout if result.returncode == 0 else None
        except (FileNotFoundError, subprocess.TimeoutExpired, PermissionError):
            return None

    def _detect_gpu_nvidia(self) -> None:
        stdout = self._run_cmd(
            [
                "nvidia-smi",
                "--query-gpu=name,memory.total,driver_version",
                "--format=csv,noheader",
            ]
        )
        if not stdout:
            return

        for line in stdout.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 3:
                self.system_info.gpu.append(
                    {
                        "vendor": "NVIDIA",
                        "model": parts[0],
                        "memory": parts[1],
                        "driver": parts[2],
                    }
                )

    def _detect_gpu_amd(self) -> None:
        if platform.system() != "Linux":
            return
        stdout = self._run_cmd(["lspci"])
        if not stdout:
            return

        for line in stdout.split("\n"):
            if "VGA" not in line and "Display" not in line:
                continue
            if not any(kw in line for kw in ("AMD", "ATI", "Radeon")):
                continue
            self.system_info.gpu.append(
                {
                    "vendor": "AMD",
                    "model": line.split(":")[-1].strip(),
                    "memory": "Unknown",
                    "driver": "Unknown",
                }
            )

    def detect_gpu(self) -> None:
        self._detect_gpu_nvidia()
        self._detect_gpu_amd()

        if not self.system_info.gpu:
            self.system_info.gpu.append(
                {
                    "vendor": "Unknown",
                    "model": "No dedicated GPU detected",
                    "memory": "N/A",
                    "driver": "N/A",
                }
            )

    # -- Recommendations ----------------------------------------------------

    def _has_dedicated_gpu(self) -> bool:
        return any(
            gpu["vendor"] in ("NVIDIA", "AMD") for gpu in self.system_info.gpu
        )

    def _category_to_dict(self, cat: MiningCategory, extra: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        d: Dict[str, Any] = {
            "category": cat.category,
            "priority": cat.priority,
        }
        if extra:
            d.update(extra)
        if cat.note:
            d["note"] = cat.note
        d["projects"] = [
            {
                "name": p.name,
                "algorithm": p.algorithm,
                "description": p.description,
                "pools": p.pools,
                "exchanges": p.exchanges,
                "hardware": p.hardware,
            }
            for p in cat.projects
        ]
        return d

    def _warnings_to_dict(self) -> Dict[str, Any]:
        return {
            "category": "⚠️ 重要提示",
            "priority": "必读",
            "warnings": WARNINGS,
        }

    def recommend_projects(self) -> None:
        recommendations: List[Dict[str, Any]] = []
        has_gpu = self._has_dedicated_gpu()
        cpu_cores = self.system_info.cpu.get("physical_cores") or 0

        if has_gpu:
            recommendations.append(self._category_to_dict(gpu_category))

        if cpu_cores >= 4:
            recommendations.append(self._category_to_dict(cpu_category))

        # ASIC section: show when no dedicated GPU OR always as reference
        if not has_gpu:
            recommendations.append(self._category_to_dict(asic_category))

        recommendations.append(self._warnings_to_dict())
        self.system_info.recommended_projects = recommendations

    # -- Output -------------------------------------------------------------

    def _print_basic(self) -> None:
        """Plain-text CLI output (fallback when rich is unavailable)."""
        sep = "=" * 70
        info = self.system_info

        print(f"\n{sep}")
        print("SupMiner 硬件检测报告 - 主流挖矿项目版本")
        print(sep)

        # OS
        print("\n【操作系统】")
        print(f"  系统: {info.os['system']} {info.os['release']}")
        print(f"  架构: {info.os['machine']}")

        # CPU
        print("\n【处理器 CPU】")
        print(f"  型号: {info.cpu['model']}")
        print(f"  物理核心: {info.cpu['physical_cores']}")
        print(f"  逻辑核心: {info.cpu['logical_cores']}")
        if info.cpu.get("max_frequency_mhz"):
            print(f"  最大频率: {info.cpu['max_frequency_mhz']} MHz")

        # Memory
        print("\n【内存 RAM】")
        print(f"  总容量: {info.memory['total_gb']} GB")
        print(f"  已使用: {info.memory['used_gb']} GB ({info.memory['percent']}%)")
        print(f"  可用: {info.memory['available_gb']} GB")

        # GPU
        print("\n【显卡 GPU】")
        for i, gpu in enumerate(info.gpu, 1):
            print(f"  显卡 {i}:")
            print(f"    厂商: {gpu['vendor']}")
            print(f"    型号: {gpu['model']}")
            print(f"    显存: {gpu['memory']}")
            if gpu.get("driver", "N/A") != "N/A":
                print(f"    驱动: {gpu['driver']}")

        # Recommendations
        print(f"\n{sep}")
        print("【推荐的主流挖矿项目】")
        print(sep)

        for rec in info.recommended_projects:
            if "warnings" in rec:
                print(f"\n{rec['category']}")
                print("-" * 70)
                for w in rec["warnings"]:
                    print(f"  ⚠️  {w}")
            else:
                print(f"\n{rec['category']} - 优先级: {rec['priority']}")
                if rec.get("note"):
                    print(f"  💡 {rec['note']}")
                print("-" * 70)
                for proj in rec.get("projects", []):
                    print(f"\n  🪙 {proj['name']}")
                    print(f"     算法: {proj['algorithm']}")
                    print(f"     简介: {proj['description']}")
                    print(f"     矿池: {', '.join(proj['pools'])}")
                    print(f"     交易所: {', '.join(proj['exchanges'])}")
                    print(f"     硬件: {proj['hardware']}")

        print(f"\n{sep}")
        print("详细的JSON报告已保存到: hardware_report.json")
        print(f"{sep}\n")

    def _print_rich(self) -> None:
        """Rich-formatted CLI output."""
        info = self.system_info

        console.print(
            Panel.fit(
                "[bold cyan]SupMiner 硬件检测报告 - 主流挖矿项目版本[/]",
                border_style="cyan",
            )
        )

        # OS
        console.print("\n[bold yellow]【操作系统】[/]")
        console.print(f"  系统: {info.os['system']} {info.os['release']}")
        console.print(f"  架构: {info.os['machine']}")

        # CPU
        console.print("\n[bold yellow]【处理器 CPU】[/]")
        console.print(f"  型号: {info.cpu['model']}")
        console.print(f"  物理核心: {info.cpu['physical_cores']}")
        console.print(f"  逻辑核心: {info.cpu['logical_cores']}")
        if info.cpu.get("max_frequency_mhz"):
            console.print(f"  最大频率: {info.cpu['max_frequency_mhz']} MHz")

        # Memory
        console.print("\n[bold yellow]【内存 RAM】[/]")
        console.print(f"  总容量: {info.memory['total_gb']} GB")
        console.print(f"  已使用: {info.memory['used_gb']} GB ({info.memory['percent']}%)")
        console.print(f"  可用: {info.memory['available_gb']} GB")

        # GPU
        console.print("\n[bold yellow]【显卡 GPU】[/]")
        for i, gpu in enumerate(info.gpu, 1):
            console.print(f"  显卡 {i}:")
            console.print(f"    厂商: {gpu['vendor']}")
            console.print(f"    型号: [green]{gpu['model']}[/]")
            console.print(f"    显存: {gpu['memory']}")
            if gpu.get("driver", "N/A") != "N/A":
                console.print(f"    驱动: {gpu['driver']}")

        # Recommendations
        console.print(f"\n[bold cyan]{'=' * 70}[/]")
        console.print("[bold]【推荐的主流挖矿项目】[/]")
        console.print(f"[bold cyan]{'=' * 70}[/]")

        for rec in info.recommended_projects:
            if "warnings" in rec:
                console.print(f"\n[bold red]{rec['category']}[/]")
                console.print("-" * 70)
                for w in rec["warnings"]:
                    console.print(f"  [yellow]⚠️[/]  {w}")
            else:
                console.print(f"\n[bold green]{rec['category']}[/] - 优先级: [cyan]{rec['priority']}[/]")
                if rec.get("note"):
                    console.print(f"  [blue]💡 {rec['note']}[/]")
                console.print("-" * 70)
                for proj in rec.get("projects", []):
                    console.print(f"\n  [bold white]🪙 {proj['name']}[/]")
                    console.print(f"     算法: [yellow]{proj['algorithm']}[/]")
                    console.print(f"     简介: {proj['description']}")
                    console.print(f"     矿池: {', '.join(proj['pools'])}")
                    console.print(f"     交易所: {', '.join(proj['exchanges'])}")
                    console.print(f"     硬件: {proj['hardware']}")

        console.print(f"\n[bold cyan]{'=' * 70}[/]")
        console.print("详细的JSON报告已保存到: [green]hardware_report.json[/]")
        console.print(f"[bold cyan]{'=' * 70}[/]\n")

    def generate_report(self) -> None:
        if RICH_AVAILABLE:
            self._print_rich()
        else:
            self._print_basic()

    def save_json_report(self, filename: str = "hardware_report.json") -> None:
        path = Path(filename)
        path.write_text(
            json.dumps(self.system_info.to_dict(), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def run(self) -> None:
        print("正在检测硬件配置...")
        self.detect_os()
        self.detect_cpu()
        self.detect_memory()
        self.detect_gpu()

        print("正在分析并推荐主流挖矿项目...")
        self.recommend_projects()

        self.generate_report()
        self.save_json_report()


# ---------------------------------------------------------------------------
# CLI Entry
# ---------------------------------------------------------------------------

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          SupMiner 硬件检测工具 - 主流项目版本 v3.0            ║
║                                                              ║
║          推荐的都是上交易所的主流币种                         ║
║          支持蚂蚁矿池、F2Pool、币安矿池等                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""


def main() -> None:
    print(BANNER)
    detector = HardwareDetector()
    detector.run()
    print("\n✅ 检测完成！")
    print("📧 如需专业挖矿部署服务，请联系:")
    print("   - 网站: https://supminer.net")
    print("   - 邮箱: support@supminer.net")
    print("   - Telegram: @supminer")
    print("\n💡 提示: 所有推荐项目均为主流币种，流动性有保障")
    print("⚠️  理性投资，谨防诈骗！\n")
    print("---")
    print("Project by Davey Wong <wgwcko@gmail.com> | https://www.guangweiblog.com")
    print("Licensed under MIT.\n")


if __name__ == "__main__":
    main()
