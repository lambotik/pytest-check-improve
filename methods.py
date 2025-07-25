import inspect
import os

import allure
from pytest_check import check



class Improve:
    @staticmethod
    def get_test_call_site():
        """
        Определяет строку вызова внутри тестового файла на основе стека вызовов.
        Возвращает: строка в формате 'название_файла:номер_строки' или 'строка неизвестна'.
        """
        stack = inspect.stack()
        for frame in stack:
            filepath = frame.filename.lower()
            # Ищем фрейм, путь которого содержит 'tests' (можно адаптировать под конкретную структуру)
            if "tests" in filepath:
                filename = os.path.basename(frame.filename)
                return f"{filename}:{frame.lineno}"
        return "❌ строка неизвестна"


    def check_equal_with_line(self, actual, expected, note=""):
        """
        🔎 Добавляет шаг в Allure:
         — при ошибке включает номер строки;
        — при успехе — только краткую отметку.
        """

        call_site = self.get_test_call_site()  # фиксируем до вызова check.equal
        if actual != expected:
            msg = f"{note} 📍 ({call_site})"
            with allure.step(f"❌ Ошибка: ожидается <{expected}>, получено <{actual}> — {msg}"):
                print(f"❌ {msg}: ожидается <{expected}>, получено <{actual}>")
        else:
            msg = f"{note}"
            with allure.step(f"✅ Проверка: значение корректно <{actual}> — {msg}"):
                ...
        check.equal(actual, expected, msg=msg)