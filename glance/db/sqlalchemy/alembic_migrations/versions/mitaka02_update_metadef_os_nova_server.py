"""update_metadef_os_nova_server

Revision ID: mitaka02
Revises: mitaka01
Create Date: 2016-08-03 17:23:23.041663

"""

from alembic import op
from sqlalchemy import MetaData, Table


# revision identifiers, used by Alembic.
revision = 'mitaka02'
down_revision = 'mitaka01'
branch_labels = None
depends_on = None


def upgrade():
    migrate_engine = op.get_bind()
    meta = MetaData(bind=migrate_engine)

    resource_types_table = Table('metadef_resource_types', meta, autoload=True)

    resource_types_table.update(values={'name': 'OS::Nova::Server'}).where(
        resource_types_table.c.name == 'OS::Nova::Instance').execute()


def downgrade():
    raise NotImplementedError
