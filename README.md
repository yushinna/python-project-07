# User Profile with Django
## Description
An user profile web page, which includes first name, last name, email, date of birth, confirm email, short bio and the option to upload an avatar. The profile page should only be visible and editable once the user has logged in.

## Screenshot
### User profile page


## Requirements
Install the project requirements from the provided Pipfile by running the following command in your terminal:
```
pipenv install
```

## Usage
Run server by Django, enter given url (`http://127.0.0.1:8000` by default) on browser so you can interact with the app!

```
# enter virtual environment
pipenv shell

# create database and load data from json file
python manage.py migrate

#run Django app
python manage.py runserver
```
