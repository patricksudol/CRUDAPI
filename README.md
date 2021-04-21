# CRUD API

A simple CRUD API built using the Django Framework and [Django REST Framework](https://www.django-rest-framework.org)

## Installation

- Install, at a minimum, Python 3.8. A great installation guide, based on your OS, can be found [here](https://realpython.com/installing-python/).
- Install `virtualenv`. This will allow you install Python packages that will remain local to an environment to the Django project as opposed to globally on your entire machine.
  - On macOS and Linux:
    ```bash
    python3 -m pip install --user virtualenv
    ```
  - On Windows:
    ```bash
    python3 -m pip install --user virtualenv
    ```
- Create a virtualenv for the project, the name you pick is trivial but it is common to name it after the project itself.
  - On macOS and Linux
    ```bash
    python3 -m venv name
    ```
  - On Windows
    ```bash
    python3 -m venv name
    ```



```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

