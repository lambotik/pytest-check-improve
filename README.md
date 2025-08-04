# pytest-check-improvement
## Here is a variant of improving pytest-check methods to simplify debugging when there are a large number of checks within a single test.
The key improvement is the output to the console of the line number where the check was unsuccessful and adding this data to allure. This improves the readability of the report. Emojis ❌✅ have also been added for faster search in the console and report.

To view the example test report, click the button: [![Allure Report](https://img.shields.io/badge/Allure%20Report-deployed-green)](https://lambotik.github.io/pytest-check-improve)

![Screenshot 1](https://github.com/lambotik/pytest-check-improve/blob/main/screenshots/Снимок%20экрана%202025-07-31%20145350.png?raw=true)
![Screenshot 2](https://github.com/lambotik/pytest-check-improve/blob/main/screenshots/Снимок%20экрана%202025-07-31%20145808.png?raw=true)

```
pytest --alluredir=allure-results
```
```
allure serve
```
