import allure
from methods import Improve

class TestExample(Improve):
    @allure.title('test_example_assert_and_soft_assert')
    def test_example_assert_and_soft_assert(self):
        page = Improve()
        page.check_equal_with_line(1, 2)
        page.check_equal_with_line(2, 2)
        page.check_equal_with_line(3, 3)
        page.check_equal_with_line(['a', 'b', 'c'], ['a', 'b'], 'Lists is dose not match')  # 3
        page.check_equal_with_line('karamba', 'karAmba')  # 2
        page.check_equal_with_line('karamba', 'karAmba')