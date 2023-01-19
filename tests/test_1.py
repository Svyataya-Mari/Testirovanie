import pytest
from libs import lib


# Тест функции, которая проверяет, что значения во входном списке стоят в порядке возрастания
class TestSort:

    # Функция возвращает отсортированный по возрастанию список
    @pytest.fixture
    def sorted_example(self):
        return [2, 6, 12, 17, 24]

    # Функция возвращает неотсортированный список
    @pytest.fixture
    def unsorted_example(self):
        return [6, 2, 24, 17, 12]

    # Функция возвращает неотсортированный список с одинаковыми значениями
    @pytest.fixture
    def unsorted_qeual_example(self):
        return [6, 2, 24, 17, 12, 6, 2, 12]

    # Функция возвращает данные для проверки теста - отсортированный список с одинаковыми значениями
    @pytest.fixture
    def sorted_qeual_example(self):
        return [2, 2, 6, 6, 12, 12, 17, 24]

    # Тест функции на несортированном списке, проверка значений с сортированным
    def test_1(self, sorted_example, unsorted_example):
        assert lib.sort(unsorted_example) == sorted_example

    # Тест функции с одинаковыми значениями в списке
    def test_2(self, sorted_qeual_example, unsorted_qeual_example):
        assert lib.sort(unsorted_qeual_example) == sorted_qeual_example