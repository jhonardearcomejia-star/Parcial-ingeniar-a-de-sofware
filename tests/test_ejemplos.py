"""Casos de EJEMPLO calculados a mano (modelo de formato).

Tu entrega debe tener tus propios 20+ casos (Parte 3), con técnica y
cálculo paso a paso. Crea tu suite en tests/test_envios.py (rama test/suite).
Parámetros: PMAX=70, L1=2 (incluido), L2=10, RR=20 %, RN=40 %, V=20 %, S=2000.
"""
import pytest
from envios import calc


@pytest.mark.parametrize(
    "p, z, c, d, cup, esperado",
    [
        (2, "urbana", "normal", 3, None, 6000),         # límite L1 incluido
        (12.5, "rural", "vip", 3, None, 10600),         # redondeo: 10.560 -> 10.600
        (5, "urbana", "normal", 6, None, 11000),        # sábado = fin de semana
        (5, "urbana", "vip", 2, "ENVIO10", 7200),       # solo el mayor descuento
        (10, "rural", "vip", 6, "ENVIO10", 10200),      # recargo antes + mayor
        (70, "nacional", "normal", 7, None, 81800),     # PMAX = 70
    ],
)
def test_resultado_esperado(p, z, c, d, cup, esperado):
    assert calc(p, z, c, d, cup) == esperado


def test_cupon_inexistente_es_error():
    with pytest.raises(ValueError):
        calc(3, "urbana", "normal", 1, "PROMO5")
