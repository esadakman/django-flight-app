<!-- Please update value in the {}  -->

<h1 align="center">Django Flight App</h1>

<div align="center">
  <h3> 
    <a href="https://github.com/esadakman/django-flight-app">
      Project
    </a> 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Acknowledgements](#acknowledgements)
- [Overview](#overview)
- [Built With](#built-with)
- [Project Structure](#project-structure)
- [How to use](#how-to-use)
- [Contact](#contact)


## Acknowledgements

- I created a Flight Reservation API with Django Rest Framework that allows users to
    - register/login/logout
    - crud operations for flights
    - crud operations for reservations

<!-- OVERVIEW -->
## Overview

![flight](https://user-images.githubusercontent.com/98649983/193425444-38f82341-9bd8-4981-ac5a-fb35e07dd4e6.gif)


### Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Django
- Django Rest Framework
- Django Rest Auth
- Django Debug Toolbar
- PosrtgreSQL
- Swagger

## Project Structure

```bash
.──── django-flight-app (repo)
│
├── main
│     ├── __pycache__ 
│     ├── __init__.py 
│     ├── asgi.py
│     ├── urls.py
│     ├── wsgi.py
│     └── settings
│           ├── __pycache__
│           ├── db.sqlite3
│           ├── __init__.py 
│           ├── base.py
│           ├── dev.py 
│           └── prod.py
│─── flight
│       ├── __pycache__
│       │── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       ├── models.py 
│       ├── permissions.py 
│       ├── serializers.py 
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├──── users
│       ├── __pycache__
│       ├── migrations
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── signals.py 
│       ├── tests.py
│       ├── urls.py
│       └── views.py 
├── manage.py
├── db.sqlite3
├── debug.log
├── requirements.txt
└── .env

```

## How To Use 

To clone and run this application, you'll need [Git](https://git-scm.com)

```bash
# Clone this repository
$ git clone https://github.com/esadakman/django-flight-app 

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt 

# Add .env file for secret key, ENV_NAME and SQL informations 

- Create a .env file for =>
  -- SECRET_KEY,
  -- ENV_NAME  
  -- DEBUG value, 
  -- SQL_DATABASE,
  -- SQL_USER,
  -- SQL_PASSWORD,
  -- SQL_HOST and
  -- SQL_PORT values

- After these you can run the project as usual => 

# Run the app
    $ python manage.py runserver
```

## Contact

- Website [@esadakman](https://esadakman.github.io/)
- GitHub [@esadakman](https://github.com/esadakman)
- Linkedin [@esadakman](https://www.linkedin.com/in/esadakman/)