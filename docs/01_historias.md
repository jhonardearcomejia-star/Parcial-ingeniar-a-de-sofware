# Historias de usuario

Estudiante: Jhonar David De Arco Mejia · Código: 1029860263
Parámetros: PMAX=70, L1=2 (incluido), L2=10, RR=20 %, RN=40 %, V=20 %, S=$2.000.

## HU-1 · Validar datos de entrada (R1, R2)
**Como** operador de EnvíaYa **quiero** que el sistema rechace datos inválidos
**para** no cotizar envíos imposibles.

- **CA-1** Dado un paquete de 70,01 kg, cuando calculo el costo, entonces se lanza el error "peso inválido".
- **CA-2** Dado un envío a la zona "aerea", cuando calculo el costo, entonces se lanza un error.
- **CA-3** Dado el día 8, cuando calculo el costo, entonces se lanza un error.

## HU-2 · Calcular tarifa base y recargos (R3, R4, R5)
**Como** operador de EnvíaYa **quiero** que el costo parta de la tarifa por peso y sume los recargos de zona y de fin de semana
**para** cobrar el servicio real de cada envío.

- **CA-1** Dado un paquete de 2 kg a zona urbana en un día hábil, cuando calculo el costo, entonces la tarifa es $6.000 (el límite L1 está incluido).
- **CA-2** Dado un paquete de 5 kg a zona rural en un día hábil, cuando calculo el costo, entonces el costo es $10.800 (9.000 + 20 %).
- **CA-3** Dado un paquete de 5 kg a zona urbana un sábado, cuando calculo el costo, entonces el costo es $11.000 (9.000 + $2.000 de fin de semana).

## HU-3 · Aplicar descuentos, cupón, mínimo y redondeo (R6, R7, R8)
**Como** operador de EnvíaYa **quiero** que se aplique el descuento correcto, se rechacen cupones falsos y el valor final sea redondeado
**para** que el cliente reciba un precio justo y claro.

- **CA-1** Dado un cliente vip con el cupón ENVIO10 y un paquete de 4 kg a zona urbana en día hábil, cuando calculo el costo, entonces solo se aplica el 20 % y el costo es $7.200.
- **CA-2** Dado el cupón "PROMO5" que no existe, cuando calculo el costo, entonces se lanza un error.
- **CA-3** Dado un cliente frecuente con un paquete de 4 kg a zona urbana en día hábil, cuando calculo el costo, entonces el valor 8.550 se redondea hacia arriba y el resultado es $8.600.
