"""add visibility

Revision ID: newton_expand01
Revises: mitaka02
Create Date: 2016-08-04 12:08:08.258679

"""
from alembic import op
from sqlalchemy import MetaData, Table, Column, Enum, Index

from glance.db import migration

# revision identifiers, used by Alembic.
revision = 'newton_expand01'
down_revision = 'mitaka02'
branch_labels = (migration.EXPAND_BRANCH,)
depends_on = None


def upgrade():
    meta = MetaData(bind=op.get_bind())
    images = Table('images', meta, autoload=True)

    # TODO(tsymanczyk): would be nice if this enum weren't copypaste
    enum = Enum('private', 'public', 'shared', 'community',
                metadata=meta,
                name='image_visibility')
    enum.create()

    op.add_column('images', Column('visibility',
                                   enum,
                                   nullable=False,
                                   server_default='private'))
    op.create_index('visibility_image_idx',
                    'images',
                    ['visibility'],
                    unique=False)


def downgrade():
    raise NotImplementedError
