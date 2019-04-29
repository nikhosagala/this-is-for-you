# This is an example of flask app

## Available API
 * `/status`
 * `/send_email`
    
    request body :
    
    ```json
    {
       "event_id": 10, 
       "subject": "Email subject", 
       "content": "Email content", 
       "send_date": "29-04-2019T15:00",
    }
    ```
 
 * `/faker`
 
    request body :
    
    ```json
    {
	      "type": "user",
	      "total": 10
    }
    ```
 

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

* Run flask inside sub-shell

    `(.venv)$ python manage.py runserver`
    
    
#### You need to run migration before running the app

`(.venv)$ python manage.py db upgrade`