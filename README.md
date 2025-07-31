# pytest-check-improve
## Here is a variant of improving pytest-check methods to simplify debugging when there are a large number of checks within a single test.
The key improvement is the output to the console of the line number where the check was unsuccessful and adding this data to allure. This improves the readability of the report. Emojis ❌✅ have also been added for faster search in the console and report.

To view the example test report, click the button: [![Allure Report](https://img.shields.io/badge/Allure%20Report-deployed-green)](https://lambotik.github.io/pytest-check-improve)

[For example](https://github.com/lambotik/pytest-check-improve/blob/main/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-07-31%20145350.png)
```
pytest --alluredir=allure-results
```
```
allure serve
```
