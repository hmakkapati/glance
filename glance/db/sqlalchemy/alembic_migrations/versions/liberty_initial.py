"""liberty initial

Revision ID: liberty
Revises:
Create Date: 2016-08-03 16:06:59.657433

"""

from glance.db.sqlalchemy.alembic_migrations import add_artifacts_tables
from glance.db.sqlalchemy.alembic_migrations import add_images_tables
from glance.db.sqlalchemy.alembic_migrations import add_metadefs_tables
from glance.db.sqlalchemy.alembic_migrations import add_tasks_tables

# revision identifiers, used by Alembic.
revision = 'liberty'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    add_images_tables.upgrade()
    add_tasks_tables.upgrade()
    add_metadefs_tables.upgrade()
    add_artifacts_tables.upgrade()


def downgrade():
    raise NotImplementedError
