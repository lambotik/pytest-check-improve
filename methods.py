import inspect
import os

import allure
from pytest_check import check


class Improvement:
    @staticmethod
    def get_test_call_site():
        """
        Determines the call line inside the test file based on the call stack.
        Returns: a string in the format 'file_name:line_number' or 'string unknown'.
        """
        stack = inspect.stack()
        for frame in stack:
            filepath = frame.filename.lower()
            # Ищем фрейм, путь которого содержит 'tests' (можно адаптировать под конкретную структуру)
            if "tests" in filepath:
                filename = os.path.basename(frame.filename)
                return f"{filename}:{frame.lineno}"
        return "❌ string unknown"

    def check_equal_with_line(self, actual, expected, note=""):
        """
        Compares actual and expected
        🔎 Adds a step to Allure:
        - on error, includes the line number;
        - on success, only a short mark.
        """

        call_site = self.get_test_call_site()  # фиксируем до вызова check.equal
        if actual != expected:
            msg = f"{note} 📍 ({call_site})"
            with allure.step(f"❌ Error: expected <{expected}>, received <{actual}> — {msg}"):
                print(f"❌ {msg}: expected <{expected}>, received <{actual}>")
        else:
            msg = f"{note}"
            with allure.step(f"✅ Check: value <{actual}> is correct."):
                ...
        check.equal(actual, expected, msg=msg)
