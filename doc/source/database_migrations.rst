..
      Copyright 2017 OpenStack Foundation
      All Rights Reserved.

      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.

======================================================
Writing Database Migrations for Zero-Downtime Upgrades
======================================================

Beginning in Ocata, OpenStack Glance uses Alembic, which replaced SQLAlchemy
Migrate as the database migration engine. Moving to Alembic is particularly
motivated by the zero-downtime upgrade work. Refer to [GSPEC1]_ and [GSPEC2]_
for more information on zero-downtime upgrades in Glance and why a move to
Alembic was deemed necessary.

Essentially, the erstwhile database migrations were always conceived as
monoliths. That is, the idea of impacting schema and data changes at once with
no special consideration for additive and/or contractive schema changes. The
modern database migrations are more sensitive to the characteristics of changes
being attempted and thus classified as expand, migrate and contract migrations.

Expand migrations MUST strictly be additive in nature and optionally include
database triggers that keep the old and new columns in sync. Expand migrations
should be seen as the minimal set of schema changes required by the new
services that can be applied while the old services are still running. Data
migrations MUST NOT attempt any schema changes and only move existing data
between old and new columns such that new services can start consuming the new
tables and/or columns introduced by the expand migrations. Contract migrations
usually include the remaining schema changes required by the new services that
couldn't be applied during expand phase due to their incompatible nature with
the old services.

Alembic Migrations
==================
As mentioned earlier, starting in Ocata all Glance database migrations must be
written for Alembic. All existing Glance migrations have been ported to work
with Alembic. All Glance Alembic migrations can be found here [GMIGS1]_.

Here are some things to keep in mind while writing Glance migrations:









Starting Ocata, Glance needs every database migration to include both
monolithic and Expand-Migrate-Contract (E-M-C) style migrations. At some point
in Pike, E-M-C migrations would be made default. At that point, it would be no
longer required to include monolithic migration scripts.

However, Glance currently still relies on monolith migrations to manage its
database. And, here is how to write monolith Glance migrations using Alembic.


References
==========
.. [GSPEC1] `Database Strategy for Zero-downtime Upgrades in Glance
            <https://specs.openstack.org/openstack/glance-specs/specs/ocata/implemented/glance/alembic-migrations.html>`_
.. [GSPEC2] `Glance Alembic Migrations
            <https://specs.openstack.org/openstack/glance-specs/specs/ocata/implemented/glance/database-strategy-for-rolling-upgrades.html>`_
.. [GMIGS1] `Glance Alembic Migrations
            <http://git.openstack.org/cgit/openstack/glance/tree/glance/db/sqlalchemy/alembic_migrations/versions>`_


