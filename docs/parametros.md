# Mis parámetros

Estudiante: Jhonar David De Arco Mejia · Código: 1029860263

| A | B | C | D | E | F | PMAX | L1 | L2 | RR | RN | V | S | CAMBIO |
|---|---|---|---|---|---|------|----|----|----|----|---|---|--------|
| 8 | 6 | 0 | 2 | 6 | 3 | 70 | 2 | 10 | 20 % | 40 % | 20 % | $2.000 | 2 |

Reglas por paridad:
- D = 2 (par): tramo 1 incluye el límite (peso <= 2).
- E = 6 (par): recargo de fin de semana ANTES de los descuentos.
- B = 6 (par): solo se aplica el mayor entre descuento de cliente y cupón.
- F = 3 (impar): cupón inexistente es ERROR.
- Solicitud de cambio (8+3) mod 3 = 2: hora pico.
