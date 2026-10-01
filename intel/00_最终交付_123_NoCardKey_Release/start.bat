@echo off
chcp 65001 >nul
title XWGZSkins 无卡密免验证版
cd /d "%~dp0"
echo [*] 启动无卡密环境...
sc start CrytMap >nul 2>&1
echo [*] 启动主程序 123.exe（UeVerify.dll 已打免卡密补丁）
start "" "%~dp0123.exe"
echo [*] 已启动，若弹出卡密窗口说明补丁未命中，请查看 launcher.log
