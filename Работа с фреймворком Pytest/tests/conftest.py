# Знакомство с параметром scope в PyTest

import pytest

@pytest.fixture()
def set_up():
    print("Вход в систему выполнен")
    yield  # Точка начала теста, ключевое слово yield
    print("Выход из системы")

@pytest.fixture(scope="module")  # Еще есть function, cls
def some():
    print("Начало")
    yield
    print("Конец")