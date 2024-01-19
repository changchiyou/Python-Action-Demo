# Python-Action-Demo

By adding specific [testing](https://github.com/changchiyou/Github-Action-Test/labels/testing) tag in the pull request, you can actively trigger the complete GitHub Action Python testing workflow.

|                                                   Success                                                   |                                                    Error                                                    |                                                   Failure                                                   |
| :---------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------: |
| ![](https://github.com/changchiyou/Github-Action-Test/assets/46549482/e24fbdb3-bf05-45d9-a585-44e6ad364e35) | ![](https://github.com/changchiyou/Github-Action-Test/assets/46549482/8fad1f6b-3f8d-4968-b357-37c950ce2920) | ![](https://github.com/changchiyou/Github-Action-Test/assets/46549482/a0722041-e9e5-4a6c-861f-47ab18c4f8e0) |

This is particularly useful in private repositories, as although GitHub Actions are free for public repositories, they incur [charges](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions) for private repositories once usage exceeds a certain limit. This workflow allows us to control the time spent on testing , rather than automatically running tests every time a commit is pushed to GitHub 💸.

---

This repository includes the following components:

1. [python.yml](./.github/workflows/python.yml)
2. [ptest/](./ptest/) (for DEMO purpose only)
3. [test/](./tests/) (for DEMO purpose only)

> To locally test whether `ptest` passes the Status Check through the GitHub Action workflow, you can execute the following command:
>
> ```shell
> pylint $(git ls-files '*.py') --rcfile=./.pylintrc; mypy . --exclude build/ --exclude __init__.py --ignore-missing-imports; pytest --cov=./ptest tests/ --cov-report=xml -m "not webtest" -c pytest.ini; coverage report -m --precision=2
> ```
