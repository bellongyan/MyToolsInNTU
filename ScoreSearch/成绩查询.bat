@echo off
chcp 65001
title 成绩查询
mode con: cols=90 lines=15
:loop
cls
echo         查询时间：%TIME%
python地址 文件位置
timeout /t 60 /nobreak >nul
goto loop
