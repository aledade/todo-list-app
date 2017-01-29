""" Create some tasks

Revision ID: 9a00d0ce8719
Revises: 33c9605377db
Create Date: 2017-01-29 15:48:19.518711

"""
import os
from glob import glob

from alembic import op
from sqlalchemy.sql import text
import markdown2


# revision identifiers, used by Alembic.
revision = '9a00d0ce8719'
down_revision = '33c9605377db'
branch_labels = None
depends_on = None


def get_tasks():
    """ Get an ordered list of tasks from file, convert to HTML. """
    for task_file in glob('starting_tasks/*.md'):
        fn = os.path.basename(task_file)
        priority, slug = os.path.splitext(fn)[0].split('-')
        name = slug.replace('_', ' ').capitalize()

        with open(task_file) as contents:
            description = markdown2.markdown(contents.read())
        yield int(priority), name, description


def upgrade():
    conn = op.get_bind()

    insert = "insert into tasks (name, description) values (:name, :description)"

    for _, name, description in sorted(get_tasks(), key=lambda tup: tup[0]):
        conn.execute(text(insert), {'name': name, 'description': description})


def downgrade():
    op.execute("delete from tasks")
