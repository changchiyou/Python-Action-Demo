# Github-Action-Test

Github Action workflow for Python development.

This is a test.

---

This repository includes the following components:

1. [python.yml](./.github/workflows/python.yml)
2. [ptest/](./ptest/) (DEMO)
3. [test/](./tests/) (DEMO)

> To locally test whether `ptest`` passes the Status Check through the GitHub Action workflow, you can execute the following command:
>
> ```shell
> pylint $(git ls-files '*.py') --rcfile=./.pylintrc; mypy . --exclude build/ --exclude __init__.py --ignore-missing-imports; pytest --cov=./ptest tests/ --cov-report=xml -m "not webtest" -c pytest.ini; coverage report -m --precision=2
> ```
