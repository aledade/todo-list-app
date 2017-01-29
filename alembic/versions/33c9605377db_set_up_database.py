"""Set up database

Revision ID: 33c9605377db
Revises:
Create Date: 2017-01-19 07:32:25.625456

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '33c9605377db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        create table tasks (
          id           integer primary key,
          name         text not null,
          description  text,
          completed    boolean default 0,
          deleted      boolean default 0,
          created_at   datetime default current_timestamp,
          updated_at   datetime default current_timestamp
        )
        """
    )


def downgrade():
    op.execute("drop table tasks")
