# Changelog
Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y versionado semántico ([SemVer](https://semver.org/lang/es/)).

## [Sin publicar]

## [1.0.0] - 2026-11-11
### Added
- Código heredado de EnvíaYa (`calc`) con CONFIG según mi código estudiantil.

## [2.0.0] - 2026-11-11
### Changed
- Refactorización completa de `calc` en funciones pequeñas y patrón Estrategia
- Eliminación del argumento `flag` (cambio MAJOR en la interfaz)
- Sustitución de números mágicos por constantes con nombre
- Corrección de 7 defectos (DEF-01 a DEF-07)
- Mejora en el redondeo (múltiplo de $100 más cercano, $50 hacia arriba)

### Fixed
- DEF-01: PMAX usado correctamente en validación de peso
- DEF-02: Validación de zona inválida lanzando ValueError
- DEF-03: Validación de día fuera de rango 1-7
- DEF-04: Sábado (día 6) incluye recargo de fin de semana
- DEF-05: Descuento de cliente y cupón aplican solo el mayor
- DEF-06: Cupón inexistente lanza error en lugar de ignorarse
- DEF-07: Redondeo al múltiplo de $100 más cercano ($50 hacia arriba)

### Deprecated
- Función `calc` con firma antigua (p, z, c, d, cup, flag)
- Use `calc(peso, zona, cliente, dia, cupón=None)` en su lugar

## [Unreleased]

## [2.0.0] - AAAA-MM-DD

### Fixed
- Se valida la zona y el día del envío.
- Se corrigen el recargo de sábado, los descuentos, los cupones y el redondeo.

### Changed
- Se refactorizó el cálculo usando el patrón Estrategia.

### Removed
- Se eliminó el argumento `flag` de `calc`.