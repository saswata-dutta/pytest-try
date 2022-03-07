# Sample PyTest setup

Based on [Pytest Good Integration Practices](https://docs.pytest.org/en/7.0.x/explanation/goodpractices.html#tests-outside-application-code).

**Steps to run**

1. Optionally create virtual env `python3 -m venv env` and activate `./env/bin/activate`
2. For first run, install Pytest and current package in editable mode `python3 -m pip install pytest` and `python3 -m pip install -e .`
3. Run tests `python3 -m pytest`
4. Exit venv `deactivate`
