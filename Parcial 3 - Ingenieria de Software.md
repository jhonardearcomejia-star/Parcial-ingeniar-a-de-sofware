**UNIVERSIDAD DE LA GUAJIRA** 

Facultad de Ingenierías · Ingeniería de Sistemas 

# **Parcial 3 · Ingeniería de Software** 

Tercer corte  ·  Punto único  ·  Valor: 5,0 

|**Facultad**|Facultad de Ingenierías|**Programa**|Ingeniería de Sistemas|
|---|---|---|---|
|**Asignatura**|Ingeniería de Software I (273365)|**Grupo · Semestre**|B1 · VI semestre|
|**Docente**|Ing. Robert Damián Quintero Laverde|**Periodo**|2026-2 · Tercer corte|
|**Fecha**|Miércoles 11 de noviembre de 2026|**Unidades**|6. Pruebas · 7. Evolución|
|**Estudiante**||**Códig**|**o estudiantil**|



|**Entrega**|Hoy,**11 de noviembre, a las 11:59 p. m.**, en Moodle: enlace al repositorio en GitHub (o un .zip<br>que incluya la carpeta`.git`) y un PDF con el informe.|
|---|---|
|**Sustentación**|En la próxima clase.**Es obligatoria**y forma parte de la nota.|
|**Duración**|Está pensado para**toda la jornada**. Haz commits a medida que avanzas.|



## **» Punto único: sé el equipo de calidad y mantenimiento de** **_EnvíaYa_** 

_EnvíaYa_ es una empresa de envíos de Riohacha. Su sistema calcula el costo de cada envío con una función que escribió un desarrollador que ya no trabaja allí. La función **tiene defectos** , está **mal escrita** y la empresa necesita **cambiarla** . Tú eres el equipo que la va a poner en orden: 

|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|
|---|---|---|---|---|---|---|---|
|Requisitos|Plan de<br>pruebas|Caja<br>negra|Caja<br>blanca|Automatizar<br>y reportar|Refactorizar|Versionar<br>con Git|Evolucionar|



**Personalizado. Tu especificación es única.** Los valores y varias reglas del negocio dependen de tu código estudiantil. **El código heredado es el mismo para todos** , pero si una línea es o no un defecto depende de _tu_ especificación. Dos compañeros no encuentran los mismos defectos ni obtienen los mismos resultados esperados. 

## **1 Calcula tus parámetros** 

Toma los **6 últimos dígitos** de tu código estudiantil y llámalos **A B C D E F** . Ejemplo: con el código 2023 **184706** , A = 1, B = 8, C = 4, D = 7, E = 0 y F = 6. 

|**Parámetro**|**Fórmula**|**Significado**|**Ejemplo**|
|---|---|---|---|
|**PMAX**|30 + 5·A|Peso máximo permitido (kg)|35|
|**L1**|2 + (B mod 3)|Límite del tramo 1 (kg)|4|
|**L2**|10 + C|Límite del tramo 2 (kg)|14|
|**RR**|10 + 5·(E mod 4)|Recargo zona rural (%)|10 %|
|**RN**|40 + 5·(F mod 3)|Recargo zona nacional (%)|40 %|



Universidad de La Guajira · Facultad de Ingenierías · Ingeniería de Sistemas 

Página 1 

Docente: Robert Damián Quintero Laverde 

Ingeniería de Software I · Grupo B1 · Parcial 3 

|**Parámetro**|**Fórmula**|**Significado**|**Ejemplo**|
|---|---|---|---|
|**V**|10 + 5·(A mod 3)|Descuento cliente VIP (%)|15 %|
|**S**|2000 + 500·(C mod 4)|Recargo de fin de semana ($)|$2.000|



#### **Reglas que cambian según la paridad de un dígito** 

|**Dígito**|**Si es par**|**Si es impar**|**Ejemplo**|
|---|---|---|---|
|**D**· tramo 1|Incluye el límite: peso ≤ L1|No incluye el límite: peso < L1|D = 7 → peso < 4|
|**E**· recargo de fin de<br>semana|Se suma**antes**de los<br>descuentos|Se suma**después**de los<br>descuentos|E = 0 → antes|
|**B**· cliente y cupón|Solo se aplica**el mayor**de<br>los dos|Se aplican**ambos**: primero el del<br>cliente y luego el cupón|B = 8 → el mayor|
|**F**· cupón que no<br>existe|**Se ignora**|Es**error**|F = 6 → se ignora|



La **solicitud de cambio** que te toca en la Parte 8 es el valor de **(A + F) mod 3** . En el ejemplo: (1 + 6) mod 3 = **1** . 

#### **Mis parámetros (llénalo y cópialo al inicio de tu informe)** 

|**A**<br>**B**<br>**C**<br>**D**<br>**E**<br>**F**<br>**PMAX**<br>**L1**<br>**L2**<br>**RR**<br>**RN**<br>**V**<br>**S**<br>**CAMBIO**|
|---|



## **2 Especificación del cálculo del costo** 

La función recibe `peso` en kg (puede tener decimales); `zona` : urbana, rural o nacional; `cliente` : normal, frecuente o vip; `dia` : de 1 a 7, donde 6 es sábado y 7 es domingo; y `cupon` , que es opcional. 

|**ID**|**Regla (con tus valores)**|
|---|---|
|**R1**|El peso debe cumplir 0 < peso ≤ PMAX. Si no, se lanza el error “peso inválido”.|
|**R2**|Si la zona no es una de las tres válidas, o el día no está entre 1 y 7, se lanza un error.|
|**R3**|**Tarifa base.**Tramo 1 (según tu regla D): $6.000. Tramo 2 (hasta L2, inclusive): $9.000. Más de L2: $9.000<br>+ $800 por cada kg sobre L2, de forma proporcional.|
|**R4**|**Recargo por zona.**Rural: +RR %. Nacional: +RN %. Urbana: sin recargo.|
|**R5**|**Fin de semana**(sábado y domingo): +$S, antes o después de los descuentos según tu regla E.|
|**R6**|**Descuento de cliente.**Frecuente: 5 %. VIP: V %.**Cupón** `ENVIO10`: 10 %. Si hay los dos, se combinan<br>según tu regla B.|
|**R7**|Un cupón que no existe se ignora o es error, según tu regla F.|
|**R8**|El costo nunca es menor que $5.000. El resultado se**redondea al múltiplo de $100 más cercano**; los $50<br>redondean hacia arriba.|



Universidad de La Guajira · Facultad de Ingenierías · Ingeniería de Sistemas 

Página 2 

Docente: Robert Damián Quintero Laverde 

Ingeniería de Software I · Grupo B1 · Parcial 3 

#### **Ejemplo de un resultado esperado calculado a mano (código 2023184706)** 

**Entradas:** peso = 4 kg · zona = rural · cliente = vip · día = 6 (sábado) · cupón = ENVIO10 

**1.** Tramo: D = 7 es impar, el tramo 1 es peso < 4. Como 4 no es menor que 4, va al tramo 2 → **$9.000** 

**2.** Zona rural +10 % → 9.000 × 1,10 = **$9.900** 

**3.** Sábado, y E = 0 es par: el recargo va antes de los descuentos → 9.900 + 2.000 = **$11.900** 

**4.** B = 8 es par: solo el mayor descuento. VIP 15 % contra cupón 10 % → 11.900 × 0,85 = **$10.115** 

**5.** Es mayor que $5.000. Se redondea a $100 → **resultado esperado: $10.100** 

## **3 Código heredado · versión 1.0.0** 

Este código es **el mismo para todos** . Antes de empezar, llena `CONFIG` con tus valores. **No cambies nada más** hasta que llegues a la Parte 6. 

```
# envios.py
CONFIG = {
"L1": None,               # <- pon tus valores
"L2": None,
"RECARGO_RURAL": None,    # como fracción, ej. 0.15
"RECARGO_NACIONAL": None,
"DESC_VIP": None,
"RECARGO_FINDE": None,    # en pesos
}
def calc(p, z, c, d, cup=None, flag=False):
if p <= 0or p > 50:
raise ValueError("peso invalido")
if p <= CONFIG["L1"]:
        t = 6000
elif p <= CONFIG["L2"]:
        t = 9000
else:
        t = 9000 + (p - CONFIG["L2"]) * 800
if z == "urbana":
        t = t
elif z == "rural":
        t = t + t * CONFIG["RECARGO_RURAL"]
elif z == "nacional":
        t = t + t * CONFIG["RECARGO_NACIONAL"]
# fin de semana
if d > 6:
        t = t + CONFIG["RECARGO_FINDE"]
if c == "frecuente":
        t = t - t * 0.05
if c == "vip":
        t = t - t * CONFIG["DESC_VIP"]
if cup != None:
if cup == "ENVIO10":
            t = t - t * 0.10
if t < 5000:
        t = 5000
if flag:
        print("costo:", t)
return int(t / 100) * 100
```

Universidad de La Guajira · Facultad de Ingenierías · Ingeniería de Sistemas 

Página 3 

Docente: Robert Damián Quintero Laverde 

Ingeniería de Software I · Grupo B1 · Parcial 3 

**Lenguaje.** Puedes trabajar en Java o JavaScript si lo prefieres, pero debes traducir el código **sin cambiar su lógica** , defectos incluidos. 

## **4 Lo que debes hacer** 

#### **Parte 1 · Requisitos y criterios de aceptación** 

**0,4 pts** 

1. Escribe **tu especificación** completa, de R1 a R8, con tus números ya puestos. 

2. Redacta **3 historias de usuario** que cubran las reglas R1 a R8, cada una con criterios de aceptación en formato **Dado / Cuando / Entonces** . 

3. Arma una **matriz de trazabilidad** con las columnas requisito → historia → casos de prueba. La irás completando en las partes siguientes. 

#### **Parte 2 · Plan de pruebas** 

**0,5 pts** 

El plan debe tener: 

- alcance; 

- los cuatro niveles de prueba (unidad, integración, sistema y aceptación) y **cómo se aplica cada uno** a este caso; 

- estrategia, ambiente y roles; 

- **riesgos** con su mitigación; 

- criterios de entrada y de salida. 

#### **Parte 3 · Diseño de casos de caja negra** 

**0,9 pts** 

1. **Particiones de equivalencia** de cada entrada, válidas e inválidas. 

2. **Valores límite** de `peso` alrededor de 0, L1, L2 y PMAX. Ten en cuenta si tu límite L1 está incluido o no. 

3. **Tabla de decisión** para cliente × cupón × fin de semana, según tus reglas B y E. 

4. **Matriz de casos de prueba** con **mínimo 20 casos** . Columnas: ID, requisito, entradas, **resultado esperado calculado a mano** y técnica que lo generó. Muestra el cálculo paso a paso de al menos 5 casos, como en el ejemplo. 

#### **Parte 4 · Caja blanca** 

**0,6 pts** 

1. Dibuja el **grafo de flujo** de `calc` . 

2. Calcula la **complejidad ciclomática de tres formas** : con aristas y nodos, con nodos predicado y con regiones. 

3. Lista los **caminos independientes** y escribe un caso de prueba para cada uno. 

4. Indica qué casos logran **cobertura de sentencias** y cuáles **cobertura de ramas** . 

#### **Parte 5 · Automatización, ejecución y defectos** 

**0,8 pts** 

1. Automatiza **todos** tus casos con `pytest` (o JUnit o Jest) y ejecútalos **contra el código heredado** . 

2. Mide la cobertura con `pytest-cov` o una herramienta equivalente, y adjunta capturas. 

3. Registra **cada defecto** con: ID, título, requisito que incumple, pasos para reproducirlo, resultado esperado y resultado obtenido, y **severidad** y **prioridad** justificadas. 

Universidad de La Guajira · Facultad de Ingenierías · Ingeniería de Sistemas 

Página 4 

Docente: Robert Damián Quintero Laverde 

Ingeniería de Software I · Grupo B1 · Parcial 3 

4. Calcula estas **métricas** : porcentaje de casos que pasan, defectos por severidad, densidad de defectos (defectos por cada 100 líneas) y cobertura de sentencias y de ramas. 

#### **Parte 6 · Mantenimiento y refactorización** 

**0,9 pts** 

1. Identifica **mínimo 6 malos olores** ( _code smells_ ) con su nombre técnico y la línea donde están. Explica qué **deuda técnica** genera cada uno. 

2. **Clasifica** cada cambio que harás como mantenimiento correctivo, adaptativo, perfectivo o preventivo. 

3. **Refactoriza** : extrae funciones; reemplaza los números mágicos por constantes con nombre; elimina el argumento `flag` ; y aplica el patrón **Estrategia** a las zonas **o** a los descuentos, con su diagrama de clases UML. 

4. **Corrige** todos los defectos que reportaste. 

5. Haz las **pruebas de regresión** : vuelve a ejecutar las **mismas** pruebas y muestra que ahora todas pasan. 

6. Compara el antes y el después: complejidad ciclomática, número de líneas y cobertura. 

#### **Parte 7 · Gestión de configuración** 

###### **0,5 pts** 

1. Pon la etiqueta `v1.0.0` al código heredado. 

2. Crea **una rama por cada defecto** ( `fix/DEF-01` , `fix/DEF-02` , …), una rama `refactor/estrategia` y otra `test/suite` . Intégralas con _merge_ o _pull request_ . 

3. Publica la nueva versión con la etiqueta que corresponda según **versionado semántico** . Justifica la versión: por ejemplo, quitar `flag` cambia la interfaz de la función. ¿Eso la hace _major_ ? 

4. Escribe un `CHANGELOG.md` en el formato _Keep a Changelog_ y las **notas de la versión** . 

5. Adjunta la salida de `git log --oneline --graph --all` . 

6. Los commits deben estar repartidos a lo largo del día. 



<!-- Start of picture text -->
Parte 8 · Solicitud de cambio y análisis de impacto 0,4 pts<br><!-- End of picture text -->

Te toca la solicitud de cambio que corresponde a tu valor de **(A + F) mod 3** : 

|**(A+F) mod 3**|**Solicitud de cambio**|
|---|---|
|**0**|Nueva zona**insular**(San Andrés) con un recargo del 70 %. Los envíos insulares no aceptan cupón.|
|**1**|Nuevo tipo de cliente**empresarial**con un 12 % de descuento. Si el peso es mayor que L2, el<br>recargo de zona no se cobra.|
|**2**|**Hora pico:**se agrega el parámetro`hora`(de 0 a 23). Entre las 17 y las 19, inclusive, hay un recargo<br>del 8 %, que se calcula**después**del recargo por zona.|



##### Para tu solicitud: 

1. Haz el **análisis de impacto** con tu matriz de trazabilidad: qué requisitos, historias, casos de prueba y partes del código se afectan. 

2. Clasifica el tipo de mantenimiento. 

3. Implementa el cambio en su propia rama, con **sus pruebas escritas primero** . 

4. Publica una nueva versión y actualiza el CHANGELOG. 

Universidad de La Guajira · Facultad de Ingenierías · Ingeniería de Sistemas 

Página 5 

Docente: Robert Damián Quintero Laverde 

Ingeniería de Software I · Grupo B1 · Parcial 3 

## **5 Sustentación dinámica (obligatoria)** 

En la sustentación, el profesor te dará un **reporte de defecto o una solicitud de cambio que no has visto** . En **20 minutos** , frente a él, debes: 

1. Escribir primero la prueba que lo reproduce y verla fallar. 

2. Corregir el código. 

3. Ejecutar toda la regresión. 

4. Hacer el commit y la etiqueta con la versión que corresponda. 

**Atención.** Si no puedes hacerlo ni explicar tu propio trabajo, tu nota máxima es **2,0** . 

## **6** 

## **Reglas** 

- Si tu especificación, tus resultados esperados o tu `CONFIG` no corresponden a tu código estudiantil, la nota es **0** . 

- Si tus pruebas o tu reporte de defectos son iguales a los de otro estudiante, los dos tienen **0** : las especificaciones son distintas. 

- Un repositorio con un solo commit, o con todos los commits hechos al mismo tiempo, se califica con sospecha. 

## **7 Rúbrica** 

|**Parte**|**Qué se evalúa**|**Valor**|
|---|---|---|
|1. Requisitos|Especificación propia, historias con criterios Dado/Cuando/Entonces,<br>trazabilidad|0,4|
|2. Plan de pruebas|Niveles aplicados al caso, estrategia, riesgos, criterios de entrada y<br>salida|0,5|
|3. Caja negra|Particiones, valores límite, tabla de decisión, matriz con resultados<br>esperados correctos|0,9|
|4. Caja blanca|Grafo de flujo, complejidad ciclomática de tres formas, caminos y<br>cobertura|0,6|
|5. Automatización y<br>defectos|Pruebas automatizadas, reporte de defectos, severidad y prioridad,<br>métricas|0,8|
|6. Refactorización|Malos olores, patrón Estrategia, corrección y regresión en verde|0,9|
|7. Configuración|Ramas, etiquetas, versionado semántico justificado, CHANGELOG y<br>notas de versión|0,5|
|8. Solicitud de cambio|Análisis de impacto, pruebas primero, implementación y nueva versión|0,4|
|**Total**||**5,0**|



Universidad de La Guajira · Facultad de Ingenierías · Ingeniería de Sistemas 

Página 6 

Docente: Robert Damián Quintero Laverde 

Ingeniería de Software I · Grupo B1 · Parcial 3 

#### **Antes de entregar, revisa que tengas…** 

Tu nombre, tu código y la tabla de **mis parámetros** llena al inicio del informe. 

El repositorio con las etiquetas `v1.0.0` y las versiones nuevas, y el CHANGELOG. Las **8 partes** del informe, en orden y con su título. 

Capturas de las pruebas fallando contra el código heredado y pasando después de corregir. 

La salida de `git log --oneline --graph --all` . 

### **¡Éxitos!** 

Universidad de La Guajira · Facultad de Ingenierías · Ingeniería de Sistemas 

Página 7 

