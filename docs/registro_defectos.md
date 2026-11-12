# Registro de defectos · código heredado v1.0.0

Estudiante: Jhonar David De Arco Mejia · Código: 1029860263

## DEF-01 · Peso máximo fijo en 50 kg en lugar de PMAX = 70
- **Requisito que incumple:** R1
- **Caso que lo detecta:** C08
- **Pasos para reproducir:** ejecutar `calc(70, 'urbana', 'normal', 3, None)` con el código heredado v1.0.0.
- **Resultado esperado:** $57.000
- **Resultado obtenido:** error: ValueError(peso invalido)
- **Severidad: Alta.** Rechaza envíos legítimos de entre 50 y 70 kg: se pierde el servicio completo para esos clientes.
- **Prioridad: Alta.** Bloquea ventas; la corrección es de una línea.
- **Rama de corrección:** `fix/DEF-01`

## DEF-02 · Zona inválida aceptada como si fuera urbana
- **Requisito que incumple:** R2
- **Caso que lo detecta:** C14
- **Pasos para reproducir:** ejecutar `calc(5, 'aerea', 'normal', 3, None)` con el código heredado v1.0.0.
- **Resultado esperado:** error (ValueError)
- **Resultado obtenido:** $9.000
- **Severidad: Media.** Se cotiza un envío a una zona que no existe sin avisar.
- **Prioridad: Media.** No hay pérdida directa, pero oculta errores de captura.
- **Rama de corrección:** `fix/DEF-02`

## DEF-03 · Día fuera del rango 1–7 aceptado (el día 8 cobra fin de semana)
- **Requisito que incumple:** R2
- **Caso que lo detecta:** C20
- **Pasos para reproducir:** ejecutar `calc(5, 'urbana', 'normal', 8, None)` con el código heredado v1.0.0.
- **Resultado esperado:** error (ValueError)
- **Resultado obtenido:** $11.000
- **Severidad: Media.** Un día inválido genera un cobro incorrecto o ninguna validación.
- **Prioridad: Media.** Se corrige junto con la validación de zona.
- **Rama de corrección:** `fix/DEF-03`

## DEF-04 · El sábado no recibe el recargo de fin de semana (`d > 6`)
- **Requisito que incumple:** R5
- **Caso que lo detecta:** C17
- **Pasos para reproducir:** ejecutar `calc(5, 'urbana', 'normal', 6, None)` con el código heredado v1.0.0.
- **Resultado esperado:** $11.000
- **Resultado obtenido:** $9.000
- **Severidad: Alta.** Cada sábado se cobra de menos $2.000 por envío: pérdida de ingresos recurrente.
- **Prioridad: Alta.** Afecta a todos los envíos del sábado.
- **Rama de corrección:** `fix/DEF-04`

## DEF-05 · Descuento de cliente y cupón se acumulan en lugar de aplicar solo el mayor
- **Requisito que incumple:** R6
- **Caso que lo detecta:** C31
- **Pasos para reproducir:** ejecutar `calc(4, 'urbana', 'vip', 2, 'ENVIO10')` con el código heredado v1.0.0.
- **Resultado esperado:** $7.200
- **Resultado obtenido:** $6.400
- **Severidad: Alta.** Se cobra de menos a los clientes con cupón: pérdida económica sistemática.
- **Prioridad: Alta.** Impacta el margen de todos los envíos con cupón.
- **Rama de corrección:** `fix/DEF-05`

## DEF-06 · Cupón inexistente se ignora en silencio (debe ser error)
- **Requisito que incumple:** R7
- **Caso que lo detecta:** C33
- **Pasos para reproducir:** ejecutar `calc(4, 'urbana', 'normal', 2, 'PROMO5')` con el código heredado v1.0.0.
- **Resultado esperado:** error (ValueError)
- **Resultado obtenido:** $9.000
- **Severidad: Baja.** No hay pérdida económica: el cliente simplemente no recibe un descuento inválido.
- **Prioridad: Media.** La especificación exige informar el error al usuario.
- **Rama de corrección:** `fix/DEF-06`

## DEF-07 · Redondeo trunca (`int(t/100)*100`) en lugar de redondear al más cercano
- **Requisito que incumple:** R8
- **Caso que lo detecta:** C25
- **Pasos para reproducir:** ejecutar `calc(4, 'urbana', 'frecuente', 2, None)` con el código heredado v1.0.0.
- **Resultado esperado:** $8.600
- **Resultado obtenido:** $8.500
- **Severidad: Media.** Cobra hasta $99 de menos por envío; los $50 no suben.
- **Prioridad: Alta.** Afecta a todos los envíos y se corrige fácil.
- **Rama de corrección:** `fix/DEF-07`

## Métricas de la ejecución contra el código heredado

| Métrica | Valor |
|---|---|
| Pruebas ejecutadas | 42 (41 casos de la matriz + 1 prueba del argumento `flag`) |
| Pruebas que pasan | 24 |
| Pruebas que fallan | 18 |
| % de pruebas que pasan | 57.1 % |
| Defectos por severidad | Alta: 3 · Media: 3 · Baja: 1 (total 7) |
| Líneas de `envios.py` | 42 |
| Densidad de defectos | 7 ÷ (42/100) = 16.7 defectos por cada 100 líneas |
| Cobertura de sentencias | 100.0 % |
| Cobertura de ramas | 100.0 % |

Nota: estos valores salieron de ejecutar `pytest --cov=envios --cov-branch` contra el código heredado; deben coincidir con tus capturas 01 y 02.

Casos que fallan contra el heredado: C08, C14, C17, C19, C20, C22, C24, C25, C26, C27, C28, C31, C32, C33, C34, C35, C36, C37.
