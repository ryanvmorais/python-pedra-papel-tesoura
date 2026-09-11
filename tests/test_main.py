"""Testes para main.py.

Estratégia de isolamento: `limpar_tela` é sempre mockada (chama `os.system`,
efeito de terminal irrelevante para a lógica testada). `input()` é mockado via
`monkeypatch.setattr("builtins.input", ...)` para simular a digitação do
usuário sem bloquear a suíte. `random.choice` é mockado quando o teste precisa
de uma jogada determinística do computador.
"""

from __future__ import annotations

import random
from collections.abc import Iterator

import pytest

from main import PedraPapelTesoura

pytestmark = pytest.mark.usefixtures("_sem_tela")


@pytest.fixture
def _sem_tela(monkeypatch: pytest.MonkeyPatch) -> None:
    """Substitui a limpeza de tela por um no-op em toda a suíte."""
    monkeypatch.setattr(PedraPapelTesoura, "limpar_tela", lambda self: None)


@pytest.fixture
def jogo() -> PedraPapelTesoura:
    """Retorna:
    PedraPapelTesoura: Instância nova, com placar zerado.
    """
    return PedraPapelTesoura()


def _digitar(monkeypatch: pytest.MonkeyPatch, *respostas: str) -> Iterator[str]:
    """Simula uma sequência de respostas do usuário no `input()`.

    Args:
        monkeypatch (pytest.MonkeyPatch): Fixture de monkeypatch do teste.
        *respostas (str): Respostas a devolver, uma por chamada de `input()`.

    Returns:
        Iterator[str]: O iterador usado internamente (raramente precisa ser
            inspecionado pelo teste).
    """
    valores = iter(respostas)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(valores))
    return valores


# ---------------------------------------------------------------------------
# __init__
# ---------------------------------------------------------------------------


def test_init_comeca_com_placar_zerado(jogo: PedraPapelTesoura) -> None:
    assert jogo.pontos_usuario == 0
    assert jogo.pontos_computador == 0
    assert jogo.opcoes == ["pedra", "papel", "tesoura"]


# ---------------------------------------------------------------------------
# realizar_jogada_usuario
# ---------------------------------------------------------------------------


def test_realizar_jogada_usuario_aceita_entrada_valida(
    jogo: PedraPapelTesoura, monkeypatch: pytest.MonkeyPatch
) -> None:
    _digitar(monkeypatch, "1")
    jogo.realizar_jogada_usuario()
    assert jogo.jogada_usuario == "papel"


def test_realizar_jogada_usuario_repete_apos_numero_fora_do_intervalo(
    jogo: PedraPapelTesoura, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Entrada fora de 0-2 não deve travar: o loop pede de novo até validar."""
    _digitar(monkeypatch, "5", "0")
    jogo.realizar_jogada_usuario()
    assert jogo.jogada_usuario == "pedra"


def test_realizar_jogada_usuario_repete_apos_entrada_nao_numerica(
    jogo: PedraPapelTesoura, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Letra digitada no lugar do número não deve travar (ValueError tratado)."""
    _digitar(monkeypatch, "abc", "2")
    jogo.realizar_jogada_usuario()
    assert jogo.jogada_usuario == "tesoura"


# ---------------------------------------------------------------------------
# realizar_jogada_computador
# ---------------------------------------------------------------------------


def test_realizar_jogada_computador_sorteia_entre_as_opcoes(
    jogo: PedraPapelTesoura, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(random, "choice", lambda _opcoes: "tesoura")
    jogo.realizar_jogada_computador()
    assert jogo.jogada_computador == "tesoura"


# ---------------------------------------------------------------------------
# determinar_vencedor
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("jogada", ["pedra", "papel", "tesoura"])
def test_determinar_vencedor_empate(jogo: PedraPapelTesoura, jogada: str) -> None:
    jogo.jogada_usuario = jogada
    jogo.jogada_computador = jogada

    resultado = jogo.determinar_vencedor()

    assert "EMPATE" in resultado
    assert jogo.pontos_usuario == 0
    assert jogo.pontos_computador == 0


@pytest.mark.parametrize(
    ("jogada_usuario", "jogada_computador"),
    [("pedra", "tesoura"), ("papel", "pedra"), ("tesoura", "papel")],
)
def test_determinar_vencedor_usuario_vence(
    jogo: PedraPapelTesoura, jogada_usuario: str, jogada_computador: str
) -> None:
    jogo.jogada_usuario = jogada_usuario
    jogo.jogada_computador = jogada_computador

    resultado = jogo.determinar_vencedor()

    assert "VOCÊ VENCEU" in resultado
    assert jogo.pontos_usuario == 1
    assert jogo.pontos_computador == 0


@pytest.mark.parametrize(
    ("jogada_usuario", "jogada_computador"),
    [("tesoura", "pedra"), ("pedra", "papel"), ("papel", "tesoura")],
)
def test_determinar_vencedor_computador_vence(
    jogo: PedraPapelTesoura, jogada_usuario: str, jogada_computador: str
) -> None:
    jogo.jogada_usuario = jogada_usuario
    jogo.jogada_computador = jogada_computador

    resultado = jogo.determinar_vencedor()

    assert "COMPUTADOR VENCEU" in resultado
    assert jogo.pontos_usuario == 0
    assert jogo.pontos_computador == 1


def test_determinar_vencedor_acumula_placar_entre_rodadas(
    jogo: PedraPapelTesoura,
) -> None:
    """O placar não deve zerar entre rodadas — só a instância nova zera."""
    jogo.jogada_usuario = "pedra"
    jogo.jogada_computador = "tesoura"
    jogo.determinar_vencedor()

    jogo.jogada_usuario = "papel"
    jogo.jogada_computador = "tesoura"
    jogo.determinar_vencedor()

    assert jogo.pontos_usuario == 1
    assert jogo.pontos_computador == 1


# ---------------------------------------------------------------------------
# exibir_placar
# ---------------------------------------------------------------------------


def test_exibir_placar_sem_resultado_nao_mostra_ultima_rodada(
    jogo: PedraPapelTesoura, capsys: pytest.CaptureFixture[str]
) -> None:
    jogo.exibir_placar()

    saida = capsys.readouterr().out
    assert "PLACAR" in saida
    assert "ÚLTIMA RODADA" not in saida


def test_exibir_placar_com_resultado_mostra_as_jogadas(
    jogo: PedraPapelTesoura, capsys: pytest.CaptureFixture[str]
) -> None:
    jogo.jogada_usuario = "pedra"
    jogo.jogada_computador = "tesoura"

    jogo.exibir_placar("🎉 VOCÊ VENCEU A RODADA!")

    saida = capsys.readouterr().out
    assert "ÚLTIMA RODADA" in saida
    assert "PEDRA" in saida
    assert "TESOURA" in saida
