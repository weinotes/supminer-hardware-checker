@echo off
chcp 65001 >nul
REM SupMiner Hardware Checker - GitHub 快速上传工具 (Windows版本)
REM 使用方法: 双击运行或在命令行中执行 quick_upload.bat

setlocal enabledelayedexpansion

echo ╔═══════════════════════════════════════════════════════════╗
echo ║     SupMiner Hardware Checker - GitHub 快速上传工具      ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

REM 检查是否安装了 git
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ 错误: 未安装 Git
    echo 请先安装 Git: https://git-scm.com/downloads
    pause
    exit /b 1
)

REM 检查 git 配置
for /f "delims=" %%i in ('git config user.name') do set git_username=%%i
for /f "delims=" %%i in ('git config user.email') do set git_email=%%i

if "!git_username!"=="" (
    echo ⚠️  Git 配置不完整
    echo.
    set /p username="请输入你的 GitHub 用户名: "
    set /p email="请输入你的 GitHub 邮箱: "
    
    git config --global user.name "!username!"
    git config --global user.email "!email!"
    
    echo ✅ Git 配置完成
    echo.
)

REM 显示当前配置
echo 当前 Git 配置:
for /f "delims=" %%i in ('git config user.name') do echo   用户名: %%i
for /f "delims=" %%i in ('git config user.email') do echo   邮箱: %%i
echo.

REM 获取 GitHub 用户名
set /p github_username="请输入你的 GitHub 用户名: "

REM 检查是否已初始化 git 仓库
if not exist ".git" (
    echo 📦 初始化 Git 仓库...
    git init
    echo ✅ Git 仓库初始化完成
    echo.
) else (
    echo ✅ Git 仓库已存在
    echo.
)

REM 添加所有文件
echo 📁 添加文件到暂存区...
git add .

REM 显示将要提交的文件
echo.
echo 将要提交的文件:
git status --short

echo.
set /p confirm="确认提交这些文件吗? (y/n): "

if /i not "!confirm!"=="y" (
    echo ❌ 取消上传
    pause
    exit /b 0
)

REM 提交
echo.
echo 💾 提交文件...
git commit -m "Initial commit: Add SupMiner Hardware Checker v1.0.0" -m "" -m "- Add hardware detection script" -m "- Add comprehensive README" -m "- Add requirements.txt" -m "- Add MIT license" -m "- Add .gitignore"

echo ✅ 文件已提交到本地仓库
echo.

REM 检查远程仓库
git remote | findstr "origin" >nul 2>nul
if %errorlevel% equ 0 (
    echo ⚠️  检测到已存在的远程仓库
    git remote -v
    echo.
    set /p replace="是否替换现有的远程仓库? (y/n): "
    
    if /i "!replace!"=="y" (
        git remote remove origin
        echo ✅ 已移除旧的远程仓库
    ) else (
        echo ⏩ 使用现有的远程仓库
        git branch -M main
        git push -u origin main
        goto :success
    )
)

REM 添加远程仓库
echo 🔗 添加远程仓库...
set remote_url=https://github.com/!github_username!/supminer-hardware-checker.git
git remote add origin "!remote_url!"
echo ✅ 远程仓库已添加: !remote_url!
echo.

REM 推送到 GitHub
echo 🚀 推送到 GitHub...
echo ⚠️  首次推送可能需要登录 GitHub
echo.

git branch -M main
git push -u origin main

if %errorlevel% equ 0 (
    :success
    echo.
    echo ╔═══════════════════════════════════════════════════════════╗
    echo ║                    🎉 上传成功! 🎉                        ║
    echo ╚═══════════════════════════════════════════════════════════╝
    echo.
    echo 📍 你的项目地址:
    echo    https://github.com/!github_username!/supminer-hardware-checker
    echo.
    echo 📝 后续更新命令:
    echo    git add .
    echo    git commit -m "Update: 描述你的修改"
    echo    git push
    echo.
    echo 🌟 别忘了:
    echo    1. 在 GitHub 上添加仓库描述
    echo    2. 添加 topics: python, hardware-detection, mining
    echo    3. 设置仓库网址: https://supminer.net
    echo    4. 创建 Release 发布正式版本
    echo.
) else (
    echo.
    echo ❌ 推送失败
    echo.
    echo 可能的原因:
    echo 1. GitHub 仓库尚未创建
    echo    解决: 访问 https://github.com/new 创建名为 'supminer-hardware-checker' 的仓库
    echo.
    echo 2. 身份验证失败
    echo    解决: 配置 GitHub 访问令牌或 SSH 密钥
    echo.
    echo 3. 网络连接问题
    echo    解决: 检查网络连接
    echo.
    echo 详细说明请查看: GITHUB_UPLOAD_GUIDE.md
    echo.
)

pause
