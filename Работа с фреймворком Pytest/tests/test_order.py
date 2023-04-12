# Задача очередности запуска методов с помощью фреймворка PyTest

import pytest

@pytest.mark.run(order=2)
def test_method_1():
    print("Метод 1")

def test_method_2():
    print("Метод 2")

def test_method_3():
    print("Метод 3")

@pytest.mark.run(order=1)
def test_method_4():
    print("Метод 4")

def test_method_5():
    print("Метод 5")

def test_method_6():
    print("Метод 6")

