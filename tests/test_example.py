import allure

from methods import Improve


class TestExample:
    @allure.title('Example for equal')
    def test_example_assert_and_soft_assert(self):
        page = Improve()
        page.check_equal_with_line(1, 2)
        page.check_equal_with_line(2, 2)
        page.check_equal_with_line(3, 3)
        page.check_equal_with_line(['a', 'b', 'c'], ['a', 'b'], 'Lists is dose not match')
        page.check_equal_with_line('karamba', 'karAmba')