from sqlite3 import dbapi2 as sqlite3
import os

from flask import Flask, g, render_template


app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'todo.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='password'
))


def connect_db():
    """ Connects to the specific database. """
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """ Opens a new database connection if needed. """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """ Closes the database again at the end of the request. """
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def hello_world():
    return render_template('base.html')