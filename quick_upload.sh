#!/bin/bash
# SupMiner Hardware Checker - 快速上传到 GitHub 脚本
# 使用方法: ./quick_upload.sh

set -e  # 遇到错误立即退出

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║     SupMiner Hardware Checker - GitHub 快速上传工具      ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# 检查是否安装了 git
if ! command -v git &> /dev/null; then
    echo "❌ 错误: 未安装 Git"
    echo "请先安装 Git: https://git-scm.com/downloads"
    exit 1
fi

# 检查 git 配置
if [ -z "$(git config user.name)" ] || [ -z "$(git config user.email)" ]; then
    echo "⚠️  Git 配置不完整"
    echo ""
    read -p "请输入你的 GitHub 用户名: " username
    read -p "请输入你的 GitHub 邮箱: " email
    
    git config --global user.name "$username"
    git config --global user.email "$email"
    
    echo "✅ Git 配置完成"
    echo ""
fi

# 显示当前配置
echo "当前 Git 配置:"
echo "  用户名: $(git config user.name)"
echo "  邮箱: $(git config user.email)"
echo ""

# 获取 GitHub 用户名
read -p "请输入你的 GitHub 用户名: " github_username

# 检查是否已初始化 git 仓库
if [ ! -d ".git" ]; then
    echo "📦 初始化 Git 仓库..."
    git init
    echo "✅ Git 仓库初始化完成"
    echo ""
else
    echo "✅ Git 仓库已存在"
    echo ""
fi

# 添加所有文件
echo "📁 添加文件到暂存区..."
git add .

# 显示将要提交的文件
echo ""
echo "将要提交的文件:"
git status --short

echo ""
read -p "确认提交这些文件吗? (y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "❌ 取消上传"
    exit 0
fi

# 提交
echo ""
echo "💾 提交文件..."
git commit -m "Initial commit: Add SupMiner Hardware Checker v1.0.0

- Add hardware detection script
- Add comprehensive README
- Add requirements.txt
- Add MIT license
- Add .gitignore"

echo "✅ 文件已提交到本地仓库"
echo ""

# 检查远程仓库
if git remote | grep -q "origin"; then
    echo "⚠️  检测到已存在的远程仓库"
    git remote -v
    echo ""
    read -p "是否替换现有的远程仓库? (y/n): " replace
    
    if [ "$replace" = "y" ] || [ "$replace" = "Y" ]; then
        git remote remove origin
        echo "✅ 已移除旧的远程仓库"
    else
        echo "⏩ 使用现有的远程仓库"
        git branch -M main
        git push -u origin main
        exit 0
    fi
fi

# 添加远程仓库
echo "🔗 添加远程仓库..."
remote_url="https://github.com/$github_username/supminer-hardware-checker.git"
git remote add origin "$remote_url"
echo "✅ 远程仓库已添加: $remote_url"
echo ""

# 推送到 GitHub
echo "🚀 推送到 GitHub..."
echo "⚠️  首次推送可能需要登录 GitHub"
echo ""

git branch -M main

if git push -u origin main; then
    echo ""
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║                    🎉 上传成功! 🎉                        ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    echo ""
    echo "📍 你的项目地址:"
    echo "   https://github.com/$github_username/supminer-hardware-checker"
    echo ""
    echo "📝 后续更新命令:"
    echo "   git add ."
    echo "   git commit -m \"Update: 描述你的修改\""
    echo "   git push"
    echo ""
    echo "🌟 别忘了:"
    echo "   1. 在 GitHub 上添加仓库描述"
    echo "   2. 添加 topics: python, hardware-detection, mining"
    echo "   3. 设置仓库网址: https://supminer.net"
    echo "   4. 创建 Release 发布正式版本"
    echo ""
else
    echo ""
    echo "❌ 推送失败"
    echo ""
    echo "可能的原因:"
    echo "1. GitHub 仓库尚未创建"
    echo "   解决: 访问 https://github.com/new 创建名为 'supminer-hardware-checker' 的仓库"
    echo ""
    echo "2. 身份验证失败"
    echo "   解决: 配置 GitHub 访问令牌或 SSH 密钥"
    echo ""
    echo "3. 网络连接问题"
    echo "   解决: 检查网络连接"
    echo ""
    echo "详细说明请查看: GITHUB_UPLOAD_GUIDE.md"
    exit 1
fi
