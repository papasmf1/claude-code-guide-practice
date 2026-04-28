import pytest

from ex_pipeline import add, divide


def test_add_integers() -> None:
    assert add(1, 2) == 3


def test_add_floats() -> None:
    assert add(1.5, 2.5) == pytest.approx(4.0)


def test_add_mixed() -> None:
    assert add(1, 2.5) == pytest.approx(3.5)


def test_add_negative() -> None:
    assert add(-3, 5) == 2


def test_add_zeros() -> None:
    assert add(0, 0) == 0


def test_divide_integers() -> None:
    assert divide(10, 2) == pytest.approx(5.0)


def test_divide_floats() -> None:
    assert divide(7.5, 2.5) == pytest.approx(3.0)


def test_divide_negative() -> None:
    assert divide(-9, 3) == pytest.approx(-3.0)


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="cannot divide"):
        divide(1, 0)


def test_divide_by_zero_message_includes_numerator() -> None:
    with pytest.raises(ValueError, match="42"):
        divide(42, 0)


def test_divide_invalid_type_a() -> None:
    with pytest.raises(TypeError, match="must be int or float"):
        divide("x", 2)  # type: ignore[arg-type]


def test_divide_invalid_type_b() -> None:
    with pytest.raises(TypeError, match="must be int or float"):
        divide(10, None)  # type: ignore[arg-type]


def test_divide_bool_rejected() -> None:
    with pytest.raises(TypeError, match="does not accept bool"):
        divide(True, 2)
