from envios import calc


def r(*args):
    try:
        return calc(*args)
    except ValueError as e:
        return f"ValueError({e})"


DEFECTOS = [
    ("DEF-01", (70, "urbana", "normal", 3), "57000"),
    ("DEF-02", (5, "aerea", "normal", 3), "error"),
    ("DEF-03", (5, "urbana", "normal", 8), "error"),
    ("DEF-04", (5, "urbana", "normal", 6), "11000"),
    ("DEF-05", (4, "urbana", "vip", 2, "ENVIO10"), "7200"),
    ("DEF-06", (4, "urbana", "normal", 2, "PROMO5"), "error"),
    ("DEF-07", (4, "urbana", "frecuente", 2), "8600"),
]

for nombre, args, esperado in DEFECTOS:
    print(f"{nombre} | esperado: {esperado:>6} | obtenido: {r(*args)}")
