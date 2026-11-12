# envios.py
# Código evolucionado · versión 3.0.0


# Constantes con nombre (reemplazo de números mágicos)
PESO_MAXIMO = 70
LIMITE_TRAMO_1 = 2
LIMITE_TRAMO_2 = 10
TARIFA_TRAMO_1 = 6_000
TARIFA_TRAMO_2 = 9_000
PRECIO_KG_EXTRA = 800
RECARGO_RURAL = 0.20
RECARGO_NACIONAL = 0.40
RECARGO_HORA_PICO = 0.08
RECARGO_FIN_DE_SEMANA = 2_000
DESCUENTO_FRECUENTE = 0.05
DESCUENTO_VIP = 0.20
DESCUENTO_CUPON = 0.10
COSTO_MINIMO = 5_000
MULTIPLO_REDONDEO = 100


# Estrategia: patrones de recargo por zona
class RecargoZona:
    """Clase base abstracta para recargos por zona."""

    def aplicar(self, tarifa: float) -> float:
        raise NotImplementedError("Subclases deben implementar este método")


class ZonaUrbana(RecargoZona):
    def aplicar(self, tarifa: float) -> float:
        return tarifa


class ZonaRural(RecargoZona):
    def aplicar(self, tarifa: float) -> float:
        return tarifa + tarifa * RECARGO_RURAL


class ZonaNacional(RecargoZona):
    def aplicar(self, tarifa: float) -> float:
        return tarifa + tarifa * RECARGO_NACIONAL


# Diccionario de estrategias por zona
ZONAS: dict[str, RecargoZona] = {
    "urbana": ZonaUrbana(),
    "rural": ZonaRural(),
    "nacional": ZonaNacional(),
}


def validar_entradas(
    peso: float,
    zona: str,
    cliente: str,
    dia: int,
    hora: int,
    cupón: str | None,
) -> None:
    """Validar entradas según reglas R1, R2, R7 y R9.

    R1: 0 < peso <= PESO_MAXIMO, si no, ValueError("peso inválido").
    R2: zona debe ser urbana/rural/nacional y día entero entre 1 y 7.
    R7: cupón distinto de None y ENVIO10 -> ValueError("cupon invalido").
    R9: hora debe ser un entero entre 0 y 23.
    """
    if peso <= 0 or peso > PESO_MAXIMO:
        raise ValueError("peso inválido")
    if zona not in ("urbana", "rural", "nacional"):
        raise ValueError("zona inválida")
    validar_dia(dia)
    validar_hora(hora)
    if cupón is not None and cupón != "ENVIO10":
        raise ValueError("cupon invalido")


def validar_dia(dia: int) -> None:
    """R2: aceptar únicamente días enteros del 1 al 7."""
    if isinstance(dia, bool) or not isinstance(dia, int):
        raise ValueError("día inválido")
    if not 1 <= dia <= 7:
        raise ValueError("día inválido")


def validar_hora(hora: int) -> None:
    """R9: aceptar únicamente horas enteras del 0 al 23."""
    if isinstance(hora, bool) or not isinstance(hora, int) or not 0 <= hora <= 23:
        raise ValueError("hora inválida")


def tarifa_base(peso: float) -> float:
    """Regla R3: calcular tarifa base por tramos de peso.

    - peso <= LIMITE_TRAMO_1: TARIFA_TRAMO_1
    - LIMITE_TRAMO_1 < peso <= LIMITE_TRAMO_2: TARIFA_TRAMO_2
    - peso > LIMITE_TRAMO_2: TARIFA_TRAMO_2 + (peso - LIMITE_TRAMO_2) * PRECIO_KG_EXTRA
    """
    if peso <= LIMITE_TRAMO_1:
        return TARIFA_TRAMO_1
    elif peso <= LIMITE_TRAMO_2:
        return TARIFA_TRAMO_2
    else:
        return TARIFA_TRAMO_2 + (peso - LIMITE_TRAMO_2) * PRECIO_KG_EXTRA


def recargo_fin_de_semana(dia: int, tarifa: float) -> float:
    """Regla R5: agregar recargo de fin de semana.

    Si dia es 6 (sábado) o 7 (domingo): +RECARGO_FIN_DE_SEMANA.
    El recargo va ANTES de los descuentos cuando E es par (E=6 es par).
    """
    if dia >= 6:  # sábado (6) o domingo (7)
        return tarifa + RECARGO_FIN_DE_SEMANA
    return tarifa


def recargo_hora_pico(hora: int, tarifa: float) -> float:
    """Regla R9: aplicar 8 % entre las 17:00 y las 19:00, inclusive."""
    if 17 <= hora <= 19:
        return tarifa + tarifa * RECARGO_HORA_PICO
    return tarifa


def descuento_aplicable(
    cliente: str, cupón: str | None
) -> float:
    """Regla R6: aplicar el mayor descuento entre cliente y cupón.

    - Si cliente es 'frecuente': DESCUENTO_FRECUENTE (5%)
    - Si cliente es 'vip': DESCUENTO_VIP (20%)
    - Si cupón es 'ENVIO10': DESCUENTO_CUPON (10%)
    - Solo se aplica el MAYOR de los dos (no se acumulan)
    """
    desc_cliente = 0.0
    if cliente == "frecuente":
        desc_cliente = DESCUENTO_FRECUENTE
    elif cliente == "vip":
        desc_cliente = DESCUENTO_VIP

    desc_cupon = 0.0
    if cupón == "ENVIO10":
        desc_cupon = DESCUENTO_CUPON

    return max(desc_cliente, desc_cupon)


def redondear(tarifa: float) -> int:
    """Regla R8: redondear al múltiplo de $100 más cercano.

    Los $50 redondean hacia arriba.
    Ejemplo: 8.550 -> 8.600, 7.200 -> 7.200, 10.240 -> 10.200

    Se usa: tarifa + 50 // 100 * 100 para que los exactamente $50
    roten hacia arriba (8550 -> 8600, 8450 -> 8500).
    """
    return int((tarifa + MULTIPLO_REDONDEO // 2) // MULTIPLO_REDONDEO * MULTIPLO_REDONDEO)


def calc(
    peso: float,
    zona: str,
    cliente: str,
    dia: int,
    hora: int,
    cupón: str | None = None,
) -> int:
    """Calcular el costo de un envío.

    Función principal que orquesta las funciones validadoras y
    de cálculo para aplicar las reglas R1-R9.

    Parámetros:
        peso: en kg (puede tener decimales)
        zona: urbana, rural o nacional
        cliente: normal, frecuente o vip
        dia: de 1 a 7 (6=sábado, 7=domingo)
        hora: entero de 0 a 23
        cupón: opcional, solo "ENVIO10" es válido

    Retorna:
        Costo final redondeado al múltiplo de $100 más cercano,
        con un mínimo de $5.000.
    """
    # 1. Validar entradas
    validar_entradas(peso, zona, cliente, dia, hora, cupón)

    # 2. Tarifa base
    t = tarifa_base(peso)

    # 3. Recargo de zona
    estrategia = ZONAS[zona]
    t = estrategia.aplicar(t)

    # 4. Hora pico: se calcula después del recargo de zona.
    t = recargo_hora_pico(hora, t)

    # 5. Recargo de fin de semana (antes de descuentos al E par)
    t = recargo_fin_de_semana(dia, t)

    # 6. Descuento de cliente y cupón (solo el mayor)
    desc = descuento_aplicable(cliente, cupón)
    t = t - t * desc

    # 7. Mínimo $5.000
    if t < COSTO_MINIMO:
        t = COSTO_MINIMO

    # 8. Redondeo final
    return redondear(t)
