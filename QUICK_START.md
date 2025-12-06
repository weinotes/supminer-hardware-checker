# 快速入门指南

## 📦 项目文件说明

你现在拥有以下文件：

```
supminer-hardware-checker/
├── hardware_checker.py          # 主程序 - 硬件检测脚本
├── README.md                    # 项目说明文档
├── requirements.txt             # Python依赖包列表
├── LICENSE                      # MIT开源许可证
├── .gitignore                   # Git忽略文件配置
├── GITHUB_UPLOAD_GUIDE.md       # 详细的GitHub上传教程
├── quick_upload.sh              # Linux/Mac快速上传脚本
├── quick_upload.bat             # Windows快速上传脚本
└── QUICK_START.md               # 本文件 - 快速入门
```

## 🚀 三步上传到 GitHub

### 方法一：使用快速上传脚本（最简单）

#### Windows用户：
1. 双击运行 `quick_upload.bat`
2. 按照提示输入信息
3. 完成！

#### Linux/Mac用户：
```bash
# 给脚本添加执行权限
chmod +x quick_upload.sh

# 运行脚本
./quick_upload.sh
```

### 方法二：手动上传（3条命令）

确保你已经：
- ✅ 在 GitHub 创建了名为 `supminer-hardware-checker` 的仓库
- ✅ 安装并配置了 Git

然后运行：

```bash
# 1. 初始化并提交
git init
git add .
git commit -m "Initial commit"

# 2. 连接远程仓库（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/supminer-hardware-checker.git

# 3. 推送
git branch -M main
git push -u origin main
```

## 🔧 测试硬件检测脚本

在上传到 GitHub 之前，你可以先测试脚本：

```bash
# 基础测试（无需安装依赖）
python hardware_checker.py

# 完整测试（推荐）
pip install psutil
python hardware_checker.py
```

## 📝 GitHub 仓库创建步骤

如果还没有创建 GitHub 仓库：

1. 登录 [GitHub](https://github.com)
2. 点击右上角 "+" → "New repository"
3. 填写以下信息：
   - **Repository name**: `supminer-hardware-checker`
   - **Description**: `智能硬件检测工具 - 为挖矿项目推荐最适合的方案`
   - **Public/Private**: 选择 Public
   - ⚠️ **不要勾选** "Initialize this repository with..."
4. 点击 "Create repository"

## 🎯 上传后要做的事

### 1. 完善仓库信息

在 GitHub 仓库页面：

**About 区域（右侧）：**
- 点击设置图标 ⚙️
- 添加描述：`智能硬件检测工具 - 为挖矿项目推荐最适合的方案`
- 添加网址：`https://supminer.net`
- 添加 Topics: 
  - `python`
  - `hardware-detection`
  - `mining`
  - `gpu`
  - `cpu`
  - `cryptocurrency`

### 2. 创建 Release（可选）

1. 点击右侧 "Releases"
2. 点击 "Create a new release"
3. 标签：`v1.0.0`
4. 标题：`SupMiner Hardware Checker v1.0.0`
5. 描述：
   ```
   ## 🎉 首次发布
   
   ### 功能特点
   - ✅ 智能检测 CPU、GPU、内存信息
   - ✅ 根据硬件配置推荐挖矿项目
   - ✅ 支持 Windows、Linux、macOS
   - ✅ 生成 JSON 格式检测报告
   
   ### 使用方法
   ```bash
   python hardware_checker.py
   ```
   
   访问 [supminer.net](https://supminer.net) 获取详细教程
   ```
6. 点击 "Publish release"

### 3. 在 supminer.net 上推广

在你的网站上添加：

```html
<!-- GitHub 按钮 -->
<a href="https://github.com/YOUR_USERNAME/supminer-hardware-checker" 
   class="github-button">
  <i class="fab fa-github"></i> 
  在 GitHub 上查看
</a>

<!-- 下载链接 -->
<a href="https://github.com/YOUR_USERNAME/supminer-hardware-checker/releases" 
   class="download-button">
  📥 下载检测工具
</a>
```

## 📊 用户使用流程

用户获取和使用你的工具：

### 方法1：直接下载脚本
```bash
curl -O https://raw.githubusercontent.com/YOUR_USERNAME/supminer-hardware-checker/main/hardware_checker.py
python3 hardware_checker.py
```

### 方法2：克隆仓库
```bash
git clone https://github.com/YOUR_USERNAME/supminer-hardware-checker.git
cd supminer-hardware-checker
pip install -r requirements.txt
python hardware_checker.py
```

## 🔄 后续更新流程

当你修改代码后：

```bash
# 1. 查看修改
git status

# 2. 添加修改
git add .

# 3. 提交
git commit -m "Update: 添加AMD显卡支持"

# 4. 推送
git push
```

### 版本更新示例

如果是重要更新（如v1.1.0）：

```bash
# 更新版本号
# 在 hardware_checker.py 中修改版本号

# 提交并打标签
git add .
git commit -m "Release v1.1.0: Add AMD GPU support"
git tag -a v1.1.0 -m "Version 1.1.0"
git push origin main
git push origin v1.1.0

# 在 GitHub 上创建新的 Release
```

## 🆘 常见问题

### Q1: 推送时要求输入密码？

**A:** GitHub 不再支持密码验证，需要使用个人访问令牌（Token）：

1. GitHub 头像 → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token → 勾选 `repo` 权限
3. 复制 token（只显示一次！）
4. 推送时用 token 代替密码

### Q2: 推送失败：remote: Repository not found

**A:** 检查：
- GitHub 仓库是否已创建
- 用户名是否正确
- 仓库名称是否为 `supminer-hardware-checker`

### Q3: 如何更新 README？

```bash
# 编辑 README.md
nano README.md  # 或用你喜欢的编辑器

# 提交更新
git add README.md
git commit -m "docs: Update README"
git push
```

### Q4: 想要删除某个文件？

```bash
# 删除文件并提交
git rm filename
git commit -m "Remove filename"
git push

# 仅从Git移除，保留本地文件
git rm --cached filename
git commit -m "Remove filename from git"
git push
```

## 📞 获取帮助

- 📖 详细教程：查看 `GITHUB_UPLOAD_GUIDE.md`
- 🌐 官网：[supminer.net](https://supminer.net)
- 💬 GitHub Issues：在仓库中提问
- 📧 邮箱：support@supminer.net

## ✅ 完成检查清单

上传前：
- [ ] 测试脚本运行正常
- [ ] README.md 中的用户名已替换
- [ ] Git 已安装并配置
- [ ] GitHub 账号已创建
- [ ] GitHub 仓库已创建

上传后：
- [ ] 所有文件已成功上传
- [ ] README 显示正常
- [ ] 仓库描述和 Topics 已添加
- [ ] 网址链接已设置
- [ ] Release 已创建（如需要）
- [ ] 在 supminer.net 上添加了链接

## 🎉 恭喜！

你已经成功将项目上传到 GitHub！现在用户可以：
- 查看你的代码
- 下载使用你的工具
- 提交反馈和建议
- 参与项目贡献

记得在社交媒体上分享你的项目！

---

**下一步建议：**
1. 收集用户反馈
2. 持续改进功能
3. 添加更多硬件支持
4. 创建视频教程
5. 建立用户社区

祝你的项目越来越好！🚀
