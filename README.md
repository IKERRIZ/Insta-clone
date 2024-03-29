## Instagram
Web clone of the Instagram app
## Description
This is a simple web clone of the instagram website. A user can create an account and sign into it. The site supports uploading images,liking and commnting on images as well as following other users. Logged in users can view photos uploaded by other users in the home page of app.

## Link to deployed site
https://lucyinsta.herokuapp.com/

## Set Up and Installations
----------------------------
### Prerequisites
* Ubuntu Software
* Python3.6
* Postgres
* python virtualenv
## Clone the Repo
Run the following command on the terminal: git clone github.com/ikerriz/Insta-clone.git && cd Insta-Clone

## Activate virtual environment
Activate virtual environment using python3.6 as default handler

virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
## Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Create the Database
psql
CREATE DATABASE instagram;
## .env file
Create .env file and paste paste the following filling where appropriate:

- SECRET_KEY = '<Secret_key>'
- DBNAME = 'instagram'
- USER = '<Username>'
- PASSWORD = '<password>'
- DEBUG = True

- EMAIL_USE_TLS = True
- EMAIL_HOST = 'smtp.gmail.com'
- EMAIL_PORT = 587
- EMAIL_HOST_USER = '<your-email>'
- EMAIL_HOST_PASSWORD = '<your-password>'

## Run initial Migration
python3.6 manage.py makemigrations insta
python3.6 manage.py migrate
## Run the app
python3.6 manage.py runserver
Open terminal on localhost:8800

 ## Known bugs
Like functionality not well implemented

## Technologies used
- Python 3.6
- HTML
- Bootstrap 3
- Heroku
- Postgresql
## Support and contact details
Contact me for further help/support

License
Copyright (c) ikerriz