## Demonstration for pydantic-settings bug #298 

See https://github.com/pydantic/pydantic-settings/issues/298

### How to test

 * install poetry
 * poetry install
 * tox

### What I learned

 * The bug is present on python 3.8 to 3.9
 * The bug is NOT present on python 3.10+
 * The bug is related to `injector` but is solved by dropping pipe based field typing in the `main.py` file.

### The bug is described in `test_injector.py`

That’s all :)