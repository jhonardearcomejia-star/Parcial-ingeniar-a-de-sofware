# Especificación (R1–R8) con mis valores

- R1: 0 < peso <= 70; si no, error "peso inválido".
- R2: zona distinta de urbana/rural/nacional, o día fuera de 1..7 -> error.
- R3: peso <= 2 -> $6.000; peso <= 10 -> $9.000; > 10 -> $9.000 + $800 por kg sobre 10 (proporcional).
- R4: rural +20 %, nacional +40 %, urbana sin recargo.
- R5: sábado (6) y domingo (7): +$2.000, antes de los descuentos.
- R6: frecuente 5 %, VIP 20 %, cupón ENVIO10 10 %; si hay cliente y cupón, solo el mayor.
- R7: cupón inexistente -> error.
- R8: mínimo $5.000; redondeo al múltiplo de $100 más cercano ($50 sube).
