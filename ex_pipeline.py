def add(a: int | float, b: int | float) -> int | float:
    return a + b


def divide(a: int | float, b: int | float) -> float:
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("divide() does not accept bool arguments")
    if not isinstance(a, (int, float)):
        raise TypeError(
            f"divide() argument 'a' must be int or float, got {type(a).__name__!r}"
        )
    if not isinstance(b, (int, float)):
        raise TypeError(
            f"divide() argument 'b' must be int or float, got {type(b).__name__!r}"
        )
    if b == 0:
        raise ValueError(f"divide() cannot divide {a!r} by zero")
    return a / b
