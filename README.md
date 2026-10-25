# gens — Generador Luhn

Generador y validador de números con el algoritmo de Luhn (mod 10). Python 3.10+, sin dependencias.

## Uso

```bash
# Generar 5 números de 16 dígitos que empiecen por 4
python3 luhn.py generar -p 4 -l 16 -n 5

# Validar uno o varios números (código de salida 1 si alguno es inválido)
python3 luhn.py validar 79927398713 "4111 1111 1111 1111"

# Calcular y añadir el dígito verificador
python3 luhn.py digito 7992739871   # -> 79927398713
```

Como módulo:

```python
import luhn
luhn.generate("4", 16)
luhn.is_valid("79927398713")
luhn.check_digit("7992739871")
```

## Tests

```bash
python3 -m unittest
```
