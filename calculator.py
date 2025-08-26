import argparse
import math
from typing import Dict


def add(a: float, b: float) -> float:
    """Return the sum of ``a`` and ``b``."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the result of ``a`` minus ``b``."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of ``a`` and ``b``."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the result of ``a`` divided by ``b``.

    Raises:
        ZeroDivisionError: If ``b`` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def modulus(a: float, b: float) -> float:
    """Return the modulus of ``a`` and ``b``."""
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b


def sin(x: float) -> float:
    """Return the sine of ``x`` (in radians)."""
    return math.sin(x)


def cos(x: float) -> float:
    """Return the cosine of ``x`` (in radians)."""
    return math.cos(x)


def tan(x: float) -> float:
    """Return the tangent of ``x`` (in radians)."""
    return math.tan(x)


# Mapping of supported function names to callables used for expression evaluation.
_ALLOWED_NAMES: Dict[str, float] = {name: getattr(math, name) for name in [
    "sin",
    "cos",
    "tan",
    "pi",
    "e",
]}


def calculate(expression: str) -> float:
    """Safely evaluate a mathematical ``expression``.

    The environment includes basic mathematical operators and the trigonometric
    functions ``sin``, ``cos`` and ``tan`` as well as constants ``pi`` and ``e``.
    """
    # ``eval`` is used with a restricted global namespace to avoid exposing
    # builtins which could be unsafe in this simple calculator.
    return eval(expression, {"__builtins__": {}}, _ALLOWED_NAMES)


def main() -> None:
    parser = argparse.ArgumentParser(description="Command line calculator")
    parser.add_argument(
        "expression",
        help="Mathematical expression to evaluate, e.g. 'sin(pi / 2) + 5'",
    )
    args = parser.parse_args()
    result = calculate(args.expression)
    print(result)


if __name__ == "__main__":
    main()
