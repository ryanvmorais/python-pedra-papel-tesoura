@echo off
title Iniciando Pedra, Papel e Tesoura...
cls

echo ===========================================
echo   VERIFICANDO AMBIENTE PYTHON...
echo ===========================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado! 
    echo Por favor, instale o Python em: https://python.org
    pause
    exit
)

echo [OK] Python detectado. Iniciando o jogo...
python PedraPapelTesoura.py
pause
