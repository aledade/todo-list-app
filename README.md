# Installation guide

## Install system dependencies

You will need Python 3 installed, along with developer libraries.

You should also install and configure `git`, `npm`, and `sqlite3`
however you desire on your system.

## Retrieve assets with Bower

    npm install -g bower
    bower install

## Set up a virtual environment

    python3 -m venv todo_env
    source todo_env/bin/activate
    pip3 install --editable .

## Initialize the SQLite database

    alembic upgrade head

## Run server

    export FLASK_APP=todo
    export FLASK_DEBUG=1
    flask run

# Exercise instructions

Navigate your browser to http://127.0.0.1:5000/ to begin the exercise!


# Repository "how-to"

This is a quick guide to tasks you may wish to execute as part of the exercise
instructions.

## Database & schema changes
This application uses a SQLite database (`todo/todo.db`), with Alembic managing
migrations.

### Reset the database
To reload the database and start with a "clean slate":

    rm todo/todo.db
    alembic upgrade head

### Create new schema migrations

To change anything about the database, you'll make an Alembic migration.
Migrations are just simple SQL. For examples, see `alembic/versions`.

    alembic revision -m 'Some message describing migration'
    alembic upgrade head  # Execute all pending migrations
