# pytest-check-improve
## Here is a variant of improving pytest-check methods to simplify debugging when there are a large number of checks within a single test.
The key improvement is the output to the console of the line number where the check was unsuccessful and adding this data to allure. This improves the readability of the report. Emojis have also been added for faster search in the console and report.

To view the example test report, click the button: [![Allure Report](https://img.shields.io/badge/Allure%20Report-deployed-green)](https://lambotik.github.io/pytest-check-improve)
```
pytest --alluredir=allure-results
```
```
allure serve
```
