# Plan de pruebas · EnvíaYa · legado v1.0.0 y evolución v3.0.0

Estudiante: Jhonar David De Arco Mejia · Código: 1029860263

## 1. Alcance
**Dentro del alcance:** la función heredada `calc(p, z, c, d, cup, flag)` y la función final `calc(peso, zona, cliente, dia, hora, cupón)` de `envios.py`,
y las reglas R1–R9 con mis parámetros (PMAX=70, L1=2 incluido, L2=10,
RR=20 %, RN=40 %, V=20 %, S=$2.000).
**Fuera del alcance:** interfaz de usuario, base de datos, pagos, rendimiento
y seguridad del sistema de EnvíaYa.

## 2. Niveles de prueba aplicados a este caso
| Nivel | Cómo se aplica en EnvíaYa | Evidencia |
|---|---|---|
| Unidad | `calc` se prueba aislada, con una regla por caso (por ejemplo, solo el límite de L1 o solo el recargo rural). También se prueban los tipos inválidos de día y la estrategia base. | Casos de caja negra y caja blanca en pytest |
| Integración | `calc` combina CONFIG, tarifa, zona, fin de semana, descuentos y redondeo. Se prueban combinaciones (rural + sábado + vip + cupón). | Casos de la tabla de decisión |
| Sistema | Una cotización completa de punta a punta, con entradas de un envío real, validando el valor final. | Casos de extremo a extremo y regresión |
| Aceptación | El cliente (EnvíaYa) acepta si se cumplen los criterios Dado/Cuando/Entonces de HU-1, HU-2 y HU-3. | Criterios de las historias de usuario |

## 3. Estrategia
- **Caja negra:** particiones de equivalencia, valores límite y tabla de decisión.
- **Caja blanca:** grafo de flujo, complejidad ciclomática y caminos independientes.
- **Automatización:** pytest con `parametrize`, ejecutada contra el código heredado
  y después de cada corrección.
- **Medición:** cobertura de sentencias y de ramas con pytest-cov.
- **Regresión:** toda la suite se vuelve a ejecutar tras cada corrección y la refactorización.
- **Resultados esperados:** calculados a mano a partir de la especificación,
  no del comportamiento del código.

## 4. Ambiente
Arch Linux, Python 3.14, pytest 9.2, pytest-cov 7.1, Git y GitHub
(repositorio público con ramas y etiquetas).

## 5. Roles
| Rol | Responsable | Funciones |
|---|---|---|
| Analista de requisitos | Jhonar | Especificación e historias |
| Diseñador y ejecutor de pruebas | Jhonar | Casos, automatización, defectos |
| Desarrollador de mantenimiento | Jhonar | Correcciones y refactorización |
| Cliente / aprobador | Docente | Aceptación y sustentación |

## 6. Riesgos y mitigación
| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Resultados esperados mal calculados | Media | Alto | Calcular a mano dos veces y revisar con la spec |
| Interpretar mal las reglas de paridad (D, E, B, F) | Media | Alto | Tabla de decisión y casos de frontera explícitos |
| Errores de punto flotante en el redondeo | Media | Medio | Casos con valores terminados en 50 |
| Corregir un defecto y romper otro | Alta | Alto | Regresión completa tras cada rama fix |
| Poco tiempo antes de la entrega | Alta | Alto | Commits frecuentes y priorizar partes de mayor peso |
| Cliente desconocido o regla ambigua en la spec | Baja | Medio | Documentar la ambigüedad y asumir un criterio |

## 7. Criterios de entrada
- Especificación R1–R9 aprobada y con mis valores.
- CONFIG verificado contra mi código estudiantil.
- Repositorio creado, etiqueta v1.0.0 y entorno con pytest instalado.
- Casos de prueba diseñados y con resultados esperados calculados.

## 8. Criterios de salida
- 100 % de los casos diseñados ejecutados y automatizados.
- Todos los defectos registrados con severidad y prioridad.
- Cobertura de sentencias del 100 % y de ramas ≥ 95 % tras la refactorización.
- Defectos de severidad alta corregidos y regresión completa en verde.
- Capturas de ejecución antes y después, y CHANGELOG actualizado.