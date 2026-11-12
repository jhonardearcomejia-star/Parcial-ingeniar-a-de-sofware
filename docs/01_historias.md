HU-1 · Validar datos de entrada (R1, R2)
Como operador de EnvíaYa quiero que el sistema rechace datos inválidos
para no cotizar envíos imposibles.
  CA-1  Dado un peso de 70,01 kg, Cuando calculo el costo,
        Entonces se lanza el error "peso inválido".
  CA-2  Dado una zona "aerea", Cuando calculo el costo, Entonces se lanza un error.
  CA-3  Dado un día 8, Cuando calculo el costo, Entonces se lanza un error.

HU-2 · Calcular tarifa base y recargos (R3, R4, R5)
  CA-1  Dado un peso de 2 kg ... Entonces la tarifa base es $6.000 (L1 incluido).
  CA-2  Dado una zona rural ... Entonces se suma 20 %.
  CA-3  Dado un sábado ... Entonces se suma $2.000 antes de los descuentos.

HU-3 · Aplicar descuentos, cupón, mínimo y redondeo (R6, R7, R8)
  CA-1  Dado un cliente vip con ENVIO10 ... Entonces solo se aplica el 20 %.
  CA-2  Dado un cupón "PROMO5" ... Entonces se lanza un error.
  CA-3  Dado un costo de 8.550 ... Entonces el resultado es 8.600.