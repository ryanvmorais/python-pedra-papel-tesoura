---
feature: Jogo de Pedra, Papel e Tesoura (Jokenpô) via terminal
status: concluído
data: 2026-09-11
relacionado:
  - 001-jogo-pedra-papel-tesoura/requirements.md
origem: engenharia reversa
---

# 001 — Jogo de Pedra, Papel e Tesoura — design

## Visão geral da abordagem

Um único módulo (`main.py`) com uma classe (`PedraPapelTesoura`) que guarda o
estado de uma sessão de jogo (placar acumulado e jogadas da rodada atual) e
expõe um método por responsabilidade (limpar tela, exibir placar, ler jogada
do usuário, sortear jogada do computador, determinar vencedor). Uma função
`main()` no nível do módulo orquestra o loop de rodadas e o prompt de replay,
e é o único ponto que lê/imprime diretamente no terminal fora da classe.

Não há camadas (persistência, rede, UI gráfica) — é intencional: o projeto
é didático e o objetivo é que o fluxo caiba na cabeça em uma leitura.

## Layout de módulos

```
main.py            # classe do jogo + função main() (ponto de entrada)
tests/test_main.py # suíte pytest
```

## Modelo de dados

`PedraPapelTesoura` (não é um dataclass/pydantic — é um objeto com estado
mutável, o ponto pedagógico central da POO nesta spec):

- `opcoes: list[str]` — `["pedra", "papel", "tesoura"]`, fixo por instância.
- `pontos_usuario: int` / `pontos_computador: int` — placar acumulado.
- `jogada_usuario: str` / `jogada_computador: str` — jogadas da rodada atual,
  sobrescritas a cada rodada.

Constante de módulo `REGRAS_VITORIA: dict[str, str]` — mapeia cada jogada
para a jogada que ela vence (`"pedra" -> "tesoura"`, `"papel" -> "pedra"`,
`"tesoura" -> "papel"`).

## Componentes

### `PedraPapelTesoura.limpar_tela`

Detecta o SO via `os.name` (`"nt"` = Windows) e roda `cls`/`clear` via
`os.system`. Efeito de terminal, sem retorno.

### `PedraPapelTesoura.exibir_placar`

Redesenha a tela: limpa, imprime o placar, e — se recebeu uma mensagem de
resultado — imprime as jogadas da rodada anterior e o resultado. Sempre
termina imprimindo o menu de opções.

### `PedraPapelTesoura.realizar_jogada_usuario`

Loop de leitura: pede um número, converte para `int`, valida o intervalo
0-2. Repete em caso de `ValueError` (entrada não numérica) ou número fora do
intervalo — nunca deixa uma exceção subir.

### `PedraPapelTesoura.realizar_jogada_computador`

`random.choice(self.opcoes)` — um sorteio uniforme, sem peso.

### `PedraPapelTesoura.determinar_vencedor`

Compara `jogada_usuario` com `jogada_computador`: iguais é empate; senão,
consulta `REGRAS_VITORIA[jogada_usuario]` — se bater com a jogada do
computador, o usuário venceu, senão o computador venceu. Incrementa o placar
do lado vencedor e retorna a mensagem correspondente.

### `main()`

Loop externo (uma rodada por iteração): mostra o placar, lê a jogada do
usuário, sorteia a do computador, determina o vencedor, redesenha a tela com
o resultado. Loop interno: pergunta se quer jogar de novo (`0`/`1`),
validando a resposta antes de decidir entre continuar ou encerrar.

## Interfaces

Nenhuma — programa de terminal sem rede, arquivo ou API. A única "interface"
é o protocolo de entrada/saída via `input()`/`print()`, documentado nos
requisitos funcionais.

## ADRs

### ADR-1 — `os.system` em vez de `subprocess.run(..., shell=True)`

**Decisão.** `limpar_tela` usa `os.system(comando)` com uma string fixa
(`"cls"` ou `"clear"`).

**Alternativas.** (a) `subprocess.run(comando, shell=True)` — a versão
original antes desta modernização. (b) uma lib de terceiros (`colorama`,
`rich`) com função de limpar tela embutida.

**Porquê.** `comando` nunca é entrada do usuário — é sempre um literal fixo
escolhido por `os.name`. `os.system` faz exatamente o mesmo com uma linha
mais simples e sem o `shell=True` que ferramentas de análise estática
sinalizam por hábito (mesmo sem risco real aqui, o sinal de alerta some).
Descartar (b): manter zero dependência de runtime é um objetivo explícito
(RNF-01).

**Trade-off.** `os.system` é levemente menos flexível que `subprocess`
(não captura stdout/stderr) — irrelevante aqui, pois o efeito desejado é só
o side-effect no terminal.

### ADR-2 — Extrair `main()` em vez de código solto em `if __name__ == "__main__"`

**Decisão.** O loop do jogo vive numa função `main()`, chamada pelo guard
`if __name__ == "__main__"`.

**Alternativas.** (a) manter o loop diretamente no bloco do guard (como
estava antes da modernização).

**Porquê.** Uma função nomeada é importável e documentável (docstring); o
guard vira uma linha só. Não muda o comportamento em nada.

**Trade-off.** Nenhum relevante — é reorganização pura.

### ADR-3 — `REGRAS_VITORIA` como constante de módulo, não recriada por chamada

**Decisão.** O dicionário de regras de vitória subiu de dentro de
`determinar_vencedor` para uma constante de módulo (`REGRAS_VITORIA`).

**Alternativas.** (a) manter o dicionário local à função (como estava).

**Porquê.** O dicionário é fixo e nunca muda entre chamadas — recriá-lo a
cada rodada é trabalho redundante, e como constante de módulo o valor da
regra fica visível/documentável fora do método que o usa (útil para quem lê
o arquivo de cima para baixo, incluindo em `docs/stack.md` e nesta spec).

**Trade-off.** Nenhum relevante — dicionário pequeno e imutável na prática
(nada no código escreve nele depois de definido).

### ADR-4 — Reconfigurar `sys.stdout` para UTF-8 no import

**Decisão.** `main.py` chama `sys.stdout.reconfigure(encoding="utf-8",
errors="replace")` no nível do módulo, se o atributo existir.

**Alternativas.** (a) não fazer nada (comportamento original). (b) remover os
emojis das mensagens.

**Porquê.** No Windows, quando `stdout` não está preso a um console UTF-8
(saída redirecionada para arquivo, pipe, ou alguns executores de CI), o
Python cai para a codepage do sistema (`cp1252`) e todo `print()` com emoji
lança `UnicodeEncodeError` — confirmado ao rodar `main.py` com a entrada via
pipe durante esta modernização. Descartar (a): é a causa raiz do crash.
Descartar (b): os emojis são parte da voz didática/calorosa do projeto
(RF-04); removê-los é perda maior que o custo de uma linha de configuração.

**Trade-off.** `errors="replace"` troca um caractere não suportado por `?`
em vez de crashar — aceitável, pois a única saída que perderia fidelidade é
um terminal exótico que também não suporta UTF-8.

## Impacto no código existente

Esta spec documenta a versão já modernizada de `main.py` (type hints, `uv`,
suíte de testes). Não há código legado para migrar — é a spec fundadora do
projeto.

## Estratégia de testes

Unitária, sem integração (não há rede nem arquivo). `limpar_tela` é sempre
mockada nos testes (evita side-effect de terminal); `input()` é mockado via
`monkeypatch.setattr("builtins.input", ...)` para simular sequências de
digitação, inclusive as inválidas que o loop de validação precisa absorver;
`random.choice` é mockado quando o teste precisa de uma jogada determinística
do computador. Ver `tests/test_main.py` e a seção "Testes" de
`requirements.md`.
