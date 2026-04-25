import pytest
from calculator import add, subtract, multiply, divide

# Тест 1: Проверка сложения
def test_add():
    assert add(2, 3) == 5

# Тест 2: Проверка вычитания
def test_subtract():
    assert subtract(10, 4) == 6

# Тест 3: Проверка умножения
def test_multiply():
    assert multiply(3, 3) == 9

# Тест 4: Проверка деления
def test_divide():
    assert divide(10, 2) == 5.0

# Тест 5: Проверка деления на ноль (ожидаем ошибку)
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)