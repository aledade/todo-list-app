from sqlite3 import dbapi2 as sqlite3
import os

from flask import Flask, g, json, render_template
from flask_assets import Environment, Bundle


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


# set up asset management
assets = Environment(app)
a_s = {
    'base_css': Bundle(
        'css/base.css',
        'bower_components/bootstrap/dist/css/bootstrap.css',
        output='gen/base.css'
    ),

    # all the JS for our single-page application
    'main_js': Bundle(
        'bower_components/jquery/dist/jquery.js',
        'bower_components/angular/angular.js',
        'bower_components/angular-sanitize/angular-sanitize.js',
        'bower_components/angular-animate/angular-animate.js',
        'bower_components/bootstrap/dist/js/bootstrap.js',
        'bower_components/angular-bootstrap/ui-bootstrap-tpls.js',
        'bower_components/angular-ui-sortable/sortable.js',
        'bower_components/jquery-ui/jquery-ui.js',

        'js/app.js',
        'js/tasks.js',
        output='gen/main.js'
    ),
}

for ast, bun in a_s.items():
    assets.register(ast, bun)


@app.route('/')
def instructions():
    return render_template('instructions.html')


@app.route('/tasks')
def manage_tasks():
    return render_template('manage_tasks.html')


@app.route('/api/tasks/')
def get_tasks():
    db = get_db()
    cur = db.execute("""
        select id,
               name,
               description,
               created_at,
               updated_at
          from tasks
    """)
    return json.jsonify(tasks=[dict(row) for row in cur])
