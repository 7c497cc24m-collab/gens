#!/usr/bin/env python3
"""Generador y validador de números con el algoritmo de Luhn (mod 10)."""

import argparse
import secrets
import sys


def _digits(number: str) -> list[int]:
    if not number.isdigit():
        raise ValueError(f"'{number}' debe contener solo dígitos")
    return [int(d) for d in number]


def check_digit(partial: str) -> int:
    """Calcula el dígito verificador que hay que añadir a `partial`."""
    total = 0
    # Recorriendo desde la derecha, se duplican las posiciones pares
    # (la primera queda en posición 1 al añadir el verificador).
    for i, d in enumerate(reversed(_digits(partial))):
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return (10 - total % 10) % 10


def is_valid(number: str) -> bool:
    """Indica si `number` (con su dígito verificador) cumple Luhn."""
    number = number.replace(" ", "").replace("-", "")
    if len(number) < 2 or not number.isdigit():
        return False
    return check_digit(number[:-1]) == int(number[-1])


def complete(partial: str) -> str:
    """Devuelve `partial` con su dígito verificador añadido."""
    return partial + str(check_digit(partial))


def generate(prefix: str = "", length: int = 16) -> str:
    """Genera un número aleatorio válido de `length` dígitos que empieza por `prefix`."""
    if prefix and not prefix.isdigit():
        raise ValueError("el prefijo debe contener solo dígitos")
    if length < 2:
        raise ValueError("la longitud mínima es 2")
    if len(prefix) >= length:
        raise ValueError("el prefijo debe ser más corto que la longitud total")
    body = prefix + "".join(
        str(secrets.randbelow(10)) for _ in range(length - len(prefix) - 1)
    )
    return complete(body)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generador y validador Luhn")
    sub = parser.add_subparsers(dest="cmd", required=True)

    gen = sub.add_parser("generar", aliases=["gen"], help="generar números válidos")
    gen.add_argument("-p", "--prefijo", default="", help="prefijo inicial")
    gen.add_argument("-l", "--longitud", type=int, default=16, help="longitud total (16)")
    gen.add_argument("-n", "--cantidad", type=int, default=1, help="cuántos generar (1)")

    val = sub.add_parser("validar", aliases=["val"], help="validar números")
    val.add_argument("numeros", nargs="+")

    dig = sub.add_parser("digito", aliases=["dig"], help="calcular dígito verificador")
    dig.add_argument("parcial")

    args = parser.parse_args(argv)
    try:
        if args.cmd in ("generar", "gen"):
            for _ in range(args.cantidad):
                print(generate(args.prefijo, args.longitud))
        elif args.cmd in ("validar", "val"):
            ok = True
            for n in args.numeros:
                valid = is_valid(n)
                ok &= valid
                print(f"{n}: {'válido' if valid else 'inválido'}")
            return 0 if ok else 1
        else:
            print(complete(args.parcial))
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
