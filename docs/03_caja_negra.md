# Parte 3 · Diseño de casos de caja negra

Estudiante: Jhonar David De Arco Mejia · Código: 1029860263

Parámetros: PMAX=70 · L1=2 (incluido) · L2=10 · RR=20 % · RN=40 % · V=20 % · S=$2.000
Reglas: D par (peso ≤ 2) · E par (recargo de fin de semana ANTES de descuentos) ·
B par (solo el mayor descuento) · F impar (cupón inexistente = error).

Orden de cálculo usado para todos los resultados esperados:

> tarifa base → recargo de zona → +$2.000 si es sábado o domingo → descuento (el mayor entre cliente y cupón) → mínimo $5.000 → redondeo a $100 ($50 sube)

## 1. Particiones de equivalencia

| Entrada | Clases válidas | Clases inválidas |
|---|---|---|
| Peso (kg) | V1: 0 < p ≤ 2 (tramo 1) · V2: 2 < p ≤ 10 (tramo 2) · V3: 10 < p ≤ 70 (tramo 3) | I1: p ≤ 0 · I2: p > 70 |
| Zona | V4: urbana · V5: rural · V6: nacional | I3: cualquier otra ("aerea") |
| Cliente | V7: normal · V8: frecuente · V9: vip | (la especificación no define clientes inválidos; se anota como ambigüedad) |
| Día | V10: enteros 1–5 (hábil) · V11: 6 (sábado) · V12: 7 (domingo) | I4: d < 1 · I5: d > 7 · I6: día fraccionario o booleano |
| Cupón | V13: ninguno · V14: ENVIO10 | I7: cupón inexistente ("PROMO5") |

## 2. Valores límite del peso

Con D = 2 (par) el límite L1 está **incluido**: 2 kg pertenece al tramo 1.

| Frontera | Valores probados | Casos |
|---|---|---|
| 0 | 0 (inválido) · 0,1 (válido) | C01, C02 |
| L1 = 2 | 2 (tramo 1) · 2,01 (tramo 2) | C03, C04 |
| L2 = 10 | 10 (tramo 2) · 10,01 (tramo 3) | C05, C06 |
| PMAX = 70 | 70 (válido) · 70,01 (inválido) | C08, C09 |

También se prueban los límites del día (0, 1, 5, 6, 7, 8), los tipos inválidos del día (6,5 y `True`) y el costo mínimo ($5.000).

## 3. Tabla de decisión: cliente × cupón × fin de semana

Con B par se aplica solo el mayor descuento; con E par el recargo de fin de semana se suma antes del descuento.
Ejemplo: paquete de 4 kg a zona urbana (tarifa base $9.000).

| Regla | Cliente | Cupón | Fin de semana | Descuento efectivo | Resultado | Caso |
|---|---|---|---|---|---|---|
| 1 | normal | ninguno | no | 0 % | $9.000 | C21 |
| 2 | normal | ninguno | sí | 0 % | $11.000 | C22 |
| 3 | normal | ENVIO10 | no | 10 % | $8.100 | C23 |
| 4 | normal | ENVIO10 | sí | 10 % | $9.900 | C24 |
| 5 | frecuente | ninguno | no | 5 % | $8.600 | C25 |
| 6 | frecuente | ninguno | sí | 5 % | $10.500 | C26 |
| 7 | frecuente | ENVIO10 | no | 10 % | $8.100 | C27 |
| 8 | frecuente | ENVIO10 | sí | 10 % | $9.900 | C28 |
| 9 | vip | ninguno | no | 20 % | $7.200 | C29 |
| 10 | vip | ninguno | sí | 20 % | $8.800 | C30 |
| 11 | vip | ENVIO10 | no | 20 % | $7.200 | C31 |
| 12 | vip | ENVIO10 | sí | 20 % | $8.800 | C32 |

## 4. Matriz de casos de prueba

| ID | Requisito | Entradas | Resultado esperado (a mano) | Técnica |
|---|---|---|---|---|
| C01 | R1 | 0 kg · urbana · normal · día 3 · sin cupón | error (ValueError) | VL |
| C02 | R3 | 0,1 kg · urbana · normal · día 3 · sin cupón | $6.000 | VL |
| C03 | R3 | 2 kg · urbana · normal · día 3 · sin cupón | $6.000 | VL (L1 incluido, D par) |
| C04 | R3 | 2,01 kg · urbana · normal · día 3 · sin cupón | $9.000 | VL |
| C05 | R3 | 10 kg · urbana · normal · día 3 · sin cupón | $9.000 | VL (L2 inclusive) |
| C06 | R3, R8 | 10,01 kg · urbana · normal · día 3 · sin cupón | $9.000 | VL |
| C07 | R3 | 15,5 kg · urbana · normal · día 3 · sin cupón | $13.400 | PE (>L2) |
| C08 | R1, R3 | 70 kg · urbana · normal · día 3 · sin cupón | $57.000 | VL (PMAX) |
| C09 | R1 | 70,01 kg · urbana · normal · día 3 · sin cupón | error (ValueError) | VL |
| C10 | R1 | -5 kg · urbana · normal · día 3 · sin cupón | error (ValueError) | PE inválida |
| C11 | R4 | 5 kg · urbana · normal · día 3 · sin cupón | $9.000 | PE zona |
| C12 | R4 | 5 kg · rural · normal · día 3 · sin cupón | $10.800 | PE zona |
| C13 | R4 | 5 kg · nacional · normal · día 3 · sin cupón | $12.600 | PE zona |
| C14 | R2 | 5 kg · aerea · normal · día 3 · sin cupón | error (ValueError) | PE inválida |
| C15 | R5 | 5 kg · urbana · normal · día 1 · sin cupón | $9.000 | PE día |
| C16 | R5 | 5 kg · urbana · normal · día 5 · sin cupón | $9.000 | VL día |
| C17 | R5 | 5 kg · urbana · normal · día 6 · sin cupón | $11.000 | VL día |
| C18 | R5 | 5 kg · urbana · normal · día 7 · sin cupón | $11.000 | VL día |
| C19 | R2 | 5 kg · urbana · normal · día 0 · sin cupón | error (ValueError) | VL día |
| C20 | R2 | 5 kg · urbana · normal · día 8 · sin cupón | error (ValueError) | VL día |
| C21 | R6 | 4 kg · urbana · normal · día 2 · sin cupón | $9.000 | TD regla 1 |
| C22 | R5, R6 | 4 kg · urbana · normal · día 6 · sin cupón | $11.000 | TD regla 2 |
| C23 | R6 | 4 kg · urbana · normal · día 2 · ENVIO10 | $8.100 | TD regla 3 |
| C24 | R5, R6 | 4 kg · urbana · normal · día 6 · ENVIO10 | $9.900 | TD regla 4 |
| C25 | R6, R8 | 4 kg · urbana · frecuente · día 2 · sin cupón | $8.600 | TD regla 5 |
| C26 | R5, R6, R8 | 4 kg · urbana · frecuente · día 6 · sin cupón | $10.500 | TD regla 6 |
| C27 | R6 | 4 kg · urbana · frecuente · día 2 · ENVIO10 | $8.100 | TD regla 7 |
| C28 | R5, R6 | 4 kg · urbana · frecuente · día 6 · ENVIO10 | $9.900 | TD regla 8 |
| C29 | R6 | 4 kg · urbana · vip · día 2 · sin cupón | $7.200 | TD regla 9 |
| C30 | R5, R6 | 4 kg · urbana · vip · día 7 · sin cupón | $8.800 | TD regla 10 |
| C31 | R6 | 4 kg · urbana · vip · día 2 · ENVIO10 | $7.200 | TD regla 11 |
| C32 | R5, R6 | 4 kg · urbana · vip · día 7 · ENVIO10 | $8.800 | TD regla 12 |
| C33 | R7 | 4 kg · urbana · normal · día 2 · PROMO5 | error (ValueError) | PE inválida |
| C34 | R7 | 4 kg · urbana · vip · día 2 · PROMO5 | error (ValueError) | PE inválida |
| C35 | R3, R4, R5, R6, R8 | 10 kg · rural · vip · día 6 · ENVIO10 | $10.200 | Combinación |
| C36 | R1, R3, R4, R5 | 70 kg · nacional · normal · día 7 · sin cupón | $81.800 | Combinación |
| C37 | R3, R4, R6, R8 | 12,5 kg · rural · vip · día 3 · sin cupón | $10.600 | Combinación |
| C38 | R3, R4, R6, R8 | 15,5 kg · nacional · frecuente · día 4 · sin cupón | $17.800 | Combinación |
| C39 | R8 | 1 kg · urbana · vip · día 3 · sin cupón | $5.000 | VL costo mínimo |
| C40 | R6, R8 | 1 kg · urbana · vip · día 2 · ENVIO10 | $5.000 | VL costo mínimo |
| C41 | R6, R8 | 2 kg · urbana · frecuente · día 3 · sin cupón | $5.700 | VL costo mínimo |
| C42 | R2 | 5 kg · urbana · normal · día 6,5 · sin cupón | error (ValueError: día inválido) | PE: tipo inválido |
| C43 | R2 | 5 kg · urbana · normal · día `True` · sin cupón | error (ValueError: día inválido) | PE: tipo inválido |

Total: 43 casos. Técnicas: PE = partición de equivalencia, VL = valor límite, TD = tabla de decisión.

## 5. Cálculo paso a paso de casos representativos

### C06 · 10,01 kg · urbana · normal · día 3 · sin cupón
1. Tramo: 10,01 > L2 = 10 → 9.000 + (10,01 − 10) × 800 = 9.008.
2. Zona urbana: sin recargo → 9.008.
3. Día 3 (hábil): sin recargo de fin de semana.
4. Cliente normal sin cupón: sin descuento.
5. Mayor que $5.000. Redondeo a $100: 9.008 está más cerca de 9.000 → **$9.000**.

### C25 · 4 kg · urbana · frecuente · día 2 · sin cupón
1. Tramo: 4 > L1 = 2 y ≤ L2 = 10 → $9.000.
2. Zona urbana: sin recargo → 9.000.
3. Día 2: sin recargo de fin de semana.
4. Cliente frecuente: 5 % → 9.000 × 0,95 = 8.550.
5. Mayor que $5.000. Redondeo: 8.550 queda exactamente en $50, sube → **$8.600**.

### C32 · 4 kg · urbana · vip · día 7 · ENVIO10
1. Tramo: 4 kg → tramo 2 → $9.000.
2. Zona urbana: sin recargo → 9.000.
3. Domingo y E = 6 es par: el recargo va antes de los descuentos → 9.000 + 2.000 = 11.000.
4. B = 6 es par: solo el mayor descuento. VIP 20 % contra cupón 10 % → 11.000 × 0,80 = 8.800.
5. Mayor que $5.000 y ya múltiplo de 100 → **$8.800**.

### C35 · 10 kg · rural · vip · día 6 · ENVIO10
1. Tramo: 10 ≤ L2 → tramo 2 → $9.000.
2. Zona rural +20 % → 9.000 × 1,20 = 10.800.
3. Sábado, E par: recargo antes de los descuentos → 10.800 + 2.000 = 12.800.
4. B par: solo el mayor. VIP 20 % > cupón 10 % → 12.800 × 0,80 = 10.240.
5. Mayor que $5.000. Redondeo: 10.240 → **$10.200**.

### C36 · 70 kg · nacional · normal · día 7 · sin cupón
1. Tramo: 70 > L2 → 9.000 + (70 − 10) × 800 = 9.000 + 48.000 = 57.000.
2. Zona nacional +40 % → 57.000 × 1,40 = 79.800.
3. Domingo: +2.000 antes de descuentos → 81.800.
4. Cliente normal sin cupón: sin descuento.
5. Mayor que $5.000 y múltiplo de 100 → **$81.800**.

### C38 · 15,5 kg · nacional · frecuente · día 4 · sin cupón
1. Tramo: 15,5 > L2 → 9.000 + 5,5 × 800 = 13.400.
2. Zona nacional +40 % → 13.400 × 1,40 = 18.760.
3. Día 4 (hábil): sin recargo de fin de semana.
4. Cliente frecuente 5 % → 18.760 × 0,95 = 17.822.
5. Mayor que $5.000. Redondeo: 17.822 → **$17.800**.

### C39 · 1 kg · urbana · vip · día 3 · sin cupón
1. Tramo: 1 ≤ L1 = 2 → $6.000.
2. Zona urbana: sin recargo → 6.000.
3. Día 3: sin fin de semana.
4. Cliente vip 20 % → 6.000 × 0,80 = 4.800.
5. 4.800 es menor que $5.000 → se aplica el mínimo → **$5.000**.
