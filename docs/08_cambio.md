# Parte 8 · Solicitud de cambio y análisis de impacto

Estudiante: Jhonar David De Arco Mejia · Código: 1029860263

## Solicitud asignada

`(A + F) mod 3 = (8 + 3) mod 3 = 2`: agregar `hora` (entero de 0 a 23) y cobrar un recargo del 8 % entre las 17:00 y las 19:00, inclusive.

## Análisis de impacto

| Elemento | Impacto |
|---|---|
| Requisito nuevo | R9: validar `hora` y aplicar el 8 % durante la franja de hora pico. |
| Requisitos existentes | R4 determina la base porcentual tras el recargo de zona; R5 conserva el recargo fijo de fin de semana; R6 y R8 se ejecutan después y pueden cambiar el costo final redondeado. |
| Historias | HU-2 amplía el cálculo de recargos; HU-3 conserva descuentos y redondeo para el nuevo costo; HU-4 añade criterios específicos de hora pico. |
| Casos de prueba | Los 43 casos base usan `hora=12`, fuera de la franja, y conservan sus resultados. HP-01 a HP-13 prueban límites, validación, recargo de zona y fin de semana. |
| Código | `envios.py`: constante `RECARGO_HORA_PICO`, validación en `validar_entradas`, función `recargo_hora_pico` y nuevo parámetro obligatorio de `calc`. |
| Interfaz | La firma cambia de `calc(peso, zona, cliente, dia, cupón=None)` a `calc(peso, zona, cliente, dia, hora, cupón=None)`; las llamadas existentes deben proporcionar hora. |

## Orden de cálculo adoptado

Para que la regla sea reproducible junto con R5, el recargo de hora pico se aplica inmediatamente después del recargo de zona y antes del recargo fijo de fin de semana, descuentos, mínimo y redondeo:

> tarifa base → recargo de zona → recargo de hora pico → recargo de fin de semana → descuento → mínimo → redondeo

La solicitud exige que hora pico se calcule después de zona; se mantiene el recargo fijo de fin de semana antes de los descuentos, según E par.

## Clasificación del mantenimiento

**Adaptativo:** el sistema cambia para responder a una nueva regla del negocio (hora pico).

## Pruebas escritas primero

Se añadieron primero los casos HP-01 a HP-12. Contra la función anterior, los 12 fallaron porque `calc` no aceptaba el parámetro `hora`; los 42 casos previos seguían pasando. Después se agregó HP-13 para rechazar una hora booleana, dos casos de R2 para día no entero/booleano y pruebas para el mensaje de peso y la estrategia base. En el estado final, la regresión ejecuta 59 pruebas y todas pasan; la salida está en `docs/pytest_final.txt`.

| ID | Entrada resumida | Cálculo / resultado esperado |
|---|---|---|
| HP-01 | Urbana, hora 0 | Sin recargo → $9.000 |
| HP-02 | Urbana, hora 16 | Sin recargo → $9.000 |
| HP-03 | Urbana, hora 17 | $9.000 × 1,08 = $9.720 → $9.700 |
| HP-04 | Urbana, hora 18 | $9.000 × 1,08 = $9.720 → $9.700 |
| HP-05 | Urbana, hora 19 | $9.000 × 1,08 = $9.720 → $9.700 |
| HP-06 | Urbana, hora 20 | Sin recargo → $9.000 |
| HP-07 | Urbana, hora 23 | Hora válida, sin recargo → $9.000 |
| HP-08 | Hora -1 | `ValueError` |
| HP-09 | Hora 24 | `ValueError` |
| HP-10 | Hora 17,5 | `ValueError`; la hora debe ser entera |
| HP-11 | Rural, día hábil, hora 17 | $9.000 × 1,20 × 1,08 = $11.664 → $11.700 |
| HP-12 | Rural, sábado, hora 17 | $9.000 × 1,20 × 1,08 + $2.000 = $13.664 → $13.700 |
| HP-13 | Hora `True` | `ValueError`; un booleano no es una hora válida |

## Versión

Se publica como **3.0.0 (MAJOR)**: `hora` es un parámetro obligatorio nuevo y rompe las llamadas que usaban la firma anterior. La nueva etiqueta debe apuntar al commit integrado en `main`.
