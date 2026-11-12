# Parte 4 · Caja blanca

Estudiante: Jhonar David De Arco Mejia · Código: 1029860263
Código analizado: `calc` heredada de la etiqueta `v1.0.0`.

## 1. Grafo de flujo

El operador `or` de la validación de peso se muestra como dos decisiones porque Python evalúa la segunda condición solo cuando `p <= 0` es falso. Las asignaciones de tarifa se mantienen en nodos separados; las ramas de zona que no cambian `t` llegan directamente a la unión.

```mermaid
flowchart TD
    START[Inicio] --> P0{p <= 0?}
    P0 -- Sí --> ERR[ValueError: peso invalido]
    P0 -- No --> P50{p > 50?}
    P50 -- Sí --> ERR
    P50 -- No --> L1{p <= L1?}
    ERR --> END[Fin]

    L1 -- Sí --> T1[t = 6000]
    L1 -- No --> L2{p <= L2?}
    L2 -- Sí --> T2[t = 9000]
    L2 -- No --> T3[t = 9000 + (p - L2) * 800]
    T1 --> ZU{z == urbana?}
    T2 --> ZU
    T3 --> ZU

    ZU -- Sí --> WE{d > 6?}
    ZU -- No --> ZR{z == rural?}
    ZR -- Sí --> TR[t += t * RECARGO_RURAL]
    ZR -- No --> ZN{z == nacional?}
    ZN -- Sí --> TN[t += t * RECARGO_NACIONAL]
    ZN -- No --> WE
    TR --> WE
    TN --> WE

    WE -- Sí --> TW[t += RECARGO_FINDE]
    WE -- No --> FREQ{c == frecuente?}
    TW --> FREQ
    FREQ -- Sí --> TF[t -= t * 0.05]
    FREQ -- No --> VIP{c == vip?}
    TF --> VIP
    VIP -- Sí --> TV[t -= t * DESC_VIP]
    VIP -- No --> CUP{cup != None?}
    TV --> CUP
    CUP -- Sí --> ENV{cup == ENVIO10?}
    CUP -- No --> MIN{t < 5000?}
    ENV -- Sí --> TC[t -= t * 0.10]
    ENV -- No --> MIN
    TC --> MIN
    MIN -- Sí --> TMIN[t = 5000]
    MIN -- No --> FLAG{flag?}
    TMIN --> FLAG
    FLAG -- Sí --> PRINT[print costo]
    FLAG -- No --> RET[return int(t / 100) * 100]
    PRINT --> RET
    RET --> END
```

El grafo tiene **N = 29 nodos**, **E = 42 aristas** y **P = 1** componente conexo.

## 2. Complejidad ciclomática

### Método 1: aristas, nodos y componentes

`M = E − N + 2P = 42 − 29 + 2(1) = 15`

### Método 2: nodos predicado

Se cuentan 14 predicados: `p <= 0`, `p > 50`, `p <= L1`, `p <= L2`, `z == urbana`, `z == rural`, `z == nacional`, `d > 6`, `c == frecuente`, `c == vip`, `cup != None`, `cup == ENVIO10`, `t < 5000` y `flag`.

`M = 14 + 1 = 15`

El `or` de la validación de peso añade un predicado porque tiene evaluación de cortocircuito.

### Método 3: regiones

El grafo conectado contiene **15 regiones**. Por tanto, los tres métodos coinciden: **M = 15**.

## 3. Caminos independientes y casos

Las entradas y resultados de esta tabla son para la función heredada `calc(p, z, c, d, cup=None, flag=False)`. Los caminos parten de WB-01 y agregan una rama independiente en cada fila posterior.

| Camino | Entrada `(p, z, c, d, cup, flag)` | Resultado heredado | Rama que agrega |
|---|---|---:|---|
| WB-01 | `(5, urbana, normal, 3, None, False)` | $9.000 | Camino base; entradas válidas y retorno sin cambios |
| WB-02 | `(0, urbana, normal, 3, None, False)` | `ValueError` | `p <= 0` verdadero |
| WB-03 | `(51, urbana, normal, 3, None, False)` | `ValueError` | `p <= 0` falso y `p > 50` verdadero |
| WB-04 | `(2, urbana, normal, 3, None, False)` | $6.000 | Tramo 1 |
| WB-05 | `(11, urbana, normal, 3, None, False)` | $9.800 | Tramo superior a L2 |
| WB-06 | `(5, rural, normal, 3, None, False)` | $10.800 | Recargo rural |
| WB-07 | `(5, nacional, normal, 3, None, False)` | $12.600 | Recargo nacional |
| WB-08 | `(5, aerea, normal, 3, None, False)` | $9.000 | Zona desconocida cae en la ruta sin recargo |
| WB-09 | `(5, urbana, normal, 7, None, False)` | $11.000 | Recargo de fin de semana |
| WB-10 | `(4, urbana, frecuente, 3, None, False)` | $8.500 | Descuento frecuente; el legado trunca $8.550 |
| WB-11 | `(4, urbana, vip, 3, None, False)` | $7.200 | Descuento VIP |
| WB-12 | `(4, urbana, normal, 3, ENVIO10, False)` | $8.100 | Cupón válido |
| WB-13 | `(4, urbana, normal, 3, PROMO5, False)` | $9.000 | Cupón no reconocido se ignora |
| WB-14 | `(1, urbana, vip, 3, None, False)` | $5.000 | Se aplica el costo mínimo |
| WB-15 | `(5, urbana, normal, 3, None, True)` | $9.000 e imprime el costo | `flag` verdadero |

La base contiene 15 caminos, igual a `M`. WB-08, WB-10, WB-13 y WB-14 también muestran comportamientos del código heredado que incumplen la especificación.

## 4. Cobertura de sentencias y ramas

La cobertura registrada contra `v1.0.0` está en `docs/cobertura_heredado.txt`: **29/29 sentencias y 26/26 ramas**. La salida de `docs/pytest_heredado.txt` reporta 42 pruebas, 24 aprobadas y 18 fallidas. La cobertura mide ejecución, no corrección del resultado.

| Decisión del código heredado | Rama verdadera cubierta por | Rama falsa cubierta por |
|---|---|---|
| `p <= 0 or p > 50` | C01 (`p <= 0`) y C08 (`p > 50`) | C02 |
| `p <= L1` | C03 | C04 |
| `p <= L2` | C04 | C07 |
| `z == urbana` | C11 | C12 |
| `z == rural` | C12 | C13 |
| `z == nacional` | C13 | C14 |
| `d > 6` | C18 | C15 y C17 |
| `c == frecuente` | C25 | C21 |
| `c == vip` | C29 | C21 |
| `cup != None` | C23 y C33 | C21 |
| `cup == ENVIO10` | C23 | C33 |
| `t < 5000` | C39 | C21 |
| `flag` | Prueba del argumento `flag` en la suite heredada | C21 |

Las sentencias de error, los tres tramos, los recargos, los descuentos, el cupón, el mínimo y el `print` quedan cubiertos por los casos indicados. La cobertura completa no elimina los 7 defectos registrados: varios resultados se ejecutan, pero son incorrectos según los requisitos.
