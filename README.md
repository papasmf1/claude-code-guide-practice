# claude-code-guide-practice

## Functions

### `add`

```python
def add(a: int | float, b: int | float) -> int | float
```

두 숫자를 더해 반환합니다.

```python
from ex_pipeline import add

add(1, 2)      # 3
add(1.5, 2.5)  # 4.0
add(-3, 5)     # 2
```

---

### `divide`

```python
def divide(a: int | float, b: int | float) -> float
```

`a`를 `b`로 나눈 결과를 `float`으로 반환합니다.

**예외**

| 예외 | 발생 조건 |
|------|----------|
| `ValueError` | `b`가 `0`일 때 |
| `TypeError` | `a` 또는 `b`가 `int \| float`이 아닐 때 (`bool` 포함) |

```python
from ex_pipeline import divide

divide(10, 2)    # 5.0
divide(7.5, 2.5) # 3.0
divide(-9, 3)    # -3.0

divide(1, 0)     # ValueError: divide() cannot divide 1 by zero
divide("x", 2)   # TypeError: divide() argument 'a' must be int or float, got 'str'
divide(True, 2)  # TypeError: divide() does not accept bool arguments
```

## Development

```bash
# 린트
.venv/bin/ruff check .

# 타입 검사
.venv/bin/mypy ex_pipeline.py test_pipeline.py

# 테스트
.venv/bin/pytest test_pipeline.py -v
```
