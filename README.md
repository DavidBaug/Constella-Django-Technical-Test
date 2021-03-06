# Contella Intelligence Django technical test

### Installation

In order to run the server you will have to install Python. Once you have Python working on your machine you can run the server running the following commands:

###### Virtual environment creation
Once you have downloaded your repository create a virtual environment on the directory at the same level as <i>constella_intelligence</i> running the following:
1. `python -m venv ./myenv`
2. `source ./myenv/bin/activate`
3. `python -m pip install -U pip django`

###### Django project initialitation

In your project open a terminal on <i>constella_intelligence/src</i> and run the following:

1. `cd constella_intelligence`
2. `pip install -r requirements.txt`
3. `cd src`
4. `cp main/settings/local.sample.env main/settings/local.env`
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py runserver`