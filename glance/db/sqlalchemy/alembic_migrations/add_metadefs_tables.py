from alembic import op
from sqlalchemy.schema import (
    Column, PrimaryKeyConstraint, ForeignKeyConstraint)

from glance.db.sqlalchemy.migrate_repo.schema import (
    Boolean, DateTime, Integer, String, Text)  # noqa
from glance.db.sqlalchemy.models import JSONEncodedDict


def _add_metadef_namespaces_table():
    op.create_table('metadef_namespaces',
                    Column('id', Integer(), nullable=False),
                    Column('namespace', String(length=80), nullable=False),
                    Column('display_name', String(length=80), nullable=True),
                    Column('description', Text(), nullable=True),
                    Column('visibility', String(length=32), nullable=True),
                    Column('protected', Boolean(), nullable=True),
                    Column('owner', String(length=255), nullable=False),
                    Column('created_at', DateTime(), nullable=False),
                    Column('updated_at', DateTime(), nullable=True),
                    PrimaryKeyConstraint('id'),
                    mysql_engine='InnoDB',
                    mysql_charset='utf8',
                    extend_existing=True)

    op.create_index('ix_metadef_namespaces_namespace', 
                    'metadef_namespaces', 
                    ['namespace'], 
                    unique=False)
    op.create_index('ix_metadef_namespaces_owner', 
                    'metadef_namespaces', 
                    ['owner'], 
                    unique=False)


def _add_metadef_properties_table():
    op.create_table('metadef_properties',
                    Column('id', Integer(), nullable=False),
                    Column('namespace_id', Integer(), nullable=False),
                    Column('name', String(length=80), nullable=False),
                    Column('json_schema', JSONEncodedDict(), nullable=False),
                    Column('created_at', DateTime(), nullable=False),
                    Column('updated_at', DateTime(), nullable=True),
                    ForeignKeyConstraint(['namespace_id'], 
                                         ['metadef_namespaces.id'], ),
                    PrimaryKeyConstraint('id'),
                    mysql_engine='InnoDB',
                    mysql_charset='utf8',
                    extend_existing=True)

    op.create_index('ix_metadef_properties_name',
                    'metadef_properties',
                    ['name'],
                    unique=False)
    op.create_index('ix_metadef_properties_namespace_id',
                    'metadef_properties',
                    ['namespace_id'],
                    unique=False)


def _add_metadef_tags_table():
    op.create_table('metadef_tags',
                    Column('id', Integer(), nullable=False),
                    Column('namespace_id', Integer(), nullable=False),
                    Column('name', String(length=80), nullable=False),
                    Column('created_at', DateTime(), nullable=False),
                    Column('updated_at', DateTime(), nullable=True),
                    ForeignKeyConstraint(['namespace_id'], 
                                         ['metadef_namespaces.id'], ),
                    PrimaryKeyConstraint('id'),
                    mysql_engine='InnoDB',
                    mysql_charset='utf8',
                    extend_existing=True)
    
    op.create_index('ix_metadef_tags_name', 
                    'metadef_tags', 
                    ['name'], 
                    unique=False)
    op.create_index('ix_metadef_tags_namespace_id', 
                    'metadef_tags', 
                    ['namespace_id', 'name'], 
                    unique=False)


def _add_metadef_objects_table():
    op.create_table('metadef_objects',
                    Column('id', Integer(), nullable=False),
                    Column('namespace_id', Integer(), nullable=False),
                    Column('name', String(length=80), nullable=False),
                    Column('description', Text(), nullable=True),
                    Column('required', Text(), nullable=True),
                    Column('json_schema', JSONEncodedDict(), nullable=False),
                    Column('created_at', DateTime(), nullable=False),
                    Column('updated_at', DateTime(), nullable=True),
                    ForeignKeyConstraint(['namespace_id'], 
                                         ['metadef_namespaces.id'], ),
                    PrimaryKeyConstraint('id'),
                    mysql_engine='InnoDB',
                    mysql_charset='utf8',
                    extend_existing=True)
    
    op.create_index('ix_metadef_objects_name', 
                    'metadef_objects', 
                    ['name'], 
                    unique=False)
    op.create_index('ix_metadef_objects_namespace_id', 
                    'metadef_objects', 
                    ['namespace_id'], 
                    unique=False)


def _add_metadef_resource_types_table():
    op.create_table('metadef_resource_types',
                    Column('id', Integer(), nullable=False),
                    Column('name', String(length=80), nullable=False),
                    Column('protected', Boolean(), nullable=False),
                    Column('created_at', DateTime(), nullable=False),
                    Column('updated_at', DateTime(), nullable=True),
                    PrimaryKeyConstraint('id'),
                    mysql_engine='InnoDB',
                    mysql_charset='utf8',
                    extend_existing=True)

    op.create_index('ix_metadef_resource_types_name',
                    'metadef_resource_types',
                    ['name'],
                    unique=False)


def _add_metadef_namespace_resource_types_table():
    op.create_table('metadef_namespace_resource_types',
                    Column('resource_type_id', Integer(), nullable=False),
                    Column('namespace_id', Integer(), nullable=False),
                    Column('properties_target',
                           String(length=80),
                           nullable=True),
                    Column('prefix', String(length=80), nullable=True),
                    Column('created_at', DateTime(), nullable=False),
                    Column('updated_at', DateTime(), nullable=True),
                    ForeignKeyConstraint(['namespace_id'],
                                         ['metadef_namespaces.id'], ),
                    ForeignKeyConstraint(['resource_type_id'],
                                         ['metadef_resource_types.id'], ),
                    PrimaryKeyConstraint('resource_type_id', 'namespace_id'),
                    mysql_engine='InnoDB',
                    mysql_charset='utf8',
                    extend_existing=True)

    op.create_index('ix_metadef_ns_res_types_namespace_id',
                    'metadef_namespace_resource_types',
                    ['namespace_id'],
                    unique=False)
    op.create_index('ix_metadef_ns_res_types_res_type_id_ns_id',
                    'metadef_namespace_resource_types',
                    ['resource_type_id', 'namespace_id'],
                    unique=False)


def upgrade():
    _add_metadef_namespaces_table()
    _add_metadef_properties_table()
    _add_metadef_tags_table()
    _add_metadef_objects_table()
    _add_metadef_resource_types_table()
    _add_metadef_namespace_resource_types_table()
