import pytest

@pytest.fixture()
def set_up():
    print("Вход в систему выполнен")
    yield  # Точка начала теста, ключевое слово yield
    print("Выход из системы")

def test_mail_1(set_up):
    print("Письмо отправлено")

def test_mail_2(set_up):
    print("Письмо отправлено")