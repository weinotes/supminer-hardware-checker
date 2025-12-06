# GitHub 上传步骤详解

本文档详细说明如何将 SupMiner Hardware Checker 项目上传到 GitHub。

## 📋 前置准备

### 1. 注册 GitHub 账号

如果还没有 GitHub 账号：
1. 访问 [github.com](https://github.com)
2. 点击 "Sign up" 注册账号
3. 验证邮箱

### 2. 安装 Git

#### Windows:
```bash
# 下载并安装 Git for Windows
# https://git-scm.com/download/windows
```

#### macOS:
```bash
# 使用 Homebrew 安装
brew install git

# 或使用 Xcode Command Line Tools
xcode-select --install
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install git
```

#### Linux (CentOS/RHEL):
```bash
sudo yum install git
```

### 3. 配置 Git

```bash
# 设置用户名（替换成你的 GitHub 用户名）
git config --global user.name "你的用户名"

# 设置邮箱（替换成你的 GitHub 邮箱）
git config --global user.email "your-email@example.com"

# 验证配置
git config --list
```

## 🚀 方法一：通过命令行上传（推荐）

### 步骤 1: 在 GitHub 创建新仓库

1. 登录 GitHub
2. 点击右上角 "+" → "New repository"
3. 填写信息：
   - **Repository name**: `supminer-hardware-checker`
   - **Description**: `智能硬件检测工具 - 为挖矿项目推荐最适合的方案`
   - **Public/Private**: 选择 Public（公开）
   - ⚠️ **不要勾选** "Initialize this repository with a README"
4. 点击 "Create repository"

### 步骤 2: 准备项目文件

```bash
# 创建项目目录
mkdir supminer-hardware-checker
cd supminer-hardware-checker

# 将以下文件复制到这个目录：
# - hardware_checker.py
# - README.md
# - requirements.txt
# - .gitignore
# - LICENSE
```

### 步骤 3: 初始化 Git 仓库

```bash
# 初始化 Git 仓库
git init

# 添加所有文件到暂存区
git add .

# 查看状态（可选）
git status

# 提交文件
git commit -m "Initial commit: Add hardware checker v1.0.0"
```

### 步骤 4: 连接远程仓库并推送

```bash
# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/supminer-hardware-checker.git

# 查看远程仓库（可选）
git remote -v

# 推送到 GitHub（首次推送）
git branch -M main
git push -u origin main
```

如果遇到身份验证问题，GitHub 会提示你登录。

### 步骤 5: 验证上传

1. 访问 `https://github.com/YOUR_USERNAME/supminer-hardware-checker`
2. 确认所有文件已上传
3. 检查 README.md 是否正确显示

## 🌐 方法二：通过 GitHub Desktop（图形界面）

### 步骤 1: 安装 GitHub Desktop

1. 下载 [GitHub Desktop](https://desktop.github.com/)
2. 安装并登录你的 GitHub 账号

### 步骤 2: 创建新仓库

1. 打开 GitHub Desktop
2. 点击 "File" → "New repository"
3. 填写信息：
   - **Name**: `supminer-hardware-checker`
   - **Description**: `智能硬件检测工具`
   - **Local path**: 选择存放项目的位置
4. 点击 "Create repository"

### 步骤 3: 添加文件

1. 将所有项目文件复制到仓库目录
2. GitHub Desktop 会自动检测到新文件
3. 在左侧查看更改列表

### 步骤 4: 提交并推送

1. 在底部输入提交信息：`Initial commit: Add hardware checker v1.0.0`
2. 点击 "Commit to main"
3. 点击 "Publish repository"
4. 选择 Public 或 Private
5. 点击 "Publish repository"

## 🔐 方法三：使用 SSH 密钥（高级）

如果你经常使用 Git，建议设置 SSH 密钥以避免频繁输入密码。

### 步骤 1: 生成 SSH 密钥

```bash
# 生成 SSH 密钥（替换邮箱）
ssh-keygen -t ed25519 -C "your-email@example.com"

# 如果你的系统不支持 ed25519，使用 RSA
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"

# 按提示操作（可直接回车使用默认设置）
```

### 步骤 2: 添加 SSH 密钥到 GitHub

```bash
# 复制公钥到剪贴板
# macOS:
pbcopy < ~/.ssh/id_ed25519.pub

# Linux:
cat ~/.ssh/id_ed25519.pub
# 然后手动复制输出内容

# Windows (Git Bash):
clip < ~/.ssh/id_ed25519.pub
```

在 GitHub 上：
1. 点击头像 → Settings
2. 左侧选择 "SSH and GPG keys"
3. 点击 "New SSH key"
4. 粘贴公钥，添加标题
5. 点击 "Add SSH key"

### 步骤 3: 使用 SSH URL 推送

```bash
# 使用 SSH URL 添加远程仓库
git remote add origin git@github.com:YOUR_USERNAME/supminer-hardware-checker.git

# 推送
git push -u origin main
```

## 📝 后续更新操作

当你修改代码后，使用以下命令更新 GitHub：

```bash
# 查看修改
git status

# 添加修改的文件
git add .

# 或添加特定文件
git add hardware_checker.py

# 提交修改
git commit -m "Update: 描述你的修改"

# 推送到 GitHub
git push
```

## 🏷️ 创建版本标签

```bash
# 创建标签
git tag -a v1.0.0 -m "Release version 1.0.0"

# 推送标签
git push origin v1.0.0

# 或推送所有标签
git push --tags
```

## 📦 创建 Release

在 GitHub 网页上：
1. 进入仓库页面
2. 点击右侧 "Releases"
3. 点击 "Create a new release"
4. 选择标签或创建新标签 `v1.0.0`
5. 填写标题和说明
6. 可以附加编译好的文件
7. 点击 "Publish release"

## ⚙️ 配置项目主页

### 添加 Topics (标签)

在仓库页面：
1. 点击右侧 "About" 旁边的设置图标
2. 添加 topics: `python`, `hardware-detection`, `mining`, `gpu`, `cpu`
3. 添加网址: `https://supminer.net`
4. 保存

### 设置 GitHub Pages (可选)

如果你想创建项目网站：
1. 进入仓库 Settings
2. 左侧选择 "Pages"
3. Source 选择 "main" 分支
4. 保存

## 📊 添加徽章到 README

已经在 README.md 中添加了徽章：
- Version badge
- Python version badge
- License badge

你可以访问 [shields.io](https://shields.io) 添加更多徽章。

## 🔍 常见问题

### 问题 1: 推送时提示权限错误

**解决方案:**
```bash
# 确认远程仓库 URL
git remote -v

# 如果是 HTTPS，可能需要更新凭据
# Windows: 在凭据管理器中更新 GitHub 凭据
# Mac: 在钥匙串中更新 GitHub 凭据
# Linux: 使用 git credential helper
```

### 问题 2: 文件太大无法推送

GitHub 单个文件限制 100MB

**解决方案:**
```bash
# 使用 Git LFS（Large File Storage）
git lfs install
git lfs track "*.bin"
git add .gitattributes
git commit -m "Add Git LFS"
```

### 问题 3: 忘记添加 .gitignore

如果已经提交了不该提交的文件：

```bash
# 从 Git 移除但保留本地文件
git rm --cached hardware_report.json

# 添加到 .gitignore
echo "hardware_report.json" >> .gitignore

# 提交更改
git add .gitignore
git commit -m "Update .gitignore"
git push
```

### 问题 4: 合并冲突

如果本地和远程版本冲突：

```bash
# 拉取远程更改
git pull origin main

# 手动解决冲突
# 编辑冲突文件，删除冲突标记

# 标记为已解决
git add .

# 提交合并
git commit -m "Resolve merge conflicts"

# 推送
git push
```

## 📚 Git 常用命令速查

```bash
# 查看状态
git status

# 查看历史
git log
git log --oneline

# 查看差异
git diff

# 撤销修改
git checkout -- filename

# 撤销暂存
git reset HEAD filename

# 创建分支
git branch feature-name
git checkout -b feature-name

# 切换分支
git checkout main

# 合并分支
git merge feature-name

# 删除分支
git branch -d feature-name

# 查看远程仓库
git remote -v

# 拉取更新
git pull

# 克隆仓库
git clone https://github.com/YOUR_USERNAME/supminer-hardware-checker.git
```

## 🎯 最佳实践

1. **提交信息规范**:
   ```
   feat: 添加新功能
   fix: 修复bug
   docs: 文档更新
   style: 代码格式化
   refactor: 重构代码
   test: 测试相关
   chore: 构建工具或辅助工具的变动
   ```

2. **频繁提交**: 小步提交，方便回滚

3. **使用分支**: 
   - `main`: 稳定版本
   - `develop`: 开发版本
   - `feature/xxx`: 新功能分支
   - `hotfix/xxx`: 紧急修复分支

4. **编写好的 README**: 清晰的文档能吸引更多用户

5. **添加 LICENSE**: 明确开源协议

6. **使用 .gitignore**: 避免提交敏感或临时文件

## 🆘 获取帮助

- GitHub 文档: https://docs.github.com
- Git 文档: https://git-scm.com/doc
- SupMiner 支持: support@supminer.net

## ✅ 检查清单

上传前检查：

- [ ] 所有文件都已创建
- [ ] README.md 内容完整
- [ ] .gitignore 配置正确
- [ ] LICENSE 已添加
- [ ] 代码已测试
- [ ] 注释清晰
- [ ] 移除敏感信息
- [ ] Git 配置正确
- [ ] 远程仓库已创建

上传后检查：

- [ ] 所有文件都已上传
- [ ] README.md 正确显示
- [ ] 仓库描述已填写
- [ ] Topics 已添加
- [ ] 网址已链接
- [ ] Release 已创建（如需要）

---

祝你顺利上传项目到 GitHub! 🎉

如有问题，欢迎访问 [supminer.net](https://supminer.net) 联系我们。
