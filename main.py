"""
🪨📜✂️ PROJETO: PEDRA, PAPEL E TESOURA (JOKENPÔ)
🎯 Objetivo: Educacional - Prática de Lógica, Dicionários e Orientação a Objetos.

ESTRUTURA DO CÓDIGO (BASEADA EM CLASSE):
1. CLASSE (PedraPapelTesoura): Funciona como um 'molde' para o jogo.
2. SELF: É a forma de acessar os dados da própria instância (como pontos e jogadas).
3. MÉTODOS: São as funções que pertencem à classe (ex: exibir_placar).
4. INICIALIZAÇÃO (__init__): Onde as opções e o placar zerado são definidos.
5. INTERFACE (exibir_placar): Limpeza de tela, placar e menu de opções.
6. REGRAS DE VITÓRIA (determinar_vencedor): A lógica que compara as jogadas.
7. AGENTES (usuário vs computador): Funções que gerenciam as escolhas de cada um.
8. LOOP PRINCIPAL: O controle das rodadas e a opção de jogar novamente (Replay).
"""

import random
import subprocess
import os

class PedraPapelTesoura:
    def __init__(self):
        """
        O método __init__ é o 'construtor'. 
        O 'self' aqui garante que cada jogo tenha seu próprio placar e opções.
        """
        self.opcoes = ['pedra', 'papel', 'tesoura']
        self.pontos_usuario = 0
        self.pontos_computador = 0
        self.jogada_usuario = ''
        self.jogada_computador = ''

    def limpar_tela(self):
        # 'nt' é o identificador interno para Windows
        comando = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run(comando, shell=True)

    def exibir_placar(self, mensagem_resultado=""):
        self.limpar_tela()
        print("============================================")
        print(f"PLACAR: Você {self.pontos_usuario} x {self.pontos_computador} Computador")
        print("============================================")
        
        if mensagem_resultado:
            print(f"\nÚLTIMA RODADA:")
            print(f"Você escolheu: {self.jogada_usuario.upper()}")
            print(f"Computador escolheu: {self.jogada_computador.upper()}")
            print(f"👉 {mensagem_resultado}")
            print("--------------------------------------------")

        print("\nESCOLHA SUA JOGADA:")
        print("0 - Pedra | 1 - Papel | 2 - Tesoura")

    def realizar_jogada_usuario(self):
        while True:
            try:
                escolha = int(input("\nDigite o número da sua jogada: "))
                if 0 <= escolha <= 2:
                    self.jogada_usuario = self.opcoes[escolha]
                    break
                print("⚠️ Opção inválida! Escolha entre 0, 1 ou 2.")
            except ValueError:
                print("⚠️ Entrada inválida! Digite apenas números inteiros.")

    def realizar_jogada_computador(self):
        self.jogada_computador = random.choice(self.opcoes)

    def determinar_vencedor(self):
        if self.jogada_usuario == self.jogada_computador:
            return "🤝 EMPATE!"

        regras_vitoria = {
            'pedra': 'tesoura',
            'papel': 'pedra',
            'tesoura': 'papel'
        }

        if regras_vitoria[self.jogada_usuario] == self.jogada_computador:
            self.pontos_usuario += 1
            return "🎉 VOCÊ VENCEU A RODADA!"
        else:
            self.pontos_computador += 1
            return "😢 O COMPUTADOR VENCEU A RODADA!"

# --- Execução Principal ---
if __name__ == "__main__":
    jogo = PedraPapelTesoura()
    resultado_texto = ""
    
    while True:
        # Chamada corrigida para 'exibir_placar'
        jogo.exibir_placar(resultado_texto)
        jogo.realizar_jogada_usuario()
        jogo.realizar_jogada_computador()
        
        resultado_texto = jogo.determinar_vencedor()
        
        # Exibe o status final da rodada antes de perguntar o replay
        jogo.exibir_placar(resultado_texto)
        
        while True:
            pergunta = input('\nDeseja jogar outra rodada? (0 - SIM | 1 - NÃO): ')
            if pergunta == '0':
                break 
            elif pergunta == '1':
                print(f"\nSessão encerrada com placar de {jogo.pontos_usuario} x {jogo.pontos_computador}.")
                print("Até a próxima! 👋")
                exit()
            else:
                print("⚠️ Resposta inválida. Digite 0 ou 1.")



