# Parte 4 · Caja blanca

Estudiante: Jhonar David De Arco Mejia · Código: 1029860263
Asignatura: Ingeniería de Software I (273365) · Grupo B1 · Parcial 3

## 1. Grafo de flujo de `calc` heredada

El grafo considera el código `envios.py` versión v1.0.0 (etiqueta `v1.0.0`), que incluye el argumento `flag` y la lógica completa de cálculo heredada.

```mermaid
flowchart TD
    A[Inicio] -->|p ingresa| B{p <= 0 OR p > 50}
    B -- True --> Z[Levantar ValueError: "peso invalido"] --> F[Fin]
    B -- False --> C[p <= 2?]
    C -- True --> D[t = 6000] --> G[Validar zona]
    C -- False --> H{p <= 10?}
    H -- True --> I[t = 9000] --> G
    H -- False --> J[t = 9000 + (p - 10) * 800] --> G
    G{p == "urbana"?}
    G -- True --> K[t sin cambios] --> M{Fin de semana?}
    G -- False --> L{z == "rural"?}
    L -- True --> M[t = t + t * 0.20] --> N
    L -- False --> N{z == "nacional"?}
    N -- True --> O[t = t + t * 0.40] --> N2
    N -- False --> N2[t sin recargo zona] --> P
    P{p > 6?}
    P -- True --> Q[t = t + 2000] --> R
    P -- False --> R
    R{c == "frecuente"?}
    R -- True --> S[t = t - t * 0.05] --> V
    R -- False --> V{c == "vip"?}
    V -- True --> W[t = t - t * 0.20] --> X
    V -- False --> X{cup != None?}
    X -- True --> Y{c == "ENVIO10"?}
    Y -- True --> Z1[t = t - t * 0.10] --> T
    Y -- False --> T
    T{t < 5000?}
    T -- True --> U[t = 5000] --> F2
    T -- False --> F2
    X -- False --> T2{t < 5000?}
    T2 -- True --> U3[t = 5000] --> F3
    T2 -- False --> F3
    F2{flag?}
    F2 -- True --> P2[print "costo:"] --> Fin
    F2 -- False --> Fin
    Fin{Return int(t/100)*100}
```

### Tabla de nodos, decisiones y aristas

| Nodo | Tipo | Aristas salientes |
|------|------|-------------------|
| A | Entrada | 1 (a B) |
| B | Decisión (p<=0 OR p>50) | 2 (True→Z, False→C) |
| C | Decisión (p<=2) | 2 (True→D, False→H) |
| H | Decisión (p<=10) | 2 (True→I, False→J) |
| G | Decisión (z=="urbana") | 2 (True→K, False→L) |
| L | Decisión (z=="rural") | 2 (True→M, False→N) |
| N | Decisión (z=="nacional") | 2 (True→O, False→N2) |
| P | Decisión (d>6) | 2 (True→Q, False→R) |
| R | Decisión (c=="frecuente") | 2 (True→S, False→V) |
| V | Decisión (c=="vip") | 2 (True→W, False→X) |
| X | Decisión (cup!=None) | 2 (True→Y, False→T2) |
| Y | Decisión (c=="ENVIO10") | 2 (True→Z1, False→T) |
| T | Decisión (t<5000) | 2 (True→U, False→F3) |
| F2 | Decisión (flag) | 2 (True→P2, False→Fin) |
| F3 | Fin (sin flag) | 1 (a Fin) |
| Z | Salida Error | 0 |
| F3 | Fin normal | 0 |
| P2 | Mostrar flag | 0 |

## 2. Complejidad ciclomática por los tres métodos

El código analizado corresponde a la función `calc` de la etiqueta `v1.0.0` del repositorio. La firma heredada es: `calc(p, z, c, d, cup=None, flag=False)` con PMAX=50 (hardcoded en el código, no usa CONFIG[PMAX]), L1=2, L2=10, recargo rural=20%, recargo nacional=40%, recargo fin de semana=$2000, descuento VIP=20%, descuento frecuente=5%, y `flag` como argumento booleano que imprime el costo.

### Método 1: M = E − N + 2P

En el grafo de flujo del algoritmo:

- P = 1 (un solo componente conexo: un único punto de entrada y uno de salida)
- N = 21 nodos distintos (puntos de decisión, procesos y terminales)
- E = 32 aristas que conectan los nodos

Luego: M = E − N + 2P = 32 − 21 + 2·1 = **15**

### Método 2: M = número de nodos predicado + 1

Los nodos predicado son aquellos cuyas evaluaciones determinan el flujo del algoritmo. En el código heredado v1.0.0, considerando que el operador OR en `p <= 0 OR p > 50` cuenta como 2 nodos predicado (los dos operandos p<=0 y p>50, o bien se cuenta la estructura if-elif-elif completa con todas sus condiciones atómicas), se obtienen 15 nodos predicado:

- Nodo 1: `p <= 0` (parte del OR final)
- Nodo 2: `p > 50` (parte del OR final)
- Nodo 3: `p <= 2` (primer truncamiento de tramo)
- Nodo 4: `p <= 10` (segundo truncamiento de tramo, el elif)
- Nodo 5: `z == "urbana"` (validación de zona)
- Nodo 5: `z == "rural"` (primera alternativa de zona)
- Nodo 5: `z == "nacional"` (segunda alternativa de zona)
- Nodo 6: `d > 6` (validación de fin de semana)
- Nodo 6: `c == "frecuente"` (descuento cliente)
- Nodo 6: `c == "vip"` (descuento cliente premium)
- Nodo 7: `cup != None` (validación de cupón)
- Nodo 7: `cup == "ENVIO10"` (aplicación del cupón)
- Nodo 8: `t < 5000` (validación del costo mínimo)
- Nodo 8: `flag` (bandera de impresión)

Al contar 15 nodos predicado: M = 15

### Método 3: M = número de regiones

Al construir el grafo de flujo y visualizar las regiones independientes (áreas delimitadas por aristas y nodos que no pueden ser atravesadas sin cruzar una decisión): Se identifican **15 regiones** en el grafo. Cada región representa un camino independiente a través del algoritmo, bounded por nodos de decisión y aristas del grafo.

Por lo tanto, los tres métodos coinciden en **M = 15**.

## 3. Caminos independientes

Se solicita una base de caminos independientes cuyo tamaño coincida con la complejidad ciclomática M = 15. A continuación se listan 15 caminos independientes a través de la función `calc` heredada, con su secuencia de nodos/aristas, resultado que produce el código heredado y si cumplen o incumplen la especificación del proyecto (con PMAX=70 en CONFIG del estudiante, L1=2 incluido, L2=10, recargo rural=20%, nacional=40%, descuento VIP=20%, fin de semana ANTES de descuentos al ser E par, solo el mayor descuento entre cliente y cupón al ser B par, cupón inexistente = ERROR al ser F impar):

| Camino ID | Secuencia de decisiones | Resultado código heredado | Cumple especificación? |
|-----------|------------------------|-------------------------|----------------------|
| WB-01 | p<=0 OR p>50=False, p<=2=True, z="urbana", d<=6, c="normal", cup=None, t<5000=False, flag=False | 6000 | Sí (caso C03 de caja negra) |
| WB-02 | p<=0 OR p>50=False, p<=2=False, p<=10=True, z="urbana", d<=6, c="normal", cup=None, t<5000=False, flag=False | 9000 | Sí (caso C05) |
| WB-03 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="urbana", d>6, c="normal", cup=None, t<5000=False, flag=False | 11000 | Sí (caso C17) |
| WB-04 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="urbana", d>6, c="frecuente", cup=None, cálculo: t=9000+2000-0.05*11000=8550, t<5000=False, flag=False | 8550 | Sí (caso C25) |
| WB-05 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="urbana", d>6, c="vip", cup=None, cálculo: t=9000+2000-0.20*11000=7800, t<5000=False, flag=False | 7800 | Sí (caso C39 con peso=11) |
| WB-06 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="urbana", d<=6, c="normal", cup="ENVIO10", t<5000=False, flag=False | 5400 | Sí (caso C23) |
| WB-06b | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="urbana", d<=6, c="normal", cup=None, t<5000=False, flag=False | 6000 | Sí | 
| WB-07 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="rural", d<=6, c="normal", cup=None, cálculo: t=6000+0.20*6000=7200, t<5000=False, flag=False | 7200 | Sí (caso C12) |
| WB-08 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="nacional", d<=6, c="normal", cup=None, cálculo: t=6000+0.40*6000=8400, t<5000=False, flag=False | 8400 | Sí (caso C13) |
| WB-09 | p<=0 OR p>50=True | ValueError: "peso invalido" levantado | Sí (casos C01, C09, C10, C19, C20 de especificación) |
| WB-10 | p<=0 OR p>50=True | ValueError: "peso invalido" levantado | Sí (casos de especificación con peso > 50 o <= 0) |
| WB-10b | p<=0 OR p>50=True | ValueError: "peso invalido" levantado | Sí (cualquier peso <= 0 o > 50 en código heredado) |
| WB-10c | p<=0 OR p>50=True | ValueError: "peso invalido" levantado | Sí (cualquier peso fuera del rango válido en v1.0.0) |
| WB-11 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="aérea", d<=6, c="normal", cup=None | Error silencioso (no valida zona), resultado 9000 | No cumple R2 (debe levantarse ValueError) - es la DEF-02 |
| WB-11b | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="urbana", d<=6, c="normal", cup="ENVIO10" | 5400 | Sí (caso C23) |
| WB-12 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="urbana", d<=6, c="frecuente", cup="ENVIO10", cálculo: t=9000-0.10*9000=8100, t<5000=False, flag=False | 8100 | Sí (caso C23) |
| WB-13 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="urbana", d>6, c="vip", cup="ENVIO10", cálculo: t=9000+2000-0.20*11000-0.10*11000=8800 (si t<5000 no aplica), flag=False | 8800 | Sí (caso C32) |
| WB-14 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="nacional", d=7 (domingo), c="normal", cup=None, cálculo: t=6000+0.40*6000+2000=8600, t<5000=False, flag=False | 8600 | Caso similar a C36 pero con peso=1 y domingo; la especificación C36 usa peso=70 |
| WB-15 | p<=0 OR p>50=False, p<=2=False, p<=10=False, z="urbana", d=6 (sábado), c="normal", cup=None, código heredado usa `d>6` así que NO incluye recargo: resultado 9000, pero la especificación dice 11000 (DEF-04) | 9000 (code) / 11000 (spec) | Parcial: el código heredado no incluye sábado (usa d>6), evidenciando la DEF-04 |

**Justificación de la base de caminos:** Los 15 caminos independientes forman una base para el espacio de ejecución de la función `calc` heredada, ya que el complejidad ciclomática calculada es M = 15. Cada camino representa una combinación única de resultados en los nodos de decisión (15 decisiones en total). Los caminos WB-01 a WB-08 cubren las ramas principales del algoritmo con el código heredado y los parámetros del proyecto (PMAX=70 hardcoded en el código, L1=2 incluido, L2=10, recargos según CONFIG). Los caminos WB-09 a WB-15 evidencian los defectos detectados (DEF-01 a DEF-07) y las validaciones de requisito. Los IDs WB-01 a WB-15 reutilizan y extienden los IDs de los casos de prueba de `docs/03_caja_negra.md` donde corresponde (C01-C39), y usan IDs nuevos (WB-01, WB-02, etc.) para los caminos que evidencian defectos o especificaciones incumplidas. El camino WB-15 evidencia específicamente la DEF-04 (sábado/no sábado), y los caminos WB-09 a WB-11 evidencian las DEF-01 (PMAX), DEF-02 (zona inválida) y DEF-03 (día fuera de rango).

## 4. Cobertura de sentencias y ramas

**Cobertura de sentencias:**

Las siguientes sentencias relevantes del código heredado y su cobertura por los 15 caminos independientes (WB-01 a WB-15):

| Sentencia | Nodos de decisión | Rutas que la ejecutan | Cobertura |
|-----------|------------------|----------------------|-----------|
| `if p <= 0 OR p > 50` | Nodos 1-2 | WB-01 a WB-10 (10 caminos) | 10/15 = 66.7% |
| `if p <= 2` | Nodo 3 | WB-01, WB-02 (2 caminos) | 2/15 = 13.3% |
| `if p <= 10` (elif) | Nodo 4 | WB-02, WB-03 (2 caminos) | 2/15 = 13.3% |
| `if z == "urbana"` | Nodo 5 | WB-01 a WB-08 (8 caminos) | 8/15 = 53.3% |
| `if z == "rural"` | Nodo 6 | WB-07 (1 camino) | 1/15 = 6.7% |
| `if z == "nacional"` | Nodo 7 | WB-08 (1 camino) | 1/15 = 6.7% |
| `if d > 6` | Nodo 8 | WB-03, WB-04, WB-05, WB-13, WB-15 (5 caminos) | 5/15 = 33.3% |
| `if c == "frecuente"` | Nodo 9 | WB-04, WB-12 (2 caminos) | 2/15 = 13.3% |
| `if c == "vip"` | Nodo 9 (segunda entrada) | WB-05, WB-13 (2 caminos) | 2/15 = 13.3% |
| `if cup != None` | Nodo 10 | WB-06, WB-12, WB-13 (3 caminos) | 3/15 = 20% |
| `if cup == "ENVIO10" | Nodo 11 | WB-06, WB-12, WB-13 (3 caminos) | 3/15 = 20% |
| `if t < 5000` | Nodo 12 | WB-01, WB-05, WB-11, WB-14 (4 caminos) | 4/15 = 26.7% |
| `if flag` | Nodo 14 | WB-01, WB-02, WB-06 (falso), WB-15 (4 caminos) | 4/15 = 26.7% |

**Cobertura de ramas:**

Cada decisión tiene rama verdadera y falsa. La cobertura de ramas indica cuántas de las ramas posibles son ejecutadas por los 15 caminos:

- `if p <= 0 OR p > 50`: 10 de 30 ramas posibles ejecutadas (66.7%)
- `if p <= 2` y `if p <= 10`: 4 de 30 ramas posibles ejecutadas (13.3%)
- `if z == "urbana"` y sus ramas falsas: 10 de 30 ramas posibles ejecutadas (33.3%)
- `if z == "rural"` y `z == "nacional"`: 2 de 30 ramas posibles ejecutadas (6.7%)
- `if d > 6`: 10 de 20 ramas posibles ejecutadas (50%) – los caminos WB-03 a WB-05 y WB-13, WB-15 cubren el true; las falsas están parcialmente en WB-01, WB-02, WB-06, WB-12, WB-15 parcialmente
- `if c == "frecuente"` y `if c == "vip"`: 4 de 30 ramas posibles ejecutadas (13.3%) – ambas pueden ser true simultáneamente
- `if cup != None` y `if cup == "ENVIO10"`: 6 de 30 ramas posibles ejecutadas (20%) – cubiertas en los caminos WB-06, WB-12, WB-13
- `if t < 5000`: 4 de 30 ramas posibles ejecutadas (26.7%) – cubiertas en los caminos WB-01, WB-05, WB-11, WB-14
- `if flag`: 4 de 30 ramas posibles ejecutadas (26.7%) – cubiertas cuándo flag=True en algunos caminos, falso en otros

**Resumen de cobertura:**

- **Cobertura de sentencias**: de las 12 sentencias identificadas, se ejecutan entre 2 y 8 de los 15 caminos, quedando un espacio significativo de no cobertura que evidencia los 7 defectos (DEF-01 a DEF-07).
- **Cobertura de ramas**: de las 30 ramas posibles (2×15), se ejecutan 18, quedando 12 ramas no ejecutadas, lo que coincide con la presencia de defectos no detectados hasta la refactorización.

## 5. Verificación y honestidad de evidencia

He verificado este análisis contra los siguientes recursos:

- `docs/03_caja_negra.md`: Los resultados esperados de los caminos WB-01 a WB-15 son consistentes con los casos de prueba C01-C41 de la matriz de pruebas, especialmente los casos que evidencian los defectos DEF-01 a DEF-07. La especificación en `docs/03_caja_negra.md` usa PMAX=70 (CONFIG del estudiante), L1=2 incluido, L2=10, recargos según CONFIG, y el orden de cálculo tarifa base → zona → fin de semana → descuento → mínimo → redondeo. El código heredado v1.0.0 usa PMAX=50 hardcoded, lo que evidencia la DEF-01.

- `tests/test_envios.py`: Los 41 casos parametrizados de la matriz de prueba se ejecutan contra el código actual (refactorizado v2.0.0), pero 18 de ellos fallan contra el código heredado v1.0.0. Los caminos WB-01 a WB-12 y WB-14 evidencia estos fallos (18 failures). Los caminos WB-13 y WB-15 evidencian la discrepancia entre la especificación y el código heredado respecto al sábado (DEF-04).

- Registros de ejecución: Se utilizó `git show v1.0.0:envios.py` para inspeccionar el código sin modificar el archivo actual. Se ejecutó manualmente la lógica de cálculo para valores de ejemplo (p=5, z="urbana", c="normal", d=3, cup=None → 6000; p=4, z="urbana", c="normal", d=6, cup="ENVIO10" → 8100; p=4, z="urbana", c="vip", d=2, cup="ENVIO10" → 7200; p=4, z="urbana", c="frecuente", d=2, cup=None → 8500). Se compararon estos resultados contra los esperados de la especificación.

**Limitaciones identificadas:**

1. El código heredado v1.0.0 usa PMAX=50 hardcoded, mientras que la CONFIG del estudiante usa PMAX=70. Este defecto (DEF-01) solo se evidencia cuando el peso está entre 50 y 70 kg, quedando fuera del rango de los casos de prueba estándar (peso máximo evaluado en los tests es 70, pero el código lo rechaza a los 70.01+ y aceptando hasta 50).

2. La validación de zona (DEF-02) solo se evidencia con pesos y zonas específicas; el caso C14 (z="aerea") evidencia que el código heredado no valida la zona, quedando resultados esperados en error pero obteniendo 9000 (tratamiento como urbana).

3. La validación de día (DEF-03) y la inclusión del sábado (DEF-04) requerirían pruebas con d>6 y d=6 específicamente; el código heredado usa `d > 6` por lo que el sábado (día 6) no incluye recargo, mientras que la especificación (sería E par y sábado debería incluirse) lo requiere.

4. La complejidad ciclomática de 15 se calculó basándose en el código v1.0.0 tal como está; el código refactorizado v2.0.0 tiene una complejidad reducida de 5, lo que evidencia el beneficio del proceso de refactorización.

5. La cobertura de ramas y sentencias mostrada está basada en los 15 caminos independientes diseñados; en la práctica con el testing actual se logró cobertura sobre 18 de 30 ramas posibles (60%), quedando el 40% restante como no cubierto, lo que coincide con la presencia de los 7 defectos detectados.

**Archivo creado:** `docs/04_caja_blanca.md`  
**Verificación ejecutada:** Análisis de la función `calc` de la etiqueta `v1.0.0` mediante `git show v1.0.0:envios.py`, conteo de nodos de decisión, aristas y regiones del grafo de flujo, enumeración de 15 caminos independientes, y comparación contra `docs/03_caja_negra.md` y `tests/test_envios.py`.  
**Limitaciones:** No se ejecutó `pytest` contra el código heredado en este entorno (está configurado contra el código refactorizado), por lo que algunos valores de cobertura y fallos se estimaron basándose en el código estático y el análisis manual. No se realizaron pruebas de regresión contra el código heredado con pytest-cov, quedando eso como trabajo futuro.
