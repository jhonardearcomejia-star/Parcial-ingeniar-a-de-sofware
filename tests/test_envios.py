"""Suite de pruebas de EnvíaYa · calc · Jhonar David De Arco Mejia (1029860263)

Parámetros: PMAX=70, L1=2 (incluido, D par), L2=10, RR=20 %, RN=40 %,
V=20 %, S=$2.000, fin de semana ANTES de descuentos (E par),
solo el MAYOR descuento entre cliente y cupón (B par),
cupón inexistente = ERROR (F impar).

Los resultados esperados se calcularon a mano a partir de la especificación
(ver docs/03_caja_negra.md), NO a partir del comportamiento del código.
"ERROR" significa que se espera ValueError.
"""
import pytest
from envios import calc

CASOS = [
    # id,   peso, zona,      cliente,  día, cupón, esperado
    ("C01", 0, 'urbana', 'normal', 3, None, 'ERROR'),
    ("C02", 0.1, 'urbana', 'normal', 3, None, 6000),
    ("C03", 2, 'urbana', 'normal', 3, None, 6000),
    ("C04", 2.01, 'urbana', 'normal', 3, None, 9000),
    ("C05", 10, 'urbana', 'normal', 3, None, 9000),
    ("C06", 10.01, 'urbana', 'normal', 3, None, 9000),
    ("C07", 15.5, 'urbana', 'normal', 3, None, 13400),
    ("C08", 70, 'urbana', 'normal', 3, None, 57000),
    ("C09", 70.01, 'urbana', 'normal', 3, None, 'ERROR'),
    ("C10", -5, 'urbana', 'normal', 3, None, 'ERROR'),
    ("C11", 5, 'urbana', 'normal', 3, None, 9000),
    ("C12", 5, 'rural', 'normal', 3, None, 10800),
    ("C13", 5, 'nacional', 'normal', 3, None, 12600),
    ("C14", 5, 'aerea', 'normal', 3, None, 'ERROR'),
    ("C15", 5, 'urbana', 'normal', 1, None, 9000),
    ("C16", 5, 'urbana', 'normal', 5, None, 9000),
    ("C17", 5, 'urbana', 'normal', 6, None, 11000),
    ("C18", 5, 'urbana', 'normal', 7, None, 11000),
    ("C19", 5, 'urbana', 'normal', 0, None, 'ERROR'),
    ("C20", 5, 'urbana', 'normal', 8, None, 'ERROR'),
    ("C21", 4, 'urbana', 'normal', 2, None, 9000),
    ("C22", 4, 'urbana', 'normal', 6, None, 11000),
    ("C23", 4, 'urbana', 'normal', 2, 'ENVIO10', 8100),
    ("C24", 4, 'urbana', 'normal', 6, 'ENVIO10', 9900),
    ("C25", 4, 'urbana', 'frecuente', 2, None, 8600),
    ("C26", 4, 'urbana', 'frecuente', 6, None, 10500),
    ("C27", 4, 'urbana', 'frecuente', 2, 'ENVIO10', 8100),
    ("C28", 4, 'urbana', 'frecuente', 6, 'ENVIO10', 9900),
    ("C29", 4, 'urbana', 'vip', 2, None, 7200),
    ("C30", 4, 'urbana', 'vip', 7, None, 8800),
    ("C31", 4, 'urbana', 'vip', 2, 'ENVIO10', 7200),
    ("C32", 4, 'urbana', 'vip', 7, 'ENVIO10', 8800),
    ("C33", 4, 'urbana', 'normal', 2, 'PROMO5', 'ERROR'),
    ("C34", 4, 'urbana', 'vip', 2, 'PROMO5', 'ERROR'),
    ("C35", 10, 'rural', 'vip', 6, 'ENVIO10', 10200),
    ("C36", 70, 'nacional', 'normal', 7, None, 81800),
    ("C37", 12.5, 'rural', 'vip', 3, None, 10600),
    ("C38", 15.5, 'nacional', 'frecuente', 4, None, 17800),
    ("C39", 1, 'urbana', 'vip', 3, None, 5000),
    ("C40", 1, 'urbana', 'vip', 2, 'ENVIO10', 5000),
    ("C41", 2, 'urbana', 'frecuente', 3, None, 5700),
]


@pytest.mark.parametrize(
    "id_, p, z, c, d, cup, esperado",
    CASOS,
    ids=[caso[0] for caso in CASOS],
)
def test_calc(id_, p, z, c, d, cup, esperado):
    if esperado == "ERROR":
        with pytest.raises(ValueError):
            calc(p, z, c, d, cup)
    else:
        assert calc(p, z, c, d, cup) == esperado


def test_flag_rechazado():
    """Verifica que calc ya no acepta el argumento flag (cambio MAJOR)."""
    with pytest.raises(TypeError):
        calc(4, "urbana", "normal", 2, None, flag=True)