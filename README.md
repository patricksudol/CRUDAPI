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
    python3 -m venv environment_name
    ```
  - On Windows
    ```bash
    python3 -m venv environment_name
    ```
- Activate the virtualenv:
  - On macOS and Linux
    ```bash
    source environment_name/bin/activate
    ```
  - On Windows
    ```bash
    .\env\Scripts\activate
  - Your terminal then should look something like this:
    ```bash
    (environment_name) patricksudol@patricks-mbp
- With your environment still activated navigate to the root of the project and run:
  ```bash
  ./manage pip install -r requirements.txt
  ```
  - This will install all dependencies to run your application including Django, Django Rest Framework, and some listing libraries.
- Then to apply migrations run:
  ```bash
  ./manage.py migrate
  ```
- Then you should be ready to run the application:
  ```bash
  ./manage.py runserver
  ```
  - The API is now accessible via `http://127.0.0.1:8000/`

## API Endpoints

- You can call the following endpoints ([Postman](https://www.postman.com) is a great tool to test APIs):
  - POST: ```http://127.0.0.1:8000/widgets/```
    - Example of raw JSON body:
    ```bash
    {
       "name": "Facebook"
       "number_of_parts": 5
    }
    ```
    - You will get something returned along the lines of:
    ```bash
     {
       "id": "5742c072-a4f4-4e16-b223-abbb661fd1cc",
       "name": "Facebook",
       "number_of_parts": 5,
       "created_date": "2021-04-21T02:50:29.718208Z",
       "updated_date": "2021-04-21T03:54:08.044008Z"
     }
  - PATCH: ```http://127.0.0.1:8000/widgets/{id}/```
    - Example of raw JSON body:
    ```bash
    {
       "number_of_parts": 5
    }
    ```
    - You will get something returned along the lines of:
    ```bash
     {
       "id": "5742c072-a4f4-4e16-b223-abbb661fd1cc",
       "name": "Facebook",
       "number_of_parts": 10,
       "created_date": "2021-04-21T02:50:29.718208Z",
       "updated_date": "2021-04-21T03:54:08.044008Z"
     }
  - GET: ```http://127.0.0.1:8000/widgets/```
    - You will get something returned along the lines of:
    ```bash
     [
       {
           "id": "5742c072-a4f4-4e16-b223-abbb661fd1cc",
           "name": "Facebook",
           "number_of_parts": 10,
           "created_date": "2021-04-21T02:50:29.718208Z",
           "updated_date": "2021-04-21T03:58:17.272102Z"
       }
    ]
  - GET (List): ```http://127.0.0.1:8000/widgets/{id}/```
    - You will get something returned along the lines of:
    ```bash
       {
           "id": "5742c072-a4f4-4e16-b223-abbb661fd1cc",
           "name": "Facebook",
           "number_of_parts": 10,
           "created_date": "2021-04-21T02:50:29.718208Z",
           "updated_date": "2021-04-21T03:58:17.272102Z"
       }
  - Delete: ```http://127.0.0.1:8000/widgets/{id}/```
    - You will receive an HTTP `204` code
# Testing
 - You can run unit tests by calling:
   ```bash
   ./manage.py test
   ```
 - And expect an output such as
   ```bash
   Creating test database for alias 'default'...
   System check identified no issues (0 silenced).
   ......
   ----------------------------------------------------------------------
   Ran 6 tests in 0.025s

   OK
   Destroying test database for alias 'default'...
   ```
