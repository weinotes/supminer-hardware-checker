#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SupMiner Hardware Checker
硬件检测工具 - 判断适合GPU还是CPU挖矿

Website: https://supminer.net
"""

import platform
import subprocess
import sys
import json
from datetime import datetime

class HardwareChecker:
    def __init__(self):
        self.system = platform.system()
        self.results = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "system": {},
            "cpu": {},
            "gpu": [],
            "memory": {},
            "recommendation": {}
        }
    
    def get_system_info(self):
        """获取系统基本信息"""
        try:
            self.results["system"] = {
                "os": platform.system(),
                "os_version": platform.version(),
                "architecture": platform.machine(),
                "hostname": platform.node()
            }
        except Exception as e:
            print(f"获取系统信息时出错: {e}")
    
    def get_cpu_info(self):
        """获取CPU信息"""
        try:
            import psutil
            
            cpu_info = {
                "model": platform.processor(),
                "physical_cores": psutil.cpu_count(logical=False),
                "total_cores": psutil.cpu_count(logical=True),
                "max_frequency": f"{psutil.cpu_freq().max:.2f} MHz" if psutil.cpu_freq() else "N/A",
                "current_frequency": f"{psutil.cpu_freq().current:.2f} MHz" if psutil.cpu_freq() else "N/A"
            }
            
            # Linux系统获取更详细的CPU信息
            if self.system == "Linux":
                try:
                    with open('/proc/cpuinfo', 'r') as f:
                        cpuinfo = f.read()
                        for line in cpuinfo.split('\n'):
                            if 'model name' in line:
                                cpu_info["model"] = line.split(':')[1].strip()
                                break
                except:
                    pass
            
            self.results["cpu"] = cpu_info
            
        except ImportError:
            print("警告: 未安装 psutil 库，CPU信息可能不完整")
            self.results["cpu"] = {
                "model": platform.processor(),
                "cores": "需要安装 psutil: pip install psutil"
            }
        except Exception as e:
            print(f"获取CPU信息时出错: {e}")
    
    def get_gpu_info(self):
        """获取GPU信息"""
        gpus = []
        
        # 尝试使用 nvidia-smi (NVIDIA GPU)
        try:
            if self.system in ["Linux", "Windows"]:
                cmd = "nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
                
                if result.returncode == 0:
                    for line in result.stdout.strip().split('\n'):
                        if line:
                            parts = [p.strip() for p in line.split(',')]
                            if len(parts) >= 2:
                                gpus.append({
                                    "type": "NVIDIA",
                                    "model": parts[0],
                                    "memory": parts[1],
                                    "driver": parts[2] if len(parts) > 2 else "N/A"
                                })
        except Exception as e:
            pass
        
        # 尝试检测 AMD GPU (Linux)
        if self.system == "Linux" and not gpus:
            try:
                result = subprocess.run("lspci | grep -i vga", shell=True, capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    for line in result.stdout.strip().split('\n'):
                        if 'AMD' in line or 'Radeon' in line:
                            gpus.append({
                                "type": "AMD",
                                "model": line.split(':')[-1].strip(),
                                "memory": "请使用 rocm-smi 查看详细信息"
                            })
            except:
                pass
        
        # 尝试检测集成显卡
        if not gpus:
            try:
                if self.system == "Windows":
                    result = subprocess.run("wmic path win32_videocontroller get name", 
                                          shell=True, capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        lines = result.stdout.strip().split('\n')[1:]
                        for line in lines:
                            if line.strip():
                                gpus.append({
                                    "type": "Integrated/Other",
                                    "model": line.strip(),
                                    "memory": "N/A"
                                })
                elif self.system == "Linux":
                    result = subprocess.run("lspci | grep -i vga", shell=True, capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        for line in result.stdout.strip().split('\n'):
                            if line.strip():
                                gpus.append({
                                    "type": "Integrated/Other",
                                    "model": line.split(':')[-1].strip(),
                                    "memory": "N/A"
                                })
            except:
                pass
        
        self.results["gpu"] = gpus if gpus else [{"type": "None", "model": "未检测到独立显卡"}]
    
    def get_memory_info(self):
        """获取内存信息"""
        try:
            import psutil
            
            mem = psutil.virtual_memory()
            self.results["memory"] = {
                "total": f"{mem.total / (1024**3):.2f} GB",
                "available": f"{mem.available / (1024**3):.2f} GB",
                "percent_used": f"{mem.percent}%"
            }
        except ImportError:
            print("警告: 未安装 psutil 库，内存信息不可用")
            self.results["memory"] = {"info": "需要安装 psutil: pip install psutil"}
        except Exception as e:
            print(f"获取内存信息时出错: {e}")
    
    def analyze_and_recommend(self):
        """分析硬件并给出挖矿建议"""
        recommendation = {
            "primary_type": "",
            "reason": [],
            "suitable_projects": [],
            "warnings": []
        }
        
        # 分析GPU
        has_nvidia = any(gpu.get("type") == "NVIDIA" for gpu in self.results["gpu"])
        has_amd = any(gpu.get("type") == "AMD" for gpu in self.results["gpu"])
        has_gpu = has_nvidia or has_amd
        
        # 分析CPU
        cpu_cores = self.results["cpu"].get("physical_cores", 0)
        total_cores = self.results["cpu"].get("total_cores", 0)
        
        # GPU挖矿评估
        if has_nvidia:
            recommendation["primary_type"] = "GPU挖矿（优先推荐）"
            recommendation["reason"].append("✅ 检测到NVIDIA显卡，适合GPU挖矿")
            recommendation["suitable_projects"].extend([
                "Qubic (GPU) - 推荐",
                "Nexa (GPU)",
                "Nexus (GPU)",
                "Gauntlet (GPU)"
            ])
        
        if has_amd:
            if not has_nvidia:
                recommendation["primary_type"] = "GPU挖矿（AMD）"
            recommendation["reason"].append("✅ 检测到AMD显卡，可用于GPU挖矿")
            recommendation["suitable_projects"].append("部分项目支持AMD显卡")
        
        # CPU挖矿评估
        if cpu_cores >= 4:
            if not has_gpu:
                recommendation["primary_type"] = "CPU挖矿"
                recommendation["reason"].append(f"✅ CPU拥有{cpu_cores}个物理核心，适合CPU挖矿")
            else:
                recommendation["reason"].append(f"✅ CPU拥有{cpu_cores}个物理核心，可同时进行CPU挖矿")
            
            recommendation["suitable_projects"].extend([
                "Qubic (CPU)",
                "Ore",
                "Nexus (CPU)",
                "Gauntlet (CPU)"
            ])
        elif cpu_cores > 0:
            recommendation["warnings"].append(f"⚠️ CPU仅有{cpu_cores}个物理核心，CPU挖矿效率可能较低")
        
        # 如果既没有好的GPU也没有好的CPU
        if not has_gpu and cpu_cores < 4:
            recommendation["primary_type"] = "轻量级CPU挖矿"
            recommendation["reason"].append("⚠️ 硬件配置较低，建议选择轻量级CPU项目")
            recommendation["suitable_projects"] = ["Ore (轻量级CPU挖矿)"]
        
        # 内存检查
        try:
            total_mem = float(self.results["memory"].get("total", "0").split()[0])
            if total_mem < 4:
                recommendation["warnings"].append("⚠️ 系统内存不足4GB，可能影响挖矿性能")
            elif total_mem >= 8:
                recommendation["reason"].append(f"✅ 系统内存充足 ({self.results['memory']['total']})")
        except:
            pass
        
        # 如果没有设置primary_type
        if not recommendation["primary_type"]:
            recommendation["primary_type"] = "需要升级硬件"
            recommendation["warnings"].append("❌ 当前硬件配置不适合挖矿")
        
        self.results["recommendation"] = recommendation
    
    def print_results(self):
        """打印检测结果"""
        print("\n" + "="*60)
        print("SupMiner.net 硬件检测报告")
        print("="*60)
        
        print(f"\n检测时间: {self.results['timestamp']}")
        
        print("\n【系统信息】")
        print(f"操作系统: {self.results['system'].get('os', 'N/A')}")
        print(f"系统版本: {self.results['system'].get('os_version', 'N/A')}")
        print(f"架构: {self.results['system'].get('architecture', 'N/A')}")
        
        print("\n【CPU信息】")
        cpu = self.results['cpu']
        print(f"型号: {cpu.get('model', 'N/A')}")
        print(f"物理核心: {cpu.get('physical_cores', 'N/A')}")
        print(f"逻辑核心: {cpu.get('total_cores', 'N/A')}")
        if 'max_frequency' in cpu:
            print(f"最大频率: {cpu.get('max_frequency', 'N/A')}")
        
        print("\n【GPU信息】")
        if self.results['gpu']:
            for i, gpu in enumerate(self.results['gpu'], 1):
                print(f"GPU {i}:")
                print(f"  类型: {gpu.get('type', 'N/A')}")
                print(f"  型号: {gpu.get('model', 'N/A')}")
                print(f"  显存: {gpu.get('memory', 'N/A')}")
                if 'driver' in gpu:
                    print(f"  驱动: {gpu.get('driver', 'N/A')}")
        else:
            print("未检测到GPU")
        
        print("\n【内存信息】")
        mem = self.results['memory']
        if 'total' in mem:
            print(f"总内存: {mem.get('total', 'N/A')}")
            print(f"可用内存: {mem.get('available', 'N/A')}")
            print(f"使用率: {mem.get('percent_used', 'N/A')}")
        else:
            print(mem.get('info', 'N/A'))
        
        print("\n" + "="*60)
        print("【挖矿建议】")
        print("="*60)
        rec = self.results['recommendation']
        print(f"\n推荐类型: {rec['primary_type']}")
        
        if rec['reason']:
            print("\n原因分析:")
            for reason in rec['reason']:
                print(f"  {reason}")
        
        if rec['suitable_projects']:
            print("\n适合的项目:")
            for project in rec['suitable_projects']:
                print(f"  • {project}")
        
        if rec['warnings']:
            print("\n注意事项:")
            for warning in rec['warnings']:
                print(f"  {warning}")
        
        print("\n" + "="*60)
        print("访问 https://supminer.net 获取详细安装教程")
        print("联系我们获取专业的挖矿咨询服务")
        print("="*60 + "\n")
    
    def save_to_file(self, filename="hardware_report.json"):
        """保存结果到JSON文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, ensure_ascii=False, indent=2)
            print(f"✅ 检测报告已保存到: {filename}")
        except Exception as e:
            print(f"保存报告时出错: {e}")
    
    def run(self):
        """运行完整检测"""
        print("正在检测硬件信息...")
        
        self.get_system_info()
        self.get_cpu_info()
        self.get_gpu_info()
        self.get_memory_info()
        self.analyze_and_recommend()
        
        self.print_results()
        self.save_to_file()

def check_dependencies():
    """检查依赖库"""
    try:
        import psutil
        return True
    except ImportError:
        print("\n⚠️  警告: 未安装 psutil 库")
        print("建议安装以获取完整信息: pip install psutil")
        print("继续使用基础检测功能...\n")
        return False

def main():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║         SupMiner.net 硬件检测工具 v1.0                    ║
    ║         Hardware Checker for Mining Projects              ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    check_dependencies()
    
    checker = HardwareChecker()
    checker.run()
    
    print("\n提示: 使用 'python hardware_checker.py' 可重新运行检测")

if __name__ == "__main__":
    main()
