# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2013 OpenStack Foundation
# Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Database setup and migration commands."""

import os
import threading

from oslo_config import cfg
from oslo_db import options as db_options
from stevedore import driver

from glance.db.sqlalchemy import api as db_api


_IMPL = None
_LOCK = threading.Lock()
EXPAND_BRANCH = 'expand'
CONTRACT_BRANCH = 'contract'
MIGRATION_BRANCHES = (EXPAND_BRANCH, CONTRACT_BRANCH)
MITAKA = 'mitaka'
NEWTON = 'newton'
OCATA = 'ocata'
RELEASES = (MITAKA, NEWTON, OCATA)


db_options.set_defaults(cfg.CONF)


def get_backend():
    global _IMPL
    if _IMPL is None:
        with _LOCK:
            if _IMPL is None:
                _IMPL = driver.DriverManager(
                    "glance.database.migration_backend",
                    cfg.CONF.database.backend).driver
    return _IMPL

INIT_VERSION = 0

MIGRATE_REPO_PATH = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'sqlalchemy',
    'migrate_repo',
)


def db_sync(version=None, init_version=0, engine=None):
    """Migrate the database to `version` or the most recent version."""

    if engine is None:
        engine = db_api.get_engine()
    return get_backend().db_sync(engine=engine,
                                 abs_path=MIGRATE_REPO_PATH,
                                 version=version,
                                 init_version=init_version)
