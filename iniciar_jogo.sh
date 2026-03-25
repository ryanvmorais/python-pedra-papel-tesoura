#!/bin/bash

clear
echo "==========================================="
echo "   INICIANDO PEDRA, PAPEL E TESOURA..."
echo "==========================================="

if ! command -v python3 &> /dev/null
then
    echo "[ERRO] Python 3 nao encontrado!"
    echo "Por favor, instale o Python usando o seu gerenciador de pacotes."
    exit
fi

echo "[OK] Python 3 detectado. Iniciando..."
python3 PedraPapelTesoura.py
