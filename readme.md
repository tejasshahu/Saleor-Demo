I'm using Ubuntu 16.04 and postreSQL version 9.5.11

First of all run below command in terminal:
sudo apt-get install build-essential python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info


Create New postgresql Role and password:
here I have created.
role: 'saleor'
password: 'saleor'

Open postgresql terminal:

Create a new role with rights of create database, create role, password to login and inherit login.
postgres=# CREATE ROLE saleor WITH PASSWORD 'saleor' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;

Create new database with name 'saleor' and ownership of saleor user which we had created using above command.
postgres=# CREATE DATABASE saleor OWNER saleor;

Now install Python 3.6 or later and install Python virtual environment.

To install Python virtual environment:
python3 -m pip install --user virtualenv

After installing virtualenv create a new virtual env(here saleor_basics) for Python 3.6:
python3 -m virtualenv saleor_basics

Activate saleor_basics virtual environment(if you are in virtual env directory)
source bin/activate 

Now clone Saleor repository from Github:
git clone https://github.com/mirumee/saleor.git


Now run below command after going into Saleor directory to install all dependacies.
pip3 install -r requirnments.txt

Set SECRET_KEY environment variable. (Check Django’s documentation for details)
export SECRET_KEY='<mysecretkey>'

Run migrate command:
python manage.py migrate

Install rest of the dependacies using below commands:

Front end dependancies:
npm install

Front assets:
npm run build-assets

Compile Emails:
npm run build-emails

Atlast Start the development server:
python manage.py runserver


Now time to create superuser:
python manage.py createsuperuser

Email: admin@example.com
Password: admin

Create three type of users:

1) Admin
2) Staff user (some rights which can be allowed by admin)
3) Customer/Buyer

Admin: one who has control over all the users.
Staff user: The user who has some rights which is given by admin.
Customer/Buyer: The one who buys product from the website.
