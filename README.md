# Installation guide

## Retrieve assets with Bower

    npm install -g bower
    bower install

## Set up a virtual environment

    python3 -m venv todo_env
    source todo_env/bin/activate
    pip3 install --editable .

## Run server

    export FLASK_APP=todo
    flask run
