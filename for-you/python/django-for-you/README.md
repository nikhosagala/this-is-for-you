# This is an example of django app

## Available API
 * `/version`

### How to run?

#### If you got docker-compose installed

    docker-compose --build -d

#### Build by yourself

* You need pipenv installed

    `pip install pipenv`

* Install app requirements

    `pipenv install --deploy` 
    
    or you want install everything to your system? 
    
    `pipenv install --deploy --system`

* Activate sub-shell

    `pipenv shell`

* Run django inside sub-shell

    `(.venv)$ python manage.py runserver 0.0.0.0:8000`