"""drop is_public

Revision ID: newton_contract01
Revises: newton_expand01
Create Date: 2016-08-04 12:22:01.294934

"""

from alembic import op
from sqlalchemy import MetaData, Table

from glance.db import migration

# revision identifiers, used by Alembic.
revision = 'newton_contract01'
down_revision = 'mitaka02'
branch_labels = (migration.CONTRACT_BRANCH,)
depends_on = None


def upgrade():
    meta = MetaData(bind=op.get_bind())
    images = Table('images', meta, autoload=True)

    op.execute(images.update(values={'visibility': 'public'}).where(
        images.c.is_public))
    op.drop_column('images', 'is_public')


def downgrade():
    raise NotImplementedError
