# This is an example of flask app

## Available API
 * `/send_email`
    
    request body :
    
    ```json
    {
       "event_id": 10, 
       "subject": "Email subject", 
       "content": "Email content", 
       "send_date": "29-04-2019T15:00"
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

* You need poetry installed

    `poetry install`

* Install app requirements

    `poetry install` 
    
* Run flask inside sub-shell

    `(.venv)$ flask run`
    
    
#### You need to run migration before running the app

`(.venv)$ alembic upgrade head`


#### How to run celery worker

`(.venv)$ celery -A mailer.tasks.celery worker`