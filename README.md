# RestAPITest
A Restful API app which uses PostgreSQL

Since this project uses PostgreSQL it's required that the user and the database that it uses it's created beforehand manually, the ones that are defined by default in the settings.py file are::

user: dbarest
password: 123123123
database: restapidb

It can be created on psql by the following commands:

CREATE USER dbarest WITH PASSWORD '123123123';
CREATE DATABASE restapidb;
GRANT ALL PRIVILEGES ON DATABASE restapidb TO dbarest;

After that, its needed to install the packages that the app uses by doing:

pip install -r requirements.txt

Once it's ready, activate virtualenv, migrate the database and then:

python3 manage.py runserver

You can now enter:

localhost:8000/car 

To create a car object.

And also you can use:

localhost:8000/car/id

To read, update and delete an specific car object.
