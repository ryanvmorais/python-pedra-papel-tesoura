@echo off
title Iniciando Pedra, Papel e Tesoura...
cls

echo ===========================================
echo   VERIFICANDO AMBIENTE...
echo ===========================================

where uv >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] uv detectado. Iniciando o jogo...
    uv run main.py
    pause
    exit
)

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Nem uv nem Python foram encontrados!
    echo Instale o uv em: https://docs.astral.sh/uv/
    echo Ou o Python em: https://python.org
    pause
    exit
)

echo [OK] Python detectado (sem uv). Iniciando o jogo...
python main.py
pause
