"""kilo initial

Revision ID: 4d2943ba4261
Revises: 
Create Date: 2016-07-29 11:21:18.800136

"""

from glance.db.sqlalchemy.alembic_migrations import add_artifacts_tables
from glance.db.sqlalchemy.alembic_migrations import add_images_tables
from glance.db.sqlalchemy.alembic_migrations import add_metadefs_tables
from glance.db.sqlalchemy.alembic_migrations import add_tasks_tables


# revision identifiers, used by Alembic.
revision = '4d2943ba4261'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    add_images_tables.upgrade()
    add_tasks_tables.upgrade()
    add_artifacts_tables.upgrade()
    add_metadefs_tables.upgrade()


def downgrade():
    raise NotImplementedError
