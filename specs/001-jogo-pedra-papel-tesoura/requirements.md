---
feature: Jogo de Pedra, Papel e Tesoura (Jokenpô) via terminal
status: concluído
data: 2026-09-11
relacionado: []
origem: engenharia reversa
---

# 001 — Jogo de Pedra, Papel e Tesoura

## Contexto e problema

Este repositório é material de estudo: um jogo de terminal que exercita
lógica de programação, dicionários como estrutura de regras e Orientação a
Objetos, sem depender de nada além da biblioteca padrão do Python. O jogo já
existe e funciona (`main.py`); esta spec documenta retroativamente o
comportamento implementado, para servir de referência formal e de modelo para
futuras mudanças.

## Objetivos

- Jogar rodadas de pedra/papel/tesoura contra o computador no terminal.
- Manter um placar acumulado entre rodadas dentro da mesma sessão.
- Validar toda entrada do usuário sem travar o programa.
- Funcionar em Windows, Linux e macOS sem alteração de código.

## Não objetivos

- Modo multiplayer (dois jogadores humanos).
- Persistência do placar entre execuções (arquivo, banco de dados).
- Interface gráfica ou web.
- Variantes do jogo (ex.: "Pedra, Papel, Tesoura, Lagarto, Spock").

## Personas

- **Aprendiz de Python**: quer ler o código e entender como uma classe,
  `self`, um dicionário de regras e um loop de jogo se encaixam.
- **Jogador casual**: só quer abrir o jogo (com duplo clique ou um comando) e
  jogar algumas rodadas no terminal.

## Requisitos funcionais

### RF-01 — Escolher uma jogada por número

- **Given** o menu de opções está visível (0 - Pedra, 1 - Papel, 2 - Tesoura)
  **When** o usuário digita `0`, `1` ou `2`
  **Then** a jogada correspondente ("pedra", "papel" ou "tesoura") é
  registrada e o jogo segue para o sorteio do computador.
- **Given** o usuário digita um número fora do intervalo 0-2 (ex.: `5`)
  **When** a entrada é validada
  **Then** uma mensagem de erro é exibida e o jogo pede a jogada novamente,
  sem encerrar.
- **Given** o usuário digita algo que não é um número (ex.: `abc`)
  **When** a conversão para inteiro falha
  **Then** uma mensagem de erro é exibida (sem stack trace) e o jogo pede a
  jogada novamente.

### RF-02 — Sortear a jogada do computador

- **Given** uma rodada em andamento
  **When** chega a vez do computador jogar
  **Then** uma jogada é sorteada uniformemente entre "pedra", "papel" e
  "tesoura".

### RF-03 — Determinar o vencedor da rodada

- **Given** a jogada do usuário e a jogada do computador são iguais
  **When** o vencedor é calculado
  **Then** o resultado é empate e nenhum placar é incrementado.
- **Given** a jogada do usuário vence a do computador pela regra
  (pedra > tesoura, papel > pedra, tesoura > papel)
  **When** o vencedor é calculado
  **Then** o placar do usuário é incrementado em 1 e a mensagem de vitória é
  retornada.
- **Given** a jogada do computador vence a do usuário
  **When** o vencedor é calculado
  **Then** o placar do computador é incrementado em 1 e a mensagem de derrota
  é retornada.

### RF-04 — Exibir placar e resultado

- **Given** uma nova rodada vai começar
  **When** a tela é redesenhada
  **Then** o placar acumulado (usuário x computador) é exibido, seguido do
  menu de opções.
- **Given** uma rodada acabou de terminar
  **When** a tela é redesenhada com o resultado
  **Then** a jogada de cada lado e a mensagem de resultado da última rodada
  são exibidas, além do placar e do menu.

### RF-05 — Jogar novamente ou encerrar

- **Given** uma rodada terminou
  **When** o usuário responde `0` à pergunta de replay
  **Then** uma nova rodada começa, mantendo o placar acumulado.
- **Given** uma rodada terminou
  **When** o usuário responde `1` à pergunta de replay
  **Then** o placar final é exibido e o programa termina.
- **Given** o usuário responde algo diferente de `0` ou `1`
  **When** a resposta é validada
  **Then** uma mensagem de erro é exibida e a pergunta é repetida.

### RF-06 — Limpar a tela entre rodadas

- **Given** o sistema operacional é Windows
  **When** a tela precisa ser limpa
  **Then** o comando `cls` é executado.
- **Given** o sistema operacional é Linux ou macOS
  **When** a tela precisa ser limpa
  **Then** o comando `clear` é executado.

## Requisitos não funcionais

### RNF-01 — Sem dependências externas

O jogo deve rodar com Python puro (biblioteca padrão), sem exigir
`pip install` de nenhum pacote em tempo de execução.

### RNF-02 — Portabilidade

O mesmo `main.py` deve funcionar sem alteração em Windows, Linux e macOS
(scripts de atalho separados por sistema cobrem só a conveniência de
inicialização, não a lógica do jogo).

### RNF-03 — Feedback nunca deixa o usuário travado

Nenhuma entrada inválida (número fora do intervalo, texto não numérico,
resposta de replay inesperada) pode lançar uma exceção não tratada — o jogo
sempre pede a entrada de novo.

### RNF-04 — Saída não crasha por codificação

A impressão no terminal (incluindo os emojis das mensagens de resultado) não
pode lançar `UnicodeEncodeError`, mesmo quando `stdout` não está preso a um
console UTF-8 (saída redirecionada para arquivo, pipe, ou executor de CI).

## Perguntas em aberto

Nenhuma — feature pequena e já finalizada; ver "Atividades para praticar" no
`README.md` para extensões futuras propostas (melhor-de-3, placar persistido,
efeito de suspense).

## Testes

### RF-01, RF-02, RF-03 — Lógica pura do jogo

`tests/test_main.py` cobre `determinar_vencedor` para todas as combinações
(empate, vitória do usuário, vitória do computador — parametrizado),
`realizar_jogada_usuario` com entrada válida/fora do intervalo/não numérica
(via `monkeypatch` em `input`), e `realizar_jogada_computador` com
`random.choice` mockado.

### RF-04 — Exibição

`tests/test_main.py` verifica, via `capsys`, que `exibir_placar` mostra o
placar sempre e a seção "ÚLTIMA RODADA" só quando há resultado.

### RF-05, RF-06 — Loop principal e limpeza de tela

Não têm teste automatizado direto: `main()` é um loop interativo até
`input()` sem timeout embutido, e `limpar_tela()` chama `os.system` (efeito
de terminal, não de retorno). Cobertos por verificação manual ao rodar o
jogo; `limpar_tela` é mockada nos testes acima para isolar a lógica.
