"""Suite de pruebas de EnvíaYa · calc · Jhonar David De Arco Mejia (1029860263)

Parámetros: PMAX=70, L1=2 (incluido, D par), L2=10, RR=20 %, RN=40 %,
V=20 %, S=$2.000, fin de semana ANTES de descuentos (E par),
solo el MAYOR descuento entre cliente y cupón (B par),
cupón inexistente = ERROR (F impar).

Los resultados esperados se calcularon a mano a partir de la especificación
(ver docs/03_caja_negra.md y docs/08_cambio.md), NO a partir del comportamiento del código.
"ERROR" significa que se espera ValueError.
Los 43 casos base usan hora=12 para mantener su resultado original.
"""
import pytest
from envios import RecargoZona, calc

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
    ("C42", 5, 'urbana', 'normal', 6.5, None, 'ERROR'),
    ("C43", 5, 'urbana', 'normal', True, None, 'ERROR'),
]


@pytest.mark.parametrize(
    "id_, p, z, c, d, cup, esperado",
    CASOS,
    ids=[caso[0] for caso in CASOS],
)
def test_calc(id_, p, z, c, d, cup, esperado):
    if esperado == "ERROR":
        with pytest.raises(ValueError):
            calc(p, z, c, d, 12, cup)
    else:
        assert calc(p, z, c, d, 12, cup) == esperado


def test_flag_rechazado():
    """Verifica que calc ya no acepta el argumento flag (cambio MAJOR)."""
    with pytest.raises(TypeError):
        calc(4, "urbana", "normal", 2, 12, None, flag=True)


def test_error_peso_usa_el_mensaje_especificado():
    with pytest.raises(ValueError, match="^peso inválido$"):
        calc(0, "urbana", "normal", 3, 12)


def test_estrategia_base_exige_una_implementacion():
    with pytest.raises(NotImplementedError):
        RecargoZona().aplicar(9000)


@pytest.mark.parametrize(
    "hora, esperado",
    [
        (0, 9000),
        (16, 9000),
        (17, 9700),
        (18, 9700),
        (19, 9700),
        (20, 9000),
        (23, 9000),
    ],
    ids=["HP-01", "HP-02", "HP-03", "HP-04", "HP-05", "HP-06", "HP-07"],
)
def test_recargo_hora_pico_en_limites(hora, esperado):
    """El 8 % aplica solo entre 17 y 19, inclusive."""
    assert calc(4, "urbana", "normal", 3, hora=hora) == esperado


@pytest.mark.parametrize(
    "hora", [-1, 24, 17.5, True], ids=["HP-08", "HP-09", "HP-10", "HP-13"]
)
def test_hora_fuera_de_rango_o_no_entera_es_invalida(hora):
    with pytest.raises(ValueError):
        calc(4, "urbana", "normal", 3, hora=hora)


def test_HP_11_hora_pico_se_calcula_despues_del_recargo_de_zona():
    # $9.000 × 1,20 × 1,08 = $11.664 → $11.700
    assert calc(4, "rural", "normal", 3, hora=17) == 11700


def test_HP_12_hora_pico_va_antes_del_recargo_fijo_de_fin_de_semana():
    # ($9.000 × 1,20 × 1,08) + $2.000 = $13.664 → $13.700
    assert calc(4, "rural", "normal", 6, hora=17) == 13700
