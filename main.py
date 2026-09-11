"""Jogo de Pedra, Papel e Tesoura (Jokenpô) via terminal — projeto educacional de POO.

Material de estudo para prática de lógica de programação, dicionários e
Orientação a Objetos em Python puro (sem dependências externas).

ESTRUTURA DO CÓDIGO (BASEADA EM CLASSE):
1. CLASSE (PedraPapelTesoura): Funciona como um 'molde' para o jogo.
2. SELF: É a forma de acessar os dados da própria instância (como pontos e jogadas).
3. MÉTODOS: São as funções que pertencem à classe (ex: exibir_placar).
4. INICIALIZAÇÃO (__init__): Onde as opções e o placar zerado são definidos.
5. INTERFACE (exibir_placar): Limpeza de tela, placar e menu de opções.
6. REGRAS DE VITÓRIA (determinar_vencedor): A lógica que compara as jogadas.
7. AGENTES (usuário vs computador): Funções que gerenciam as escolhas de cada um.
8. LOOP PRINCIPAL (main): O controle das rodadas e a opção de jogar novamente (Replay).
"""

from __future__ import annotations

import os
import random
import sys

# No Windows, stdout sem console UTF-8 (saída redirecionada/pipe, alguns
# executores de CI) cai para cp1252 e quebra os emojis abaixo com
# UnicodeEncodeError; reconfigurar para UTF-8 evita o crash em qualquer ambiente.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Regras de vitória: cada chave vence o valor correspondente.
REGRAS_VITORIA = {
    "pedra": "tesoura",
    "papel": "pedra",
    "tesoura": "papel",
}


class PedraPapelTesoura:
    """Motor do jogo: guarda placar, jogadas da rodada e decide o vencedor."""

    def __init__(self) -> None:
        """O 'self' garante que cada instância tenha seu próprio placar e opções."""
        self.opcoes: list[str] = ["pedra", "papel", "tesoura"]
        self.pontos_usuario: int = 0
        self.pontos_computador: int = 0
        self.jogada_usuario: str = ""
        self.jogada_computador: str = ""

    def limpar_tela(self) -> None:
        """Limpa o terminal, detectando o sistema operacional automaticamente."""
        # 'nt' é o identificador interno para Windows.
        comando = "cls" if os.name == "nt" else "clear"
        os.system(comando)

    def exibir_placar(self, mensagem_resultado: str = "") -> None:
        """Redesenha a tela: placar atual, resultado da última rodada e menu.

        Args:
            mensagem_resultado (str, optional): Resultado da rodada anterior a
                exibir. Vazio (padrão) quando ainda não houve rodada.
        """
        self.limpar_tela()
        print("============================================")
        placar = f"Você {self.pontos_usuario} x {self.pontos_computador} Computador"
        print(f"PLACAR: {placar}")
        print("============================================")

        if mensagem_resultado:
            print("\nÚLTIMA RODADA:")
            print(f"Você escolheu: {self.jogada_usuario.upper()}")
            print(f"Computador escolheu: {self.jogada_computador.upper()}")
            print(f"👉 {mensagem_resultado}")
            print("--------------------------------------------")

        print("\nESCOLHA SUA JOGADA:")
        print("0 - Pedra | 1 - Papel | 2 - Tesoura")

    def realizar_jogada_usuario(self) -> None:
        """Lê a jogada do usuário pelo teclado, validando até receber 0, 1 ou 2."""
        while True:
            try:
                escolha = int(input("\nDigite o número da sua jogada: "))
                if 0 <= escolha <= 2:
                    self.jogada_usuario = self.opcoes[escolha]
                    break
                print("⚠️ Opção inválida! Escolha entre 0, 1 ou 2.")
            except ValueError:
                print("⚠️ Entrada inválida! Digite apenas números inteiros.")

    def realizar_jogada_computador(self) -> None:
        """Sorteia a jogada do computador entre as opções disponíveis."""
        self.jogada_computador = random.choice(self.opcoes)

    def determinar_vencedor(self) -> str:
        """Compara as duas jogadas e atualiza o placar.

        Returns:
            str: Mensagem de resultado da rodada (empate, vitória ou derrota).
        """
        if self.jogada_usuario == self.jogada_computador:
            return "🤝 EMPATE!"

        if REGRAS_VITORIA[self.jogada_usuario] == self.jogada_computador:
            self.pontos_usuario += 1
            return "🎉 VOCÊ VENCEU A RODADA!"

        self.pontos_computador += 1
        return "😢 O COMPUTADOR VENCEU A RODADA!"


def main() -> None:
    """Roda o loop principal: joga rodadas até o usuário decidir encerrar."""
    jogo = PedraPapelTesoura()
    resultado_texto = ""

    while True:
        jogo.exibir_placar(resultado_texto)
        jogo.realizar_jogada_usuario()
        jogo.realizar_jogada_computador()

        resultado_texto = jogo.determinar_vencedor()

        # Exibe o status final da rodada antes de perguntar o replay.
        jogo.exibir_placar(resultado_texto)

        while True:
            pergunta = input("\nDeseja jogar outra rodada? (0 - SIM | 1 - NÃO): ")
            if pergunta == "0":
                break
            if pergunta == "1":
                placar_final = f"{jogo.pontos_usuario} x {jogo.pontos_computador}"
                print(f"\nSessão encerrada com placar de {placar_final}.")
                print("Até a próxima! 👋")
                return
            print("⚠️ Resposta inválida. Digite 0 ou 1.")


if __name__ == "__main__":
    main()
